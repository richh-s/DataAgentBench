code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-7507401632398632819'], 'r') as f:
    opp_data = json.load(f)
with open(locals()['var_function-call-7507401632398634894'], 'r') as f:
    cont_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_cont = pd.DataFrame(cont_data)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Dates
# Contract Signed Date
df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')

# Filter Contracts for April 2023
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')
df_cont_april = df_cont[(df_cont['CompanySignedDate'] >= start_date) & (df_cont['CompanySignedDate'] <= end_date)].copy()

# Opportunity Created Date
df_opp['CreatedDate'] = pd.to_datetime(df_opp['CreatedDate'], errors='coerce')

# Merge
# Left is Opp, Right is Cont
merged = pd.merge(df_opp, df_cont_april, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate turnaround
# Days between Creation and Signed
# Use .dt.date to compare just dates
if not merged.empty:
    merged['TurnaroundDays'] = (merged['CompanySignedDate'].dt.date - merged['CreatedDate'].dt.date).apply(lambda x: x.days)

    # Filter out negative days if any
    merged = merged[merged['TurnaroundDays'] >= 0]

    # Group by OwnerId and calc average
    result = merged.groupby('OwnerId')['TurnaroundDays'].mean().reset_index()
    result = result.sort_values(by='TurnaroundDays', ascending=True)

    # Get top
    top_agent = result.iloc[0]['OwnerId'] if not result.empty else "None"
else:
    top_agent = "None"

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-7507401632398632819': 'file_storage/function-call-7507401632398632819.json', 'var_function-call-7507401632398634894': 'file_storage/function-call-7507401632398634894.json'}

exec(code, env_args)
