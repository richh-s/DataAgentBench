code = """import pandas as pd
import json

best_cpc_groups_data_str = locals()['var_function-call-17238172386859849011']
best_cpc_df = pd.DataFrame(json.loads(best_cpc_groups_data_str))

cpc_definitions_data_path = locals()['var_function-call-3412235902006546830']
with open(cpc_definitions_data_path, 'r') as f:
    cpc_definitions_list = json.load(f)
cpc_definitions_df = pd.DataFrame(cpc_definitions_list)

cpc_definitions_level4 = cpc_definitions_df[cpc_definitions_df['level'] == 4.0]

merged_df = pd.merge(best_cpc_df, cpc_definitions_level4, left_on='cpc_group', right_on='symbol', how='inner')

final_result = merged_df[['full_title', 'cpc_group', 'best_year']].to_json(orient='records')

print("__RESULT__:")
print(final_result)"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json'}

exec(code, env_args)
