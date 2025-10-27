from django.db import transaction
from django.http import Http404
from django.shortcuts import redirect
from django.db.models import Case, When, Value, CharField
from django.views.generic import ListView, UpdateView, TemplateView

from .models import TestsTodo, TradeResults, DailyProfits
from .forms import TaskForm


STATUS = {
    0: 'waiting completion',
    1: 'in progres',
    2: 'done',
    4: 'failed'
}

ORDER_OPTIONS = ["testid", "-testid", "testname", "-testname", "status", "-status"]


def serialize_model_fields(instance):
    """
    Return a list of dicts describing all concrete fields of a model instance:
    Python field name, DB column, Django type, and current value.
    """
    items = []
    opts = instance._meta
    for f in opts.fields:
        items.append({
            "name": f.name,
            "db_column": (f.db_column or f.column),
            "type": f.get_internal_type(),
            "value": getattr(instance, f.attname, None),
        })
    return items


class TaskListView(ListView):
    model = TestsTodo
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 25

    def get_paginate_by(self, queryset):
        try:
            limit = int(self.request.GET.get('limit', self.paginate_by))
            return max(1, min(limit, 200))
        except ValueError:
            return self.paginate_by

    def get_ordering(self):
        order = self.request.GET.get('order', '-testid')
        allowed = {'testid', 'testname', 'status', '-testid', '-testname', '-status'}
        return order if order in allowed else '-testid'

    def get_queryset(self):
        qs = super().get_queryset()
        status_param = self.request.GET.get("status")
        if status_param is not None:
            try:
                s = int(status_param)
                qs = qs.filter(status=s)
            except ValueError:
                pass

        qs = qs.annotate(
            status_label=Case(
                When(status=0, then=Value('waiting completion')),
                When(status=1, then=Value('in progress')),
                When(status=2, then=Value('done')),
                When(status=4, then=Value('failed')),
                default=Value(''),
                output_field=CharField(),
            )
        )
        return qs.order_by(self.get_ordering())

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['STATUS'] = STATUS
        ctx['order_options'] = ORDER_OPTIONS
        return ctx


class TaskUpdateView(UpdateView):
    model = TestsTodo
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'

    def form_valid(self, form):
        with transaction.atomic():
            task = form.save(commit=False)
            task.status = 0
            task.save()
            self._delete_previous_results(task)
        return redirect('task_list')

    @staticmethod
    def _delete_previous_results(task: TestsTodo):
        if hasattr(TradeResults, 'test_id'):
            TradeResults.objects.filter(test_id=task.testid).delete()
            return

        if task.testname:
            TradeResults.objects.filter(testname=task.testname).delete()


class TaskResultsView(TemplateView):
    template_name = 'tasks/task_results.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        task = TestsTodo.objects.get(pk=self.kwargs['pk'])
        if task.status != 2:
            raise Http404('Results are only available for completed tasks')

        tr = (TradeResults.objects
              .filter(testname=task.testname)
              .order_by("-id").first())

        daily = []
        if tr:
            q = (DailyProfits.objects
                 .filter(trade_result=tr)
                 .order_by('date')
                 .only('date', 'profitloss', 'netliquidity'))
            prev_net = None
            for row in q:
                pl = row.profitloss
                if pl is None and row.netliquidity is not None and prev_net is not None:
                    pl = row.netliquidity - prev_net
                daily.append({
                    'date': row.date,
                    'profitloss': row.profitloss,
                    'pl_derived': pl,
                })
                prev_net = row.netliquidity

        ctx.update({
            'task': task,
            'trade_result': tr,
            'daily_profits': daily,
            'todo_fields': serialize_model_fields(task),
        })
        return ctx
