from django import template

register = template.Library()

@register.filter
def get_item(d, k):
    try:
        return d.get(k)
    except Exception:
        return ""

@register.filter
def attr(obj, name):
    """{{ obj|attr:'field_name' }} -> value"""
    return getattr(obj, name, None)

@register.simple_tag
def fields_for(obj):
    """
    Usage: {% fields_for t as fields %}
    Returns a list of dicts with name, db_column, type, attname.
    """
    fields = []
    for f in obj._meta.fields:
        fields.append({
            "name": f.name,
            "db_column": f.db_column or f.column,
            "type": f.get_internal_type(),
            "attname": f.attname,
        })
    return fields
