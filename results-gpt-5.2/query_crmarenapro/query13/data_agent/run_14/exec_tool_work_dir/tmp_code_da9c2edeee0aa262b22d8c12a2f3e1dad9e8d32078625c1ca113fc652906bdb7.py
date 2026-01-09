code = """import json, pandas as pd

# load orders aggregation (may be filepath)
orders_obj = var_call_dMpgzfz4senwKcfLzfHl5h2D
if isinstance(orders_obj, str):
    with open(orders_obj, 'r') as f:
        orders = json.load(f)
else:
    orders = orders_obj

contracts = var_call_y7lejhnUYs9TnWUmCGVJ8uZr

odf = pd.DataFrame(orders)
cdf = pd.DataFrame(contracts)

# filter to eligible accounts
eligible = set(cdf['AccountIdClean'].dropna().astype(str))
odf = odf[odf['AccountIdClean'].astype(str).isin(eligible)].copy()

# clean agent ids
odf['AgentIdClean'] = odf['AgentId'].astype(str).str.replace('#','', regex=False)
# sum across accounts per agent
odf['SalesAmount'] = odf['SalesAmount'].astype(float)
res = odf.groupby('AgentIdClean', as_index=False)['SalesAmount'].sum().sort_values('SalesAmount', ascending=False).head(1)
agent_id = None if res.empty else res.iloc[0]['AgentIdClean']

print('__RESULT__:')
print(json.dumps({'AgentId': agent_id}))"""

env_args = {'var_call_dMpgzfz4senwKcfLzfHl5h2D': 'file_storage/call_dMpgzfz4senwKcfLzfHl5h2D.json', 'var_call_y7lejhnUYs9TnWUmCGVJ8uZr': [{'AccountIdClean': '001Wt00000PHVtpIAH'}, {'AccountIdClean': '001Wt00000PGzM9IAL'}, {'AccountIdClean': '001Wt00000PGdzxIAD'}, {'AccountIdClean': '001Wt00000PGtdJIAT'}, {'AccountIdClean': '001Wt00000PGzSaIAL'}, {'AccountIdClean': '001Wt00000PGovMIAT'}, {'AccountIdClean': '001Wt00000PHHXXIA5'}, {'AccountIdClean': '001Wt00000PGZZoIAP'}, {'AccountIdClean': '001Wt00000PGZmfIAH'}, {'AccountIdClean': '001Wt00000PFsjOIAT'}, {'AccountIdClean': '001Wt00000PHVqdIAH'}, {'AccountIdClean': '001Wt00000PGRnYIAX'}, {'AccountIdClean': '001Wt00000PGYx5IAH'}, {'AccountIdClean': '001Wt00000PHRTfIAP'}]}

exec(code, env_args)
