code = """import pandas as pd
import json

# Load data
with open('var_function-call-12279505214903263167', 'r') as f:
    opps = json.load(f)
with open('var_function-call-12279505214903260654', 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Clean IDs
def clean_id(x):
    if x is None: return None
    x = str(x).strip()
    if x.lower() == 'none': return None
    if x.startswith('#'): return x[1:]
    return x

df_opp['ContractID_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId_clean'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

# Merge
merged = pd.merge(df_opp, df_cont, left_on='ContractID_clean', right_on='Id_clean', how='inner')

# Dates
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# Filter Closing Date in April 2023
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

# Filter
april_deals = merged[(merged['CompanySignedDate'] >= start_date) & (merged['CompanySignedDate'] <= end_date)].copy()

if april_deals.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No deals closed in April 2023"}))
else:
    # Calculate Turnaround (Days)
    # Using difference in calendar dates
    april_deals['Turnaround'] = (april_deals['CompanySignedDate'] - april_deals['CreatedDate'].dt.floor('D')).dt.days
    
    # Filter valid turnaround
    april_deals = april_deals[april_deals['Turnaround'] >= 0]
    
    # Group
    agg = april_deals.groupby('OwnerId_clean')['Turnaround'].mean().reset_index()
    agg = agg.sort_values('Turnaround')
    
    # Get top 1
    top_agent = agg.head(1)
    
    print("__RESULT__:")
    print(top_agent.to_json(orient='records'))"""

env_args = {'var_function-call-12279505214903263167': 'file_storage/function-call-12279505214903263167.json', 'var_function-call-12279505214903260654': 'file_storage/function-call-12279505214903260654.json'}

exec(code, env_args)
