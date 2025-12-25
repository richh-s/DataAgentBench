code = """import json
import pandas as pd

# Load Opportunity data
with open(locals()['var_function-call-16291847767838896705'], 'r') as f:
    opp_data = json.load(f)

# Load Contract data
with open(locals()['var_function-call-16291847767838900130'], 'r') as f:
    contract_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_cont = pd.DataFrame(contract_data)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_opp['Id'] = df_opp['Id'].apply(clean_id)
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Filter valid contracts in opp
df_opp_with_contract = df_opp[df_opp['ContractID__c'] != 'None']

# Contracts in April 2023
df_cont['CompanySignedDate_dt'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

contracts_april = df_cont[
    (df_cont['CompanySignedDate_dt'] >= start_date) & 
    (df_cont['CompanySignedDate_dt'] <= end_date)
]

# Merge
df_merged = pd.merge(df_opp_with_contract, contracts_april, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate duration
df_merged['CreatedDate_dt'] = pd.to_datetime(df_merged['CreatedDate']).dt.tz_localize(None)
df_merged['Duration'] = (df_merged['CompanySignedDate_dt'] - df_merged['CreatedDate_dt'].dt.normalize()).dt.days

record = df_merged.iloc[0].to_dict()
# Convert timestamps to str for json
record['CreatedDate_dt'] = str(record['CreatedDate_dt'])
record['CompanySignedDate_dt'] = str(record['CompanySignedDate_dt'])

print("__RESULT__:")
print(json.dumps([record]))"""

env_args = {'var_function-call-16291847767838896705': 'file_storage/function-call-16291847767838896705.json', 'var_function-call-16291847767838900130': 'file_storage/function-call-16291847767838900130.json', 'var_function-call-4770270048180893903': [{'OwnerId': '005Wt000003NDEBIA4', 'Duration': 304.0}], 'var_function-call-388246814529086496': [{'OwnerId': '005Wt000003NDEBIA4', 'Duration': 304.0}], 'var_function-call-2620617327423793432': {'num_contracts_april': 1, 'sample_contracts_april': ['800Wt00000DE9FGIA1'], 'num_overlap': 1, 'overlap_ids': ['800Wt00000DE9FGIA1']}}

exec(code, env_args)
