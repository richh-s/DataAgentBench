code = """import json
import pandas as pd
from datetime import datetime

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

# Clean IDs
def clean_id(x):
    if x is None:
        return None
    return str(x).replace('#', '').strip()

df_opp['clean_contract_id'] = df_opp['ContractID__c'].apply(clean_id)
df_cont['clean_id'] = df_cont['Id'].apply(clean_id)

# Merge
merged = pd.merge(df_opp, df_cont, left_on='clean_contract_id', right_on='clean_id', how='inner')

# Parse dates
merged['created_dt'] = pd.to_datetime(merged['CreatedDate']).dt.date
merged['signed_dt'] = pd.to_datetime(merged['CompanySignedDate']).dt.date

# Filter for April 2023 (Closed)
start_date = pd.to_datetime("2023-04-01").date()
end_date = pd.to_datetime("2023-04-30").date()

april_closed = merged[(merged['signed_dt'] >= start_date) & (merged['signed_dt'] <= end_date)].copy()

if len(april_closed) > 0:
    # Calculate turnaround
    april_closed['turnaround'] = (april_closed['signed_dt'] - april_closed['created_dt']).dt.days
    
    # Clean OwnerId
    april_closed['clean_owner_id'] = april_closed['OwnerId'].apply(clean_id)
    
    # Average turnaround per agent
    agent_perf = april_closed.groupby('clean_owner_id')['turnaround'].mean().reset_index()
    
    # Find minimum
    best_agent = agent_perf.loc[agent_perf['turnaround'].idxmin()]
    
    print("__RESULT__:")
    print(json.dumps(best_agent.to_dict()))
else:
    print("__RESULT__:")
    print(json.dumps({"message": "No deals closed in April 2023"}))"""

env_args = {'var_function-call-12533598710159856220': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-17139697987866028930': [{'Id': '006Wt000007AvVeIAK', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aw3WIAS', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aw3XIAS', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'ContractID__c': 'None'}], 'var_function-call-3495054612801986703': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}], 'var_function-call-10340088287711419845': [{'cnt': '1170'}], 'var_function-call-8713919549684615844': [{'cnt': '163'}], 'var_function-call-575465984193636932': 'file_storage/function-call-575465984193636932.json', 'var_function-call-2853334792006630991': 'file_storage/function-call-2853334792006630991.json'}

exec(code, env_args)
