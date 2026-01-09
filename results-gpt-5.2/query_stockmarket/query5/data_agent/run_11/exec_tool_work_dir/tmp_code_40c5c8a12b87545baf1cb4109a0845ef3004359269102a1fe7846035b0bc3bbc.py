code = """import json, pandas as pd

path = var_call_hSnm5hkMQxk7jSRLKxP3Bsak
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# filter to common stocks only: exclude symbols with special share classes/warrants/units/rights, keep A-Z only (and dot?)
# Here keep tickers that are purely letters (common) to avoid U/W/R/P etc.
df['is_common_like'] = df['Symbol'].str.fullmatch(r'[A-Z]{1,5}')
df2 = df[df['is_common_like']].copy()
res = {
    'symbols': df2['Symbol'].tolist(),
    'company_map': dict(zip(df2['Symbol'], df2['company_name'])),
    'n_symbols': int(df2.shape[0]),
    'n_all': int(df.shape[0])
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_hSnm5hkMQxk7jSRLKxP3Bsak': 'file_storage/call_hSnm5hkMQxk7jSRLKxP3Bsak.json'}

exec(code, env_args)
