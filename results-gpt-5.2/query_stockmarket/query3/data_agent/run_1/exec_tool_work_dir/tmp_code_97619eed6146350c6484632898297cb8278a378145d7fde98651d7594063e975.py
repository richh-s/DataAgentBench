code = """import json, math, pandas as pd
stocks = pd.DataFrame(var_call_bWjHzqN8DdCFKqsYLhkOuJ48)
vols = {
    'FTR': var_call_H6eYFA5RvjmbQVtR1fKtUMoy[0]['avg_daily_volume_2008'],
    'SPI': var_call_jjAkwVBfTvySHVxQXZ2Cy8xr[0]['avg_daily_volume_2008'],
}
rows=[]
for _, r in stocks.iterrows():
    sym = r['symbol']
    v = vols.get(sym)
    v_float = None
    if v is None:
        v_float = None
    else:
        try:
            v_float = float(v)
            if math.isnan(v_float):
                v_float = None
        except Exception:
            v_float = None
    if v_float is not None:
        rows.append({
            'company_name': r['company_name'],
            'symbol': sym,
            'financial_status': r['financial_status'],
            'avg_daily_volume_2008': v_float
        })
out = pd.DataFrame(rows)
if not out.empty:
    out = out.sort_values(['company_name','symbol'])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bWjHzqN8DdCFKqsYLhkOuJ48': [{'symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'financial_status': 'D'}, {'symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'financial_status': 'D'}], 'var_call_pBaZbmrhwxNC7VKS4NaE6mtc': 'file_storage/call_pBaZbmrhwxNC7VKS4NaE6mtc.json', 'var_call_H6eYFA5RvjmbQVtR1fKtUMoy': [{'avg_daily_volume_2008': '254397.62845849802'}], 'var_call_jjAkwVBfTvySHVxQXZ2Cy8xr': [{'avg_daily_volume_2008': 'nan'}]}

exec(code, env_args)
