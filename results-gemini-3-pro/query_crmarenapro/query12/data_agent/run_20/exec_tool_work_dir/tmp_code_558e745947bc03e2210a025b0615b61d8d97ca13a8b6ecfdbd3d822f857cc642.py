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

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
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

contract_ids_april = set(contracts_april['Id'])
opp_contract_ids = set(df_opp_with_contract['ContractID__c'])
overlap = contract_ids_april.intersection(opp_contract_ids)

debug_info = {
    "num_contracts_april": len(contracts_april),
    "sample_contracts_april": contracts_april['Id'].head().tolist(),
    "num_overlap": len(overlap),
    "overlap_ids": list(overlap)
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16291847767838896705': 'file_storage/function-call-16291847767838896705.json', 'var_function-call-16291847767838900130': 'file_storage/function-call-16291847767838900130.json', 'var_function-call-4770270048180893903': [{'OwnerId': '005Wt000003NDEBIA4', 'Duration': 304.0}], 'var_function-call-388246814529086496': [{'OwnerId': '005Wt000003NDEBIA4', 'Duration': 304.0}]}

exec(code, env_args)
