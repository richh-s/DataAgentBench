code = """import json, math
info = var_call_Npu2C8UjIiuXeDsDncrpsA7f
avg_ftr = var_call_esHRFFbFcuBZutksOAqsUVdn[0]['avg_daily_volume_2008']
avg_spi = var_call_63TeerAyNt5GxBh1hTO410fp[0]['avg_daily_volume_2008']

def to_float(x):
    if x is None:
        return None
    if isinstance(x, (int,float)):
        if isinstance(x,float) and math.isnan(x):
            return None
        return float(x)
    s = str(x).strip()
    if s.lower() in ('nan','null','none',''):
        return None
    try:
        v = float(s)
        if math.isnan(v):
            return None
        return v
    except:
        return None

avg_map = {'FTR': to_float(avg_ftr), 'SPI': to_float(avg_spi)}

rows = []
for r in info:
    sym = r['Symbol']
    avg = avg_map.get(sym)
    if avg is None:
        continue
    rows.append({
        'company_name': r['company_name'],
        'symbol': sym,
        'financial_status': r['financial_status'],
        'avg_daily_volume_2008': avg
    })

# sort by company name
rows = sorted(rows, key=lambda x: x['company_name'])

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_Npu2C8UjIiuXeDsDncrpsA7f': [{'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}], 'var_call_esHRFFbFcuBZutksOAqsUVdn': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_63TeerAyNt5GxBh1hTO410fp': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
