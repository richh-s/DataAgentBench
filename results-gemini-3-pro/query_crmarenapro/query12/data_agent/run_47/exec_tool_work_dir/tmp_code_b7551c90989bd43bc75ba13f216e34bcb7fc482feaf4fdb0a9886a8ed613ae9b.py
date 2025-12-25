code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-7326295110052602931'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-8156187237487434029'], 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Cleaning IDs
def clean_id(x):
    if pd.isna(x): return x
    return str(x).strip().lstrip('#')

df_opp['ContractID__c_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId_clean'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

# Merge
merged = pd.merge(df_opp, df_cont, left_on='ContractID__c_clean', right_on='Id_clean', how='inner', suffixes=('_opp', '_cont'))

# Parse dates
merged['CreatedDate_dt'] = pd.to_datetime(merged['CreatedDate'], errors='coerce').dt.tz_localize(None)
merged['CompanySignedDate_dt'] = pd.to_datetime(merged['CompanySignedDate'], errors='coerce')
merged['CloseDate_dt'] = pd.to_datetime(merged['CloseDate'], errors='coerce')

# Calculate cycle days
merged['CreatedDate_date'] = merged['CreatedDate_dt'].dt.normalize()
merged['CycleDays'] = (merged['CompanySignedDate_dt'] - merged['CreatedDate_date']).dt.days

# Filter candidates
# 1. Signed in April 2023
signed_in_april = merged[
    (merged['CompanySignedDate_dt'].dt.year == 2023) & 
    (merged['CompanySignedDate_dt'].dt.month == 4)
]

# 2. Created in April 2023
created_in_april = merged[
    (merged['CreatedDate_dt'].dt.year == 2023) & 
    (merged['CreatedDate_dt'].dt.month == 4)
]

# 3. Closed in April 2023
closed_in_april = merged[
    (merged['CloseDate_dt'].dt.year == 2023) & 
    (merged['CloseDate_dt'].dt.month == 4)
]

print("__RESULT__:")
print(json.dumps({
    "signed_count": len(signed_in_april),
    "created_count": len(created_in_april),
    "closed_count": len(closed_in_april),
    "signed_data": signed_in_april[['Id_opp', 'OwnerId_clean', 'CycleDays']].to_dict(orient='records'),
    "created_preview": created_in_april[['Id_opp', 'OwnerId_clean', 'CycleDays']].head(5).to_dict(orient='records'),
    "closed_preview": closed_in_april[['Id_opp', 'OwnerId_clean', 'CycleDays']].head(5).to_dict(orient='records')
}))"""

env_args = {'var_function-call-10735388318891818430': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-3575837670014442270': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}], 'var_function-call-11016870797305392549': [{'count_star()': '1'}], 'var_function-call-10400949460133907646': [{'count_star()': '11'}], 'var_function-call-9998197593630935794': [{'CompanySignedDate': '2023-01-12', 'cnt': '1'}, {'CompanySignedDate': '2023-01-23', 'cnt': '1'}, {'CompanySignedDate': '2023-01-26', 'cnt': '2'}, {'CompanySignedDate': '2023-01-28', 'cnt': '1'}, {'CompanySignedDate': '2023-02-25', 'cnt': '1'}, {'CompanySignedDate': '2023-02-26', 'cnt': '2'}, {'CompanySignedDate': '2023-02-28', 'cnt': '2'}, {'CompanySignedDate': '2023-03-12', 'cnt': '1'}, {'CompanySignedDate': '2023-03-15', 'cnt': '1'}, {'CompanySignedDate': '2023-03-16', 'cnt': '1'}, {'CompanySignedDate': '2023-04-15', 'cnt': '1'}, {'CompanySignedDate': '2023-05-12', 'cnt': '1'}, {'CompanySignedDate': '2023-05-16', 'cnt': '1'}, {'CompanySignedDate': '2023-05-30', 'cnt': '1'}, {'CompanySignedDate': '2023-06-13', 'cnt': '1'}, {'CompanySignedDate': '2023-06-21', 'cnt': '2'}, {'CompanySignedDate': '2023-06-22', 'cnt': '1'}, {'CompanySignedDate': '2023-07-02', 'cnt': '1'}, {'CompanySignedDate': '2023-07-12', 'cnt': '1'}, {'CompanySignedDate': '2023-07-19', 'cnt': '1'}, {'CompanySignedDate': '2023-07-25', 'cnt': '1'}, {'CompanySignedDate': '2023-08-23', 'cnt': '2'}, {'CompanySignedDate': '2023-08-24', 'cnt': '1'}, {'CompanySignedDate': '2023-08-29', 'cnt': '2'}, {'CompanySignedDate': '2023-09-13', 'cnt': '1'}, {'CompanySignedDate': '2023-09-15', 'cnt': '1'}, {'CompanySignedDate': '2023-09-25', 'cnt': '1'}, {'CompanySignedDate': '2023-09-30', 'cnt': '1'}, {'CompanySignedDate': '2023-10-06', 'cnt': '2'}, {'CompanySignedDate': '2023-10-13', 'cnt': '2'}, {'CompanySignedDate': '2023-10-15', 'cnt': '1'}, {'CompanySignedDate': '2023-10-16', 'cnt': '1'}, {'CompanySignedDate': '2023-10-18', 'cnt': '1'}, {'CompanySignedDate': '2023-10-20', 'cnt': '1'}, {'CompanySignedDate': '2023-10-31', 'cnt': '1'}, {'CompanySignedDate': '2023-11-11', 'cnt': '1'}, {'CompanySignedDate': '2023-11-23', 'cnt': '1'}, {'CompanySignedDate': '2023-11-26', 'cnt': '1'}, {'CompanySignedDate': '2023-11-27', 'cnt': '1'}, {'CompanySignedDate': '2023-12-06', 'cnt': '1'}, {'CompanySignedDate': '2023-12-20', 'cnt': '1'}, {'CompanySignedDate': '2023-12-21', 'cnt': '1'}], 'var_function-call-10183162482298639328': [{'count_star()': '163'}], 'var_function-call-16813523098198302035': [{'count_star()': '1170'}], 'var_function-call-7326295110052602931': 'file_storage/function-call-7326295110052602931.json', 'var_function-call-8156187237487434029': 'file_storage/function-call-8156187237487434029.json'}

exec(code, env_args)
