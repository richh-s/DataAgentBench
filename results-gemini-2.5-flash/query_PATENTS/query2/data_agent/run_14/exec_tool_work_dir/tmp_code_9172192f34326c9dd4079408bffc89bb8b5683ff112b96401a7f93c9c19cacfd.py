code = """import pandas as pd
import json

best_cpc_groups_str = locals()['var_function-call-17238172386859849011']
best_cpc_list = json.loads(best_cpc_groups_str)
best_cpc_df = pd.DataFrame(best_cpc_list)

cpc_definitions_data_path = locals()['var_function-call-12997310755155396542']
with open(cpc_definitions_data_path, 'r') as f:
    cpc_definitions_list = json.load(f)
cpc_definitions_df = pd.DataFrame(cpc_definitions_list)

# Ensure 'level' column is present and correctly typed for filtering
if 'level' not in cpc_definitions_df.columns:
    # Assuming level is implicitly 4 if not explicitly given and we are joining on it, or need to retrieve it.
    # For this problem, we queried for level=4 explicitly in the DB, so it should be there. If not, this needs adjustment.
    # Let's assume for now the previous query actually returned level 4 entries, so we only need to filter by symbol.
    pass

# Filter CPC definitions for level 4 (this should be already done by the query, but good to double check or re-filter if needed)
# If the previous query `SELECT "titleFull", symbol FROM cpc_definition WHERE level = 4;` indeed returned only level 4, this step might be redundant.
# However, to be robust, let's ensure we are working with actual level 4 data, if `level` was part of the previous query and not just `titleFull` and `symbol`
# Based on the description, the previous query *did* get all level 4 data.

# We need to map the 'symbol' from cpc_definitions_df to 'cpc_group' in best_cpc_df
# It seems 'symbol' in cpc_definitions_df is the full CPC code, which corresponds to 'cpc_group' (first 4 chars of CPC code) from best_cpc_df

merged_df = pd.merge(best_cpc_df, cpc_definitions_df, left_on='cpc_group', right_on='symbol', how='inner')

# Select the required columns and format the output
final_result_df = merged_df[['full_title', 'cpc_group', 'best_year']]
final_result = final_result_df.to_json(orient='records')

print("__RESULT__:")
print(final_result)"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json', 'var_function-call-12997310755155396542': 'file_storage/function-call-12997310755155396542.json'}

exec(code, env_args)
