code = """import pandas as pd
import json

opps_path = locals()['var_function-call-12279505214903263167']
contracts_path = locals()['var_function-call-12279505214903260654']

with open(opps_path, 'r') as f:
    opps = json.load(f)
with open(contracts_path, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

def clean_id(x):
    if x is None: return None
    x = str(x).strip()
    if x.lower() == 'none': return None
    if x.startswith('#'): return x[1:]
    return x

df_opp['ContractID_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId_clean'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

merged = pd.merge(df_opp, df_cont, left_on='ContractID_clean', right_on='Id_clean', how='inner')

# Dates
# 'CreatedDate' e.g. "2023-09-05T11:32:46.000+0000" (mixed format in JSON?)
# 'CompanySignedDate' e.g. "2021-07-16"

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# Make CreatedDate naive
if merged['CreatedDate'].dt.tz is not None:
    merged['CreatedDate'] = merged['CreatedDate'].dt.tz_localize(None)

# Make CompanySignedDate naive (it probably is)
if merged['CompanySignedDate'].dt.tz is not None:
    merged['CompanySignedDate'] = merged['CompanySignedDate'].dt.tz_localize(None)

start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

april_deals = merged[(merged['CompanySignedDate'] >= start_date) & (merged['CompanySignedDate'] <= end_date)].copy()

if april_deals.empty:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    april_deals['Turnaround'] = (april_deals['CompanySignedDate'] - april_deals['CreatedDate'].dt.floor('D')).dt.days
    april_deals = april_deals[april_deals['Turnaround'] >= 0]
    agg = april_deals.groupby('OwnerId_clean')['Turnaround'].mean().reset_index()
    agg = agg.sort_values('Turnaround')
    print("__RESULT__:")
    print(agg.head(1).to_json(orient='records'))"""

env_args = {'var_function-call-12279505214903263167': 'file_storage/function-call-12279505214903263167.json', 'var_function-call-12279505214903260654': 'file_storage/function-call-12279505214903260654.json'}

exec(code, env_args)
