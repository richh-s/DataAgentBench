code = """import json, math
stocks = var_call_Q22zJNoiYf1qXZ8JyTQy2yQG
avg_map = {
  'FTR': var_call_zHgkjOSQQRCyiHqWVnSZjGqt[0]['avg_daily_volume_2008'],
  'SPI': var_call_o8q5mGXeDXsD5YCl0PCgmOj7[0]['avg_daily_volume_2008'],
}
rows=[]
for s in stocks:
    sym=s['Symbol']
    val=avg_map.get(sym)
    avg=None
    if val is not None:
        try:
            f=float(val)
            if not (math.isnan(f) or math.isinf(f)):
                avg=f
        except Exception:
            avg=None
    if avg is not None:
        rows.append({'company_name': s['company_name'], 'symbol': sym, 'financial_status': s['financial_status'], 'avg_daily_volume_2008': avg})
rows=sorted(rows, key=lambda r: r['company_name'])
print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_Q22zJNoiYf1qXZ8JyTQy2yQG': [{'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}], 'var_call_zHgkjOSQQRCyiHqWVnSZjGqt': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_o8q5mGXeDXsD5YCl0PCgmOj7': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
