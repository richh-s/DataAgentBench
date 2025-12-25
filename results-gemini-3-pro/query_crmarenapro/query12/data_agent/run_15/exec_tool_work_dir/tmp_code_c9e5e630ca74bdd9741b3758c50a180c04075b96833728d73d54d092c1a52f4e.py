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

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

if merged['CreatedDate'].dt.tz is not None:
    merged['CreatedDate'] = merged['CreatedDate'].dt.tz_localize(None)
if merged['CompanySignedDate'].dt.tz is not None:
    merged['CompanySignedDate'] = merged['CompanySignedDate'].dt.tz_localize(None)

# Option 1: Closed in April 2023
start_date_closed = pd.Timestamp('2023-04-01')
end_date_closed = pd.Timestamp('2023-04-30')
closed_april = merged[(merged['CompanySignedDate'] >= start_date_closed) & (merged['CompanySignedDate'] <= end_date_closed)].copy()

# Option 2: Created in April 2023
start_date_created = pd.Timestamp('2023-04-01')
end_date_created = pd.Timestamp('2023-04-30')
created_april = merged[(merged['CreatedDate'] >= start_date_created) & (merged['CreatedDate'] <= end_date_created)].copy()

def calc_stats(df, name):
    if df.empty:
        return []
    df['Turnaround'] = (df['CompanySignedDate'] - df['CreatedDate'].dt.floor('D')).dt.days
    df = df[df['Turnaround'] >= 0]
    agg = df.groupby('OwnerId_clean')['Turnaround'].agg(['mean', 'count']).reset_index().sort_values('mean')
    return agg.head(5).to_dict(orient='records')

res_closed = calc_stats(closed_april, "Closed in April")
res_created = calc_stats(created_april, "Created in April")

print("__RESULT__:")
print(json.dumps({"closed_april": res_closed, "created_april": res_created}))"""

env_args = {'var_function-call-12279505214903263167': 'file_storage/function-call-12279505214903263167.json', 'var_function-call-12279505214903260654': 'file_storage/function-call-12279505214903260654.json', 'var_function-call-17358921919883284085': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'Turnaround': 304.0}]}

exec(code, env_args)
