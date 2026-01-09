code = """import json, math
info = var_call_OwyeYdnBIVffPUqYnUaq20aq
avg_ftr = float(var_call_TvgOJm5J23lEbD7cLjZY6Nqh[0]['avg_daily_volume_2008'])
spi_raw = var_call_cz88NIbRJmkqGCUb9UM80uRK[0]['avg_daily_volume_2008']
avg_spi = float(spi_raw) if spi_raw is not None else float('nan')

rows = []
for r in info:
    sym = r['Symbol']
    avg = avg_ftr if sym=='FTR' else (avg_spi if sym=='SPI' else None)
    if avg is None or (isinstance(avg, float) and math.isnan(avg)):
        continue
    rows.append({
        'symbol': sym,
        'company_name': r['company_name'],
        'financial_status': r['fin_status'],
        'avg_daily_volume_2008': avg
    })

rows = sorted(rows, key=lambda x: x['company_name'])

out_lines = []
for r in rows:
    out_lines.append(f"{r['company_name']} (Ticker: {r['symbol']}, Financial Status: {r['financial_status']}): Avg daily volume in 2008 = {r['avg_daily_volume_2008']:.2f}")

result = "\n".join(out_lines) if out_lines else "No NASDAQ Global Select Market companies found matching criteria with non-null 2008 trading volume."
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OwyeYdnBIVffPUqYnUaq20aq': [{'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'fin_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'fin_status': 'D', 'market_category': 'Q', 'listing_exchange': 'Q'}], 'var_call_y3zfIC3YNqUbUil9yQiSMR1n': 'file_storage/call_y3zfIC3YNqUbUil9yQiSMR1n.json', 'var_call_TvgOJm5J23lEbD7cLjZY6Nqh': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_cz88NIbRJmkqGCUb9UM80uRK': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
