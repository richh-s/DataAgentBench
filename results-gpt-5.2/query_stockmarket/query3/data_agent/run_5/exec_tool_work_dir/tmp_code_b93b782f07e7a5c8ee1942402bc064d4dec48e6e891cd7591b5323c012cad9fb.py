code = """import json, math
info = var_call_zCVVSYQg8ilGrmO7ItMCJFwj
avg_ftr = float(var_call_RfLxeWx1Uzswn2wG8JHYJ5hf[0]['avg_daily_volume_2008'])
avg_spi_raw = var_call_7CTgFK0wBPPuteQJ1rScyUhy[0]['avg_daily_volume_2008']
avg_spi = None
try:
    v = float(avg_spi_raw) if avg_spi_raw is not None else float('nan')
    if not math.isnan(v):
        avg_spi = v
except Exception:
    avg_spi = None

out = []
for r in info:
    sym = r['Symbol']
    if sym == 'FTR':
        avg = avg_ftr
    elif sym == 'SPI':
        avg = avg_spi
    else:
        avg = None
    if avg is not None:
        out.append({'company_name': r['company_name'], 'symbol': sym, 'avg_daily_volume_2008': avg})

out.sort(key=lambda x: x['company_name'])
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zCVVSYQg8ilGrmO7ItMCJFwj': [{'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'financial_status': 'D'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'financial_status': 'D'}], 'var_call_RfLxeWx1Uzswn2wG8JHYJ5hf': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_7CTgFK0wBPPuteQJ1rScyUhy': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
