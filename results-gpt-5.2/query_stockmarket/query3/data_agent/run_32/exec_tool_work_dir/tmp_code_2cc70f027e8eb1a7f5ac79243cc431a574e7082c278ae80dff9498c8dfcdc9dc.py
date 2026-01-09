code = """import json, math
info = var_call_wz9RyOEzHaSQ6HmWGE8BUZm3
avg_ftr = float(var_call_i9MH9ndGDNKKGqsaYDqc17Jk[0]['avg_daily_volume_2008'])
avg_spi_raw = var_call_H9QP8iW9KD7d9o3OjKDUNKLe[0]['avg_daily_volume_2008']
avg_spi = None
try:
    v = float(avg_spi_raw)
    if not math.isnan(v):
        avg_spi = v
except Exception:
    avg_spi = None

rows = []
for r in info:
    sym = r['symbol']
    if sym == 'FTR':
        avg = avg_ftr
    elif sym == 'SPI':
        avg = avg_spi
    else:
        avg = None
    if avg is None:
        continue
    rows.append({
        'company_name': r['company_name'],
        'symbol': sym,
        'financial_status': r['financial_status'],
        'avg_daily_volume_2008': avg
    })

rows_sorted = sorted(rows, key=lambda x: x['company_name'])
print('__RESULT__:')
print(json.dumps(rows_sorted))"""

env_args = {'var_call_wz9RyOEzHaSQ6HmWGE8BUZm3': [{'symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}], 'var_call_i9MH9ndGDNKKGqsaYDqc17Jk': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_H9QP8iW9KD7d9o3OjKDUNKLe': [{'avg_daily_volume_2008': 'nan'}], 'var_call_7JpISXJn2ECfs7yIBeFpRTkY': 'file_storage/call_7JpISXJn2ECfs7yIBeFpRTkY.json'}

exec(code, env_args)
