from django.db import models

class StockInfo(models.Model):
    pair_ID = models.IntegerField(primary_key=True)
    stock_symbol = models.CharField(max_length=10)
    parent_pair_ID = models.BooleanField()
    canonical_to_pair_id = models.BooleanField()
    override_country_ID = models.BooleanField()
    eq_pe_ratio = models.FloatField(null=True)
    eq_market_cap = models.IntegerField(null=True)
    eq_one_year_return = models.FloatField(null=True)
    eq_dividend = models.IntegerField(null=True)
    eq_eps = models.FloatField(null=True)
    eq_beta = models.FloatField(null=True)
    eq_revenue = models.IntegerField(null=True)
    exchange_ID = models.IntegerField()
    security_type = models.CharField(max_length=10)
    a1fcf = models.FloatField(null=True)
    aastturn = models.FloatField(null=True)
    abepsxclxo = models.FloatField(null=True)
    abvps = models.FloatField(null=True)
    acfshr = models.FloatField(null=True)
    acshps = models.FloatField(null=True)
    acurratio = models.FloatField(null=True)
    adiv5yavg = models.FloatField(null=True)
    aebitd = models.FloatField(null=True)
    aebt = models.FloatField(null=True)
    aebtnorm = models.FloatField(null=True)
    aepsinclxo = models.FloatField(null=True)
    aepsxclxor = models.FloatField(null=True)
    agrosmgn = models.FloatField(null=True)
    ainvturn = models.FloatField(null=True)
    altd2eq = models.FloatField(null=True)
    aniac = models.FloatField(null=True)
    aniacnorm = models.FloatField(null=True)
    anpmgnpct = models.FloatField(null=True)
    aopmgnpct = models.FloatField(null=True)
    apayratio = models.FloatField(null=True)
    apeexclxor = models.FloatField(null=True)
    apenorm = models.FloatField(null=True)
    apr2rev = models.FloatField(null=True)
    apr2tanbk = models.FloatField(null=True)
    aprfcfps = models.FloatField(null=True)
    aprice2bk = models.FloatField(null=True)
    aptmgnpct = models.FloatField(null=True)
    aquickrati = models.FloatField(null=True)
    arecturn = models.FloatField(null=True)
    arevps = models.FloatField(null=True)
    aroa5yavg = models.FloatField(null=True)
    aroapct = models.FloatField(null=True)
    aroe5yavg = models.FloatField(null=True)
    aroepct = models.FloatField(null=True)
    aroi5yravg = models.FloatField(null=True)
    aroipct = models.FloatField(null=True)
    atanbvps = models.FloatField(null=True)
    atotd2eq = models.FloatField(null=True)
    beta = models.FloatField(null=True)
    bvtrendgr = models.FloatField(null=True)
    csptrendgr = models.FloatField(null=True)
    divgrpct = models.FloatField(null=True)
    divyield_curttm = models.FloatField(null=True)
    ebitda_ayr5cagr = models.FloatField(null=True)
    ebitda_ttmy5cagr = models.FloatField(null=True)
    epschngyr = models.FloatField(null=True)
    epsgrpct = models.FloatField(null=True)
    epstrendgr = models.FloatField(null=True)
    ev2fcf_cura = models.FloatField(null=True)
    ev2fcf_curttm = models.FloatField(null=True)
    focf2rev_aavg5 = models.FloatField(null=True)
    focf2rev_ttm = models.FloatField(null=True)
    focf_ayr5cagr = models.FloatField(null=True)
    grosmgn5yr = models.FloatField(null=True)
    margin5yr = models.FloatField(null=True)
    mktcap = models.FloatField(null=True)
    netdebt_a = models.FloatField(null=True)
    netdebt_i = models.FloatField(null=True)
    npmtrendgr = models.FloatField(null=True)
    opmgn5yr = models.FloatField(null=True)
    pebexclxor = models.FloatField(null=True)
    peexclxor = models.FloatField(null=True)
    peinclxor = models.FloatField(null=True)
    pr2tanbk = models.FloatField(null=True)
    price2bk = models.FloatField(null=True)
    projepsq = models.FloatField(null=True)
    ptmgn5yr = models.FloatField(null=True)
    qbvps = models.FloatField(null=True)
    qcshps = models.FloatField(null=True)
    qcurratio = models.FloatField(null=True)
    qltd2eq = models.FloatField(null=True)
    qquickrati = models.FloatField(null=True)
    qtanbvps = models.FloatField(null=True)
    qtotd2eq = models.FloatField(null=True)
    revchngyr = models.FloatField(null=True)
    revgrpct = models.FloatField(null=True)
    revps5ygr = models.FloatField(null=True)
    revtrendgr = models.FloatField(null=True)
    sharesout = models.FloatField(null=True)
    stld_ayr5cagr = models.FloatField(null=True)
    tanbv_ayr5cagr = models.FloatField(null=True)
    ttmastturn = models.FloatField(null=True)
    ttmbepsxcl = models.FloatField(null=True)
    ttmcfshr = models.FloatField(null=True)
    ttmebitd = models.FloatField(null=True)
    ttmebitdps = models.FloatField(null=True)
    ttmebt = models.FloatField(null=True)
    ttmepschg = models.FloatField(null=True)
    ttmepsincx = models.FloatField(null=True)
    ttmepsxclx = models.FloatField(null=True)
    ttmfcf = models.FloatField(null=True)
    ttmfcfshr = models.FloatField(null=True)
    ttmgrosmgn = models.FloatField(null=True)
    ttminvturn = models.FloatField(null=True)
    ttmniac = models.FloatField(null=True)
    ttmnpmgn = models.FloatField(null=True)
    ttmopmgn = models.FloatField(null=True)
    ttmpayrat = models.FloatField(null=True)
    ttmpehigh = models.FloatField(null=True)
    ttmpelow = models.FloatField(null=True)
    ttmpr2rev = models.FloatField(null=True)
    ttmprcfps = models.FloatField(null=True)
    ttmprfcfps = models.FloatField(null=True)
    ttmptmgn = models.FloatField(null=True)
    ttmrecturn = models.FloatField(null=True)
    ttmrevchg = models.FloatField(null=True)
    ttmrevps = models.FloatField(null=True)
    ttmroapct = models.FloatField(null=True)
    ttmroepct = models.FloatField(null=True)
    ttmroipct = models.FloatField(null=True)
    vdes_ttm = models.FloatField(null=True)
    yld = models.FloatField(null=True) # check
    yld5yavg = models.FloatField(null=True)
    RSI = models.FloatField(null=True)
    STOCH = models.FloatField(null=True)
    CCI = models.FloatField(null=True)
    MACD = models.FloatField(null=True)
    ADX = models.FloatField(null=True)
    WilliamsR = models.FloatField(null=True)
    STOCHRSI = models.FloatField(null=True)
    ATR = models.FloatField(null=True)
    HL = models.FloatField(null=True)
    UO = models.FloatField(null=True)
    ROC = models.FloatField(null=True)
    BullBear = models.FloatField(null=True)
    tech_sum_300 = models.CharField(max_length=12, null=True)
    tech_sum_300_Define = models.CharField(max_length=25, null=True)
    tech_sum_300_Define_order_priority = models.IntegerField(null=True)
    tech_sum_300_Color = models.CharField(max_length=6, null=True)
    tech_sum_900 = models.CharField(max_length=12, null=True)
    tech_sum_900_Define = models.CharField(max_length=25 , null=True)
    tech_sum_900_Define_order_priority = models.IntegerField(null=True)
    tech_sum_900_Color = models.CharField(max_length=6, null=True)
    tech_sum_1800 = models.CharField(max_length=12, null=True)
    tech_sum_1800_Define = models.CharField(max_length=25, null=True)
    tech_sum_1800_Define_order_priority = models.FloatField(null=True)
    tech_sum_1800_Color = models.CharField(max_length=6, null=True)
    tech_sum_3600 = models.CharField(max_length=12, null=True)
    tech_sum_3600_Define = models.CharField(max_length=25, null=True)
    tech_sum_3600_Define_order_priority = models.FloatField(null=True)
    tech_sum_3600_Color = models.CharField(max_length=6, null=True)
    tech_sum_18000 = models.CharField(max_length=12, null=True)
    tech_sum_18000_Define = models.CharField(max_length=25, null=True)
    tech_sum_18000_Define_order_priority = models.FloatField(null=True)
    tech_sum_18000_Color = models.CharField(max_length=6, null=True)
    tech_sum_86400 = models.CharField(max_length=12, null=True)
    tech_sum_86400_Define = models.CharField(max_length=25, null=True)
    tech_sum_86400_Define_order_priority = models.FloatField(null=True)
    tech_sum_86400_Color = models.CharField(max_length=6, null=True)
    tech_sum_week = models.CharField(max_length=12, null=True)
    tech_sum_week_Define = models.CharField(max_length=25, null=True)
    tech_sum_week_Define_order_priority = models.FloatField(null=True)
    tech_sum_week_Color = models.CharField(max_length=6, null=True)
    tech_sum_month = models.CharField(max_length=12, null=True)
    tech_sum_month_Define = models.CharField(max_length=25, null=True)
    tech_sum_month_Define_order_priority = models.FloatField(null=True)
    tech_sum_month_Color = models.CharField(max_length=6, null=True)
    month_change = models.FloatField(null=True)
    ytd = models.FloatField(null=True)
    week = models.FloatField(null=True)
    month = models.FloatField(null=True)
    year = models.FloatField(null=True)
    year3 = models.FloatField(null=True) # check
    sector_id = models.IntegerField(null=True)
    industry_id = models.IntegerField(null=True)
    avg_volume = models.IntegerField()
    pair_change_percent = models.FloatField()
    a52_week_high = models.IntegerField()
    a52_week_low = models.IntegerField()
    turnover_volume = models.IntegerField()
    last = models.IntegerField()
    a52_week_high_diff = models.FloatField()
    a52_week_low_diff = models.FloatField()
    exchange_trans = models.CharField(max_length=10)
    name_trans = models.CharField(max_length=50)
    sector_trans = models.CharField(max_length=20, null=True)
    industry_trans = models.CharField(max_length=30, null=True)
    viewData = models.CharField(max_length=200)
    tech_sum_300_constant = models.CharField(max_length=6, null=True)
    tech_sum_900_constant = models.CharField(max_length=6, null=True)
    tech_sum_1800_constant = models.CharField(max_length=6, null=True)
    tech_sum_3600_constant = models.CharField(max_length=6, null=True)
    tech_sum_18000_constant = models.CharField(max_length=6, null=True)
    tech_sum_86400_constant = models.CharField(max_length=6, null=True)
    tech_sum_week_constant = models.CharField(max_length=6, null=True)
    tech_sum_month_constant = models.CharField(max_length=6, null=True)
    daily = models.FloatField()
    current_assets = models.FloatField(null=True)
    assets = models.IntegerField(null=True)
    current_liabilities = models.IntegerField(null=True)
    liabilities = models.IntegerField(null=True)
    capital = models.IntegerField(null=True)
    aintcov = models.FloatField(null=True)
    ttmintcov = models.FloatField(null=True)
    aniperemp = models.IntegerField(null=True)
    arevperemp = models.IntegerField(null=True)
    ttmniperem = models.IntegerField(null=True)
    ttmrevpere = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name_trans