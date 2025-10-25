# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestsTodo(models.Model):
    testid = models.AutoField(primary_key=True)
    testname = models.CharField(max_length=255)
    rangestart = models.DateField(db_column='rangeStart', blank=True, null=True)  # Field name made lowercase.
    rangeend = models.DateField(db_column='rangeEnd', blank=True, null=True)  # Field name made lowercase.
    underlying = models.CharField(max_length=4, blank=True, null=True)
    profit_type = models.CharField(max_length=20, blank=True, null=True)
    add_leg = models.IntegerField(blank=True, null=True)
    useexactdte = models.IntegerField(db_column='useExactDte', blank=True, null=True)  # Field name made lowercase.
    roundstrikestonearest = models.IntegerField(db_column='roundStrikesToNearest', blank=True, null=True)  # Field name made lowercase.
    roundstrikestonearestamount = models.DecimalField(db_column='roundStrikesToNearestAmount', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    startingfunds = models.DecimalField(db_column='startingFunds', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    allocationpercentage = models.IntegerField(db_column='allocationPercentage', blank=True, null=True)  # Field name made lowercase.
    maxopentrades = models.IntegerField(db_column='maxOpenTrades', blank=True, null=True)  # Field name made lowercase.
    pruneoldesttrades = models.IntegerField(db_column='pruneOldestTrades', blank=True, null=True)  # Field name made lowercase.
    maxcontractspertrade = models.SmallIntegerField(db_column='maxContractsPerTrade', blank=True, null=True)  # Field name made lowercase.
    ignoremarginrequirements = models.IntegerField(db_column='ignoreMarginRequirements', blank=True, null=True)  # Field name made lowercase.
    maxallocationamount = models.IntegerField(db_column='maxAllocationAmount', blank=True, null=True)  # Field name made lowercase.
    minentrytime = models.CharField(db_column='minEntryTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxentrytime = models.CharField(db_column='maxEntryTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usefloatingentrytime = models.IntegerField(db_column='useFloatingEntryTime', blank=True, null=True)  # Field name made lowercase.
    frequency = models.CharField(max_length=20, blank=True, null=True)
    frequency_days = models.CharField(max_length=50, blank=True, null=True)
    use_vix = models.IntegerField(blank=True, null=True)
    min_vix = models.SmallIntegerField(blank=True, null=True)
    max_vix = models.SmallIntegerField(blank=True, null=True)
    stoplosswhat = models.CharField(db_column='stopLossWhat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stoplossamount = models.DecimalField(db_column='stopLossAmount', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    useunderlyingpricemovement = models.IntegerField(db_column='useUnderlyingPriceMovement', blank=True, null=True)  # Field name made lowercase.
    exitotmshortput = models.DecimalField(db_column='exitOTMShortPut', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exitotmshortputwhat = models.CharField(db_column='exitOTMShortPutWhat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usecommissionfees = models.IntegerField(db_column='useCommissionFees', blank=True, null=True)  # Field name made lowercase.
    opencontractcommission = models.DecimalField(db_column='openContractCommission', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    closecontractcommission = models.DecimalField(db_column='closeContractCommission', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    useslippage = models.IntegerField(db_column='useSlippage', blank=True, null=True)  # Field name made lowercase.
    entryslippage = models.DecimalField(db_column='entrySlippage', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    exitslippage = models.DecimalField(db_column='exitSlippage', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stoplossslippage = models.DecimalField(db_column='stopLossSlippage', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    strategy_point = models.CharField(max_length=255, blank=True, null=True)
    strike_offset_type = models.CharField(max_length=255, blank=True, null=True)
    entrytime = models.CharField(db_column='entryTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    frequency_month_entry_day = models.CharField(max_length=50, blank=True, null=True)
    frequency_month_entry_ordinal = models.CharField(max_length=50, blank=True, null=True)
    specificentrydays = models.CharField(db_column='specificEntryDays', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entryvixgaptype = models.CharField(db_column='entryVixGapType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entryvixmingapup = models.IntegerField(db_column='entryVixMinGapUp', blank=True, null=True)  # Field name made lowercase.
    entryvixmaxgapup = models.IntegerField(db_column='entryVixMaxGapUp', blank=True, null=True)  # Field name made lowercase.
    entryvixmingapdown = models.IntegerField(db_column='entryVixMinGapDown', blank=True, null=True)  # Field name made lowercase.
    entryvixmaxgapdown = models.IntegerField(db_column='entryVixMaxGapDown', blank=True, null=True)  # Field name made lowercase.
    entryvixmovetype = models.CharField(db_column='entryVixMoveType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entryvixminmoveup = models.IntegerField(db_column='entryVixMinMoveUp', blank=True, null=True)  # Field name made lowercase.
    entryvixmaxmoveup = models.IntegerField(db_column='entryVixMaxMoveUp', blank=True, null=True)  # Field name made lowercase.
    entryvixminmovedown = models.IntegerField(db_column='entryVixMinMoveDown', blank=True, null=True)  # Field name made lowercase.
    entryvixmaxmovedown = models.IntegerField(db_column='entryVixMaxMoveDown', blank=True, null=True)  # Field name made lowercase.
    entryminvix9dvixratio = models.IntegerField(db_column='entryMinVix9DVixRatio', blank=True, null=True)  # Field name made lowercase.
    entrymaxvix9dvixratio = models.IntegerField(db_column='entryMaxVix9DVixRatio', blank=True, null=True)  # Field name made lowercase.
    entrysmacondition = models.CharField(db_column='entrySmaCondition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entrysmalength = models.IntegerField(db_column='entrySmaLength', blank=True, null=True)  # Field name made lowercase.
    entrysmalengthlesser = models.IntegerField(db_column='entrySmaLengthLesser', blank=True, null=True)  # Field name made lowercase.
    entryintradayemacondition = models.CharField(db_column='entryIntradayEmaCondition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entryintradayemalength = models.IntegerField(db_column='entryIntradayEmaLength', blank=True, null=True)  # Field name made lowercase.
    entryintradayemalengthlesser = models.IntegerField(db_column='entryIntradayEmaLengthLesser', blank=True, null=True)  # Field name made lowercase.
    entryminrsi = models.IntegerField(db_column='entryMinRsi', blank=True, null=True)  # Field name made lowercase.
    entrymaxrsi = models.IntegerField(db_column='entryMaxRsi', blank=True, null=True)  # Field name made lowercase.
    entrymingapup = models.IntegerField(db_column='entryMinGapUp', blank=True, null=True)  # Field name made lowercase.
    entrymaxgapup = models.IntegerField(db_column='entryMaxGapUp', blank=True, null=True)  # Field name made lowercase.
    entrymingapdown = models.IntegerField(db_column='entryMinGapDown', blank=True, null=True)  # Field name made lowercase.
    entrymaxgapdown = models.IntegerField(db_column='entryMaxGapDown', blank=True, null=True)  # Field name made lowercase.
    entrygaptype = models.CharField(db_column='entryGapType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entryminmoveup = models.IntegerField(db_column='entryMinMoveUp', blank=True, null=True)  # Field name made lowercase.
    entrymaxmoveup = models.IntegerField(db_column='entryMaxMoveUp', blank=True, null=True)  # Field name made lowercase.
    entryminmovedown = models.IntegerField(db_column='entryMinMoveDown', blank=True, null=True)  # Field name made lowercase.
    entrymaxmovedown = models.IntegerField(db_column='entryMaxMoveDown', blank=True, null=True)  # Field name made lowercase.
    entrymovetype = models.CharField(db_column='entryMoveType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entrymindix = models.IntegerField(db_column='entryMinDix', blank=True, null=True)  # Field name made lowercase.
    entrymaxdix = models.IntegerField(db_column='entryMaxDix', blank=True, null=True)  # Field name made lowercase.
    entrymingex = models.IntegerField(db_column='entryMinGex', blank=True, null=True)  # Field name made lowercase.
    entrymaxgex = models.IntegerField(db_column='entryMaxGex', blank=True, null=True)  # Field name made lowercase.
    entrymingxv = models.IntegerField(db_column='entryMinGxv', blank=True, null=True)  # Field name made lowercase.
    entrymaxgxv = models.IntegerField(db_column='entryMaxGxv', blank=True, null=True)  # Field name made lowercase.
    openingrangebreakoutendtime = models.CharField(db_column='openingRangeBreakoutEndTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    breakoutcondition = models.CharField(db_column='breakoutCondition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    useopeningrangebreakouthighlow = models.IntegerField(db_column='useOpeningRangeBreakoutHighLow', blank=True, null=True)  # Field name made lowercase.
    maxprofit = models.IntegerField(db_column='maxProfit', blank=True, null=True)  # Field name made lowercase.
    profittype = models.CharField(db_column='profitType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trailingstopprofitthreshold = models.IntegerField(db_column='trailingStopProfitThreshold', blank=True, null=True)  # Field name made lowercase.
    trailingstopprofitthresholdtype = models.CharField(db_column='trailingStopProfitThresholdType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    useintraminutenbboonlystop = models.CharField(db_column='useIntraMinuteNbboOnlyStop', max_length=10, blank=True, null=True)  # Field name made lowercase.
    useintraminutestop = models.IntegerField(db_column='useIntraMinuteStop', blank=True, null=True)  # Field name made lowercase.
    profitallocationpercentage = models.IntegerField(db_column='profitAllocationPercentage', blank=True, null=True)  # Field name made lowercase.
    profittarget = models.IntegerField(db_column='profitTarget', blank=True, null=True)  # Field name made lowercase.
    stoploss = models.IntegerField(db_column='stopLoss', blank=True, null=True)  # Field name made lowercase.
    exitatdte = models.IntegerField(db_column='exitAtDte', blank=True, null=True)  # Field name made lowercase.
    exitatdit = models.IntegerField(db_column='exitAtDit', blank=True, null=True)  # Field name made lowercase.
    exitatmit = models.IntegerField(db_column='exitAtMit', blank=True, null=True)  # Field name made lowercase.
    exittime = models.CharField(db_column='exitTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exitvixmoveup = models.IntegerField(db_column='exitVixMoveUp', blank=True, null=True)  # Field name made lowercase.
    exitvixmovedown = models.IntegerField(db_column='exitVixMoveDown', blank=True, null=True)  # Field name made lowercase.
    exitvixmovetype = models.CharField(db_column='exitVixMoveType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    exitvix9dmoveup = models.IntegerField(db_column='exitVix9DMoveUp', blank=True, null=True)  # Field name made lowercase.
    exitvix9dmovedown = models.IntegerField(db_column='exitVix9DMoveDown', blank=True, null=True)  # Field name made lowercase.
    exitmaxvix9dvixratio = models.CharField(db_column='exitMaxVix9DVixRatio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    exitminvix9dvixratio = models.IntegerField(db_column='exitMinVix9DVixRatio', blank=True, null=True)  # Field name made lowercase.
    exitvix9dmovetype = models.IntegerField(db_column='exitVix9DMoveType', blank=True, null=True)  # Field name made lowercase.
    exitintradayemacondition = models.CharField(db_column='exitIntradayEmaCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exitintradayemalength = models.IntegerField(db_column='exitIntradayEmaLength', blank=True, null=True)  # Field name made lowercase.
    exitintradayemalengthlesser = models.IntegerField(db_column='exitIntradayEmaLengthLesser', blank=True, null=True)  # Field name made lowercase.
    exitmaxrsi = models.IntegerField(db_column='exitMaxRsi', blank=True, null=True)  # Field name made lowercase.
    exitminrsi = models.IntegerField(db_column='exitMinRsi', blank=True, null=True)  # Field name made lowercase.
    exitsmacondition = models.CharField(db_column='exitSmaCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exitsmalength = models.IntegerField(db_column='exitSmaLength', blank=True, null=True)  # Field name made lowercase.
    exitsmalengthlesser = models.IntegerField(db_column='exitSmaLengthLesser', blank=True, null=True)  # Field name made lowercase.
    exitunderlyingpricemovedown = models.IntegerField(db_column='exitUnderlyingPriceMoveDown', blank=True, null=True)  # Field name made lowercase.
    exitunderlyingpricemovetype = models.CharField(db_column='exitUnderlyingPriceMoveType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    exitunderlyingpricemoveup = models.IntegerField(db_column='exitUnderlyingPriceMoveUp', blank=True, null=True)  # Field name made lowercase.
    exitabovedelta = models.IntegerField(db_column='exitAboveDelta', blank=True, null=True)  # Field name made lowercase.
    exitbelowdelta = models.IntegerField(db_column='exitBelowDelta', blank=True, null=True)  # Field name made lowercase.
    closeopentradesattestcompletion = models.IntegerField(db_column='closeOpenTradesAtTestCompletion', blank=True, null=True)  # Field name made lowercase.
    ignorewidebidasktrades = models.IntegerField(db_column='ignoreWideBidAskTrades', blank=True, null=True)  # Field name made lowercase.
    minentrypremium = models.IntegerField(db_column='minEntryPremium', blank=True, null=True)  # Field name made lowercase.
    maxentrypremium = models.IntegerField(db_column='maxEntryPremium', blank=True, null=True)  # Field name made lowercase.
    isentrypremiumdebit = models.CharField(db_column='isEntryPremiumDebit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    blackoutdays = models.CharField(db_column='blackoutDays', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maxdailyreentries = models.IntegerField(db_column='maxDailyReentries', blank=True, null=True)  # Field name made lowercase.
    reentrystarttime = models.CharField(db_column='reentryStartTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reentryendtime = models.CharField(db_column='reentryEndTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reentrydelayminutes = models.IntegerField(db_column='reentryDelayMinutes', blank=True, null=True)  # Field name made lowercase.
    reentryconditions = models.IntegerField(db_column='reentryConditions', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tests_todo'


class TestsLegs(models.Model):
    pk = models.CompositePrimaryKey('testid', 'leg')
    testid = models.ForeignKey(TestsTodo, models.DO_NOTHING, db_column='testid', related_name='legs')
    leg = models.IntegerField()
    legsell = models.IntegerField()
    legbuy = models.IntegerField()
    legcall = models.IntegerField()
    legput = models.IntegerField()
    qty = models.IntegerField()
    type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    dte = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tests_legs'
        unique_together = (('testid', 'leg'),)


class TradeResults(models.Model):
    id = models.AutoField(primary_key=True)
    startingfunds = models.DecimalField(db_column='startingFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    endingfunds = models.DecimalField(db_column='endingFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    minfunds = models.DecimalField(db_column='minFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    maxfunds = models.DecimalField(db_column='maxFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    profit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    numberoftrades = models.IntegerField(db_column='numberOfTrades', blank=True, null=True)  # Field name made lowercase.
    tradelogref = models.TextField(db_column='tradeLogRef', blank=True, null=True)  # Field name made lowercase.
    testname = models.CharField(db_column='testName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    annualmetrics = models.TextField(db_column='annualMetrics', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trade_results'


class DailyProfits(models.Model):
    id = models.AutoField(primary_key=True)

    trade_result = models.ForeignKey(TradeResults, on_delete=models.CASCADE, db_column='trade_result_id',
                                     related_name='adaily_profits')
    date = models.DateField()
    realizedfunds = models.DecimalField(db_column='realizedFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netliquidity = models.DecimalField(db_column='netLiquidity', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    startingliquidity = models.DecimalField(db_column='startingLiquidity', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    withdrawnfunds = models.DecimalField(db_column='withdrawnFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tradingfunds = models.DecimalField(db_column='tradingFunds', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    profitloss = models.DecimalField(db_column='profitLoss', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    profitlosspercentage = models.DecimalField(db_column='profitLossPercentage', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    drawdownpercentage = models.DecimalField(db_column='drawdownPercentage', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daily_profits'
