code = """import json, pandas as pd, math

info = pd.DataFrame(var_call_AfS7OzAkOzjE8Zv9N2Jlz0vG)

avg_ftr = float(var_call_TFKpCIlGuGDXqJZGuUxtvq3p[0]['avg_volume_2008'])
spi_raw = var_call_sS4dw4UneMK0kUUN9UaW0yNx[0]['avg_volume_2008']
try:
    avg_spi = float(spi_raw)
except Exception:
    avg_spi = float('nan')

rows = []
for _, r in info.iterrows():
    sym = r['Symbol']
    avg = avg_ftr if sym=='FTR' else avg_spi if sym=='SPI' else float('nan')
    if avg is None or (isinstance(avg, float) and (math.isnan(avg))):
        continue
    rows.append({
        'company_name': r['company_name'],
        'symbol': sym,
        'financial_status': r['financial_status'],
        'avg_daily_volume_2008': avg
    })

out = pd.DataFrame(rows).sort_values(['company_name','symbol']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AfS7OzAkOzjE8Zv9N2Jlz0vG': [{'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'financial_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}], 'var_call_Xam4Hn62kWFAz36qy7KJWImg': 'file_storage/call_Xam4Hn62kWFAz36qy7KJWImg.json', 'var_call_obppEB9xiBrgU6DtrkLOmUCg': {'symbols': ['FTR', 'SPI'], 'existing_in_trade_db': ['FTR', 'SPI']}, 'var_call_TFKpCIlGuGDXqJZGuUxtvq3p': [{'avg_volume_2008': '254397.62845849802'}], 'var_call_sS4dw4UneMK0kUUN9UaW0yNx': [{'avg_volume_2008': 'nan'}]}

exec(code, env_args)
