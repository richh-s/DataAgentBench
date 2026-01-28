code = """import json, pandas as pd

accounts = pd.DataFrame(var_call_IK8ynRSn6C1S5nbw0q4bpq32)
acc_set = set(accounts['AccountId_clean'].dropna().astype(str))

# load big orders file
path = var_call_MGOsitnCm05QvtlFZz1HxI8Z
with open(path, 'r') as f:
    orders = json.load(f)

df = pd.DataFrame(orders)
# coerce numeric
for col in ['Quantity','UnitPrice']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# filter to eligible accounts
fdf = df[df['AccountId_clean'].astype(str).isin(acc_set)].copy()
fdf['Sales'] = fdf['Quantity'] * fdf['UnitPrice']
agg = fdf.groupby('AgentId_clean', as_index=False)['Sales'].sum()
agg = agg.sort_values('Sales', ascending=False)
agent_id = None
if len(agg):
    agent_id = agg.iloc[0]['AgentId_clean']

print('__RESULT__:')
print(json.dumps({'AgentId': agent_id}))"""

env_args = {'var_call_MTabjwmTaqLOHfmqxPTV9tmN': 'file_storage/call_MTabjwmTaqLOHfmqxPTV9tmN.json', 'var_call_IK8ynRSn6C1S5nbw0q4bpq32': [{'AccountId_clean': '001Wt00000PGtdJIAT'}, {'AccountId_clean': '001Wt00000PGYx5IAH'}, {'AccountId_clean': '001Wt00000PHVtpIAH'}, {'AccountId_clean': '001Wt00000PHVqdIAH'}, {'AccountId_clean': '001Wt00000PHHXXIA5'}, {'AccountId_clean': '001Wt00000PGZZoIAP'}, {'AccountId_clean': '001Wt00000PGZmfIAH'}, {'AccountId_clean': '001Wt00000PGovMIAT'}, {'AccountId_clean': '001Wt00000PGtdJIAT'}, {'AccountId_clean': '001Wt00000PGRnYIAX'}, {'AccountId_clean': '001Wt00000PGzM9IAL'}, {'AccountId_clean': '001Wt00000PGdzxIAD'}, {'AccountId_clean': '001Wt00000PHRTfIAP'}, {'AccountId_clean': '001Wt00000PFsjOIAT'}, {'AccountId_clean': '001Wt00000PGzSaIAL'}, {'AccountId_clean': '001Wt00000PHVtpIAH'}], 'var_call_MGOsitnCm05QvtlFZz1HxI8Z': 'file_storage/call_MGOsitnCm05QvtlFZz1HxI8Z.json'}

exec(code, env_args)
