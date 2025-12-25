code = """import pandas as pd
import json

path_opp = locals()['var_function-call-8541669410738994321']
path_cont = locals()['var_function-call-8541669410738991182']

with open(path_opp, 'r') as f:
    opps = json.load(f)
with open(path_cont, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

df_opp['ContractID__c_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')
df_cont_april = df_cont[
    (df_cont['CompanySignedDate'] >= '2023-04-01') & 
    (df_cont['CompanySignedDate'] <= '2023-04-30')
]

merged = pd.merge(df_opp, df_cont_april, left_on='ContractID__c_clean', right_on='Id_clean', how='inner')

print("__RESULT__:")
print(json.dumps({
    "opp_count": len(df_opp),
    "cont_count": len(df_cont),
    "cont_april_count": len(df_cont_april),
    "merged_count": len(merged),
    "sample_merged_Ids": merged[['ContractID__c_clean', 'Id_clean']].head(5).values.tolist()
}))"""

env_args = {'var_function-call-7295838422035824403': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-8541669410738994321': 'file_storage/function-call-8541669410738994321.json', 'var_function-call-8541669410738991182': 'file_storage/function-call-8541669410738991182.json', 'var_function-call-6173624232980906063': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'cycle_days': 303.5690972222}], 'var_function-call-18243377451092367769': {'top_agent': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'cycle_days': 303.56909722222224}], 'num_agents': 1, 'all_agents_head': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'cycle_days': 303.56909722222224}]}}

exec(code, env_args)
