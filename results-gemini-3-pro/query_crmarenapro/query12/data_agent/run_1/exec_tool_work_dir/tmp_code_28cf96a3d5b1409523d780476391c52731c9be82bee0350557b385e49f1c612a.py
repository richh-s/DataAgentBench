code = """import pandas as pd
import json
import datetime

# Load data
with open(locals()['var_function-call-14699303313641055001'], 'r') as f:
    opp_data = json.load(f)
with open(locals()['var_function-call-14699303313641056710'], 'r') as f:
    contract_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_contract = pd.DataFrame(contract_data)

def clean_id(x):
    if pd.isna(x):
        return None
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_contract['Id'] = df_contract['Id'].apply(clean_id)

df_opp = df_opp.dropna(subset=['ContractID__c'])
df_contract = df_contract.dropna(subset=['Id'])

merged = pd.merge(df_opp, df_contract, left_on='ContractID__c', right_on='Id', how='inner')

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])
merged['CreatedDate_dt'] = merged['CreatedDate'].dt.date
merged['CompanySignedDate_dt'] = merged['CompanySignedDate'].dt.date

# Check logic 1: Signed in April 2023
start_date_dt = datetime.date(2023, 4, 1)
end_date_dt = datetime.date(2023, 4, 30)

filtered_signed = merged[
    (merged['CompanySignedDate_dt'] >= start_date_dt) & 
    (merged['CompanySignedDate_dt'] <= end_date_dt)
].copy()

filtered_signed['Turnaround'] = (filtered_signed['CompanySignedDate_dt'] - filtered_signed['CreatedDate_dt']).apply(lambda x: x.days)

print("Signed in April 2023 Count:", len(filtered_signed))
if len(filtered_signed) > 0:
    grouped_signed = filtered_signed.groupby('OwnerId')['Turnaround'].mean().reset_index().sort_values('Turnaround')
    print("Top signed agents:")
    print(grouped_signed.head(5).to_json(orient='records'))

# Check logic 2: Created in April 2023
filtered_created = merged[
    (merged['CreatedDate_dt'] >= start_date_dt) & 
    (merged['CreatedDate_dt'] <= end_date_dt)
].copy()

filtered_created['Turnaround'] = (filtered_created['CompanySignedDate_dt'] - filtered_created['CreatedDate_dt']).apply(lambda x: x.days)

print("Created in April 2023 Count:", len(filtered_created))
if len(filtered_created) > 0:
    grouped_created = filtered_created.groupby('OwnerId')['Turnaround'].mean().reset_index().sort_values('Turnaround')
    print("Top created agents:")
    print(grouped_created.head(5).to_json(orient='records'))

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-14699303313641055001': 'file_storage/function-call-14699303313641055001.json', 'var_function-call-14699303313641056710': 'file_storage/function-call-14699303313641056710.json', 'var_function-call-11162361170750029499': [{'OwnerId': '005Wt000003NDEBIA4', 'Turnaround': 304.0}]}

exec(code, env_args)
