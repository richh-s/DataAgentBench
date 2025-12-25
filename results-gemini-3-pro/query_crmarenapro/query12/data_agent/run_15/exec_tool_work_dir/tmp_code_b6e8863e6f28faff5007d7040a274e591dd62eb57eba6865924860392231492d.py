code = """import pandas as pd
import json

opps_path = locals()['var_function-call-12279505214903263167']
contracts_path = locals()['var_function-call-12279505214903260654']

with open(opps_path, 'r') as f:
    opps = json.load(f)
with open(contracts_path, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

def clean_id(x):
    if x is None: return None
    x = str(x).strip()
    if x.lower() == 'none': return None
    if x.startswith('#'): return x[1:]
    return x

df_opp['ContractID_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

# Check lengths
opp_id_lens = df_opp['ContractID_clean'].dropna().apply(len).value_counts().to_dict()
cont_id_lens = df_cont['Id_clean'].dropna().apply(len).value_counts().to_dict()

# Create 15-char ID for joining
def to_15(x):
    if x is None: return None
    if len(x) >= 15:
        return x[:15]
    return x

df_opp['ContractID_15'] = df_opp['ContractID_clean'].apply(to_15)
df_cont['Id_15'] = df_cont['Id_clean'].apply(to_15)

merged = pd.merge(df_opp, df_cont, left_on='ContractID_15', right_on='Id_15', how='inner')

print("__RESULT__:")
print(json.dumps({
    "opp_id_lens": opp_id_lens,
    "cont_id_lens": cont_id_lens,
    "merged_count_15": len(merged)
}))"""

env_args = {'var_function-call-12279505214903263167': 'file_storage/function-call-12279505214903263167.json', 'var_function-call-12279505214903260654': 'file_storage/function-call-12279505214903260654.json', 'var_function-call-17358921919883284085': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'Turnaround': 304.0}], 'var_function-call-14137255585579949854': {'closed_april': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'mean': 304.0, 'count': 1}], 'created_april': [{'OwnerId_clean': '005Wt000003NJgAIAW', 'mean': 49.0, 'count': 1}, {'OwnerId_clean': '005Wt000003NEa3IAG', 'mean': 168.0, 'count': 1}, {'OwnerId_clean': '005Wt000003NISMIA4', 'mean': 186.0, 'count': 1}]}, 'var_function-call-57722329138143834': {'merged_count': 163}}

exec(code, env_args)
