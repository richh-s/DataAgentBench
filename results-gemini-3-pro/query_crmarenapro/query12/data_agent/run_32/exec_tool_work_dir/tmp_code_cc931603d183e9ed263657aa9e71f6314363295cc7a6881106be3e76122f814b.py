code = """import json
import pandas as pd

# Get file paths from variables
opp_file = locals()['var_function-call-575465984193636932']
cont_file = locals()['var_function-call-2853334792006630991']

# Load data
with open(opp_file, 'r') as f:
    opps = json.load(f)
with open(cont_file, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

def clean_id(x):
    if x is None:
        return None
    return str(x).replace('#', '').strip()

df_opp['clean_contract_id'] = df_opp['ContractID__c'].apply(clean_id)
df_cont['clean_id'] = df_cont['Id'].apply(clean_id)
df_opp['clean_owner_id'] = df_opp['OwnerId'].apply(clean_id)

merged = pd.merge(df_opp, df_cont, left_on='clean_contract_id', right_on='clean_id', how='inner')

merged['created_dt_full'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')
merged['signed_dt_full'] = pd.to_datetime(merged['CompanySignedDate'], errors='coerce')
merged = merged.dropna(subset=['created_dt_full', 'signed_dt_full'])
merged['created_dt'] = merged['created_dt_full'].dt.date
merged['signed_dt'] = merged['signed_dt_full'].dt.date
merged['turnaround'] = (merged['signed_dt'] - merged['created_dt']).apply(lambda x: x.days)

# Filter 1: Closed in April 2023
start_apr = pd.to_datetime("2023-04-01").date()
end_apr = pd.to_datetime("2023-04-30").date()

closed_apr = merged[(merged['signed_dt'] >= start_apr) & (merged['signed_dt'] <= end_apr)].copy()
print(f"Deals Closed in April 2023: {len(closed_apr)}")

if len(closed_apr) > 0:
    agent_perf_closed = closed_apr.groupby('clean_owner_id')['turnaround'].mean().sort_values().reset_index()
    print("Top agents (Closed in April):")
    print(agent_perf_closed.head(3).to_dict(orient='records'))

# Filter 2: Created in April 2023
created_apr = merged[(merged['created_dt'] >= start_apr) & (merged['created_dt'] <= end_apr)].copy()
print(f"Deals Created in April 2023 (and closed ever): {len(created_apr)}")

if len(created_apr) > 0:
    agent_perf_created = created_apr.groupby('clean_owner_id')['turnaround'].mean().sort_values().reset_index()
    print("Top agents (Created in April):")
    print(agent_perf_created.head(3).to_dict(orient='records'))

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-12533598710159856220': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-17139697987866028930': [{'Id': '006Wt000007AvVeIAK', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aw3WIAS', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aw3XIAS', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'ContractID__c': 'None'}], 'var_function-call-3495054612801986703': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}], 'var_function-call-10340088287711419845': [{'cnt': '1170'}], 'var_function-call-8713919549684615844': [{'cnt': '163'}], 'var_function-call-575465984193636932': 'file_storage/function-call-575465984193636932.json', 'var_function-call-2853334792006630991': 'file_storage/function-call-2853334792006630991.json', 'var_function-call-5986160764774259954': {'clean_owner_id': '005Wt000003NDEBIA4', 'turnaround': 304.0}}

exec(code, env_args)
