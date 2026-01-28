code = """import json, math
info = var_call_XMPifzAEpYhExiqKZT1qkmkY
avg_ftr = var_call_qyuyMU6ShPZpovwJPYy2Malf[0]['avg_daily_volume_2008']
avg_spi = var_call_yFlgQ8yFNtsPuIUlrGMUOnGv[0]['avg_daily_volume_2008']

def to_float(x):
    if x is None:
        return None
    try:
        f = float(x)
        if math.isnan(f) or math.isinf(f):
            return None
        return f
    except Exception:
        return None

avg_map = {'FTR': to_float(avg_ftr), 'SPI': to_float(avg_spi)}
rows = []
for r in info:
    sym = r['symbol']
    avg = avg_map.get(sym)
    if avg is None:
        continue
    rows.append({
        'company_name': r['company_name'],
        'symbol': sym,
        'financial_status': r['financial_status'],
        'avg_daily_volume_2008': avg
    })
rows.sort(key=lambda x: x['company_name'])
print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_UeXZgr1d9OWlXhEO4M3qNGDQ': ['stockinfo'], 'var_call_XMPifzAEpYhExiqKZT1qkmkY': [{'symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'financial_status': 'D'}, {'symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'financial_status': 'D'}], 'var_call_qyuyMU6ShPZpovwJPYy2Malf': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_yFlgQ8yFNtsPuIUlrGMUOnGv': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
