code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-17714401461857222524'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-11620956773306970585'], 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Clean IDs
def clean_id(x):
    if pd.isna(x): return x
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Filter Contracts for April 2023
# CompanySignedDate is YYYY-MM-DD
df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')
df_cont = df_cont.dropna(subset=['CompanySignedDate'])

start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

df_cont_apr = df_cont[(df_cont['CompanySignedDate'] >= start_date) & (df_cont['CompanySignedDate'] <= end_date)].copy()

print(f"Contracts in April 2023: {len(df_cont_apr)}")

# Join with Opportunity
# Opportunity.ContractID__c = Contract.Id
merged = pd.merge(df_opp, df_cont_apr, left_on='ContractID__c', right_on='Id', how='inner')

print(f"Merged records: {len(merged)}")

# Calculate duration
# CreatedDate has timezone, CompanySignedDate is naive (from date). 
# Convert CreatedDate to naive datetime (or matching timezone) or just date
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')

# Normalize to date for calculation (Sales cycle in days)
# Policy: "number of days between an opportunity's creation date and the company signed date"
# Interpretation: Date(Signed) - Date(Created)
merged['CreatedDate_dt'] = merged['CreatedDate'].dt.date
merged['CompanySignedDate_dt'] = merged['CompanySignedDate'].dt.date

merged['turnaround_days'] = (pd.to_datetime(merged['CompanySignedDate_dt']) - pd.to_datetime(merged['CreatedDate_dt'])).dt.days

# Group by Agent (OwnerId)
# We want average turnaround
grouped = merged.groupby('OwnerId')['turnaround_days'].mean().reset_index()
grouped = grouped.sort_values('turnaround_days')

print("__RESULT__:")
print(grouped.to_json(orient='records'))"""

env_args = {'var_function-call-17714401461857222524': 'file_storage/function-call-17714401461857222524.json', 'var_function-call-17714401461857222285': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-11620956773306970585': 'file_storage/function-call-11620956773306970585.json'}

exec(code, env_args)
