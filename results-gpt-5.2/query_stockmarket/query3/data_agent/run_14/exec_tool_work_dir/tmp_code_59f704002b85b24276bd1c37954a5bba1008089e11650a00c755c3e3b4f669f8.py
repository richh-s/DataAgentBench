code = """import json, math, pandas as pd
info = pd.DataFrame(var_call_m4KKQ5IzNpnlYYFw9VifPDcG)
vol_ftr = var_call_bvhOGQZBAebM1i3VyvhcBsVA[0]['avg_daily_volume_2008']
vol_spi = var_call_AwQgr0DXvOsRxUuckINxe05f[0]['avg_daily_volume_2008']
vol_map = {'FTR': vol_ftr, 'SPI': vol_spi}
rows = []
for _, r in info.iterrows():
    sym = r['Symbol']
    v = vol_map.get(sym)
    # convert to float and keep only non-null, non-nan
    try:
        vf = float(v) if v is not None else None
    except Exception:
        vf = None
    if vf is None or math.isnan(vf):
        continue
    rows.append({
        'company_name': r['company_name'],
        'symbol': sym,
        'financial_status': r['financial_status'],
        'avg_daily_volume_2008': vf
    })
rows = sorted(rows, key=lambda x: x['company_name'])
print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_m4KKQ5IzNpnlYYFw9VifPDcG': [{'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'financial_status': 'D'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'financial_status': 'D'}], 'var_call_bvhOGQZBAebM1i3VyvhcBsVA': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_AwQgr0DXvOsRxUuckINxe05f': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
