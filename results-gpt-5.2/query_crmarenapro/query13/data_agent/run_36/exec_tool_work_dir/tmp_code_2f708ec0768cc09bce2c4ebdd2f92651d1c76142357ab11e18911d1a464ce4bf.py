code = """import json, pandas as pd
from pathlib import Path

# load big orders aggregation
p = Path(var_call_VvOBiygToYsemUmpWxlIFH0o)
orders = json.loads(p.read_text())
contracts = var_call_jB3FbfraF8qWPnXA2RP7biLs

df_o = pd.DataFrame(orders)
df_c = pd.DataFrame(contracts)

# ensure numeric
if not df_o.empty:
    df_o['SalesAmount'] = pd.to_numeric(df_o['SalesAmount'])

# filter to eligible accounts
eligible = set(df_c['AccountId_norm'].tolist())
df_f = df_o[df_o['AccountId_norm'].isin(eligible)].copy()

# sum by agent
res = (df_f.groupby('AgentId_norm', as_index=False)['SalesAmount'].sum()
         .sort_values(['SalesAmount','AgentId_norm'], ascending=[False, True])
         .head(1))
agent_id = None
if not res.empty:
    agent_id = res.iloc[0]['AgentId_norm']

print('__RESULT__:')
print(json.dumps(agent_id))"""

env_args = {'var_call_VvOBiygToYsemUmpWxlIFH0o': 'file_storage/call_VvOBiygToYsemUmpWxlIFH0o.json', 'var_call_jB3FbfraF8qWPnXA2RP7biLs': [{'AccountId_norm': '001Wt00000PHVtpIAH'}, {'AccountId_norm': '001Wt00000PGzM9IAL'}, {'AccountId_norm': '001Wt00000PGdzxIAD'}, {'AccountId_norm': '001Wt00000PGtdJIAT'}, {'AccountId_norm': '001Wt00000PGzSaIAL'}, {'AccountId_norm': '001Wt00000PGovMIAT'}, {'AccountId_norm': '001Wt00000PHRTfIAP'}, {'AccountId_norm': '001Wt00000PGYx5IAH'}, {'AccountId_norm': '001Wt00000PGRnYIAX'}, {'AccountId_norm': '001Wt00000PHVqdIAH'}, {'AccountId_norm': '001Wt00000PHHXXIA5'}, {'AccountId_norm': '001Wt00000PGZZoIAP'}, {'AccountId_norm': '001Wt00000PGZmfIAH'}, {'AccountId_norm': '001Wt00000PFsjOIAT'}]}

exec(code, env_args)
