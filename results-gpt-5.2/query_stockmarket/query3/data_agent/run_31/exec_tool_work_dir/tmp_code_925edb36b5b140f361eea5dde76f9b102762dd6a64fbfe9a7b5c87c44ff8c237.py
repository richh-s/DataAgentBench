code = """import json, math, pandas as pd
stocks = pd.DataFrame(var_call_zd19R9nv8XOs7SRLFc47yPXS)
vol_map = {
  'FTR': var_call_grpEXIX7U1dMfdIhTW0YYPWC[0]['avg_daily_volume_2008'],
  'SPI': var_call_zlKPXmZnKvaJSsjVlIlPpn78[0]['avg_daily_volume_2008'],
}

def to_float(x):
    if x is None:
        return None
    try:
        f = float(x)
        if math.isnan(f):
            return None
        return f
    except Exception:
        return None

stocks['avg_daily_volume_2008'] = stocks['symbol'].map(lambda s: to_float(vol_map.get(s)))
# keep only non-null avg volume (and thus had 2008 trading volume data)
stocks = stocks[stocks['avg_daily_volume_2008'].notna()].copy()
# output minimal requested fields
out = stocks[['company_name','avg_daily_volume_2008']].sort_values('company_name')
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fF260qkrtD4w1VgEAJqOxFkY': ['stockinfo'], 'var_call_zd19R9nv8XOs7SRLFc47yPXS': [{'symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}, {'symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q', 'nasdaq_traded': 'Y'}], 'var_call_fABvB6hbnqblf8ADJRiceUg7': 'file_storage/call_fABvB6hbnqblf8ADJRiceUg7.json', 'var_call_grpEXIX7U1dMfdIhTW0YYPWC': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_zlKPXmZnKvaJSsjVlIlPpn78': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
