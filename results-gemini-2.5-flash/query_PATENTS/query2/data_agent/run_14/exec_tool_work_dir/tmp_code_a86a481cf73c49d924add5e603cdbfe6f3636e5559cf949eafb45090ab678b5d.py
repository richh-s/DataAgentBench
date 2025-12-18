code = """import pandas as pd
import json

best_cpc_groups_str = locals()['var_function-call-2925605632421467179']
best_cpc_list = json.loads(best_cpc_groups_str)
best_cpc_df = pd.DataFrame(best_cpc_list)

cpc_definitions_data_path = locals()['var_function-call-2445608865627351311']
with open(cpc_definitions_data_path, 'r') as f:
    cpc_definitions_list = json.load(f)
cpc_definitions_df = pd.DataFrame(cpc_definitions_list)

# Filter CPC definitions for level 4 (this is already done by the previous query, but ensuring consistency)
cpc_definitions_level4 = cpc_definitions_df[cpc_definitions_df['level'] == 4.0]

# Merge the two dataframes on the CPC group/symbol
merged_df = pd.merge(best_cpc_df, cpc_definitions_level4, left_on='cpc_group', right_on='symbol', how='inner')

# Select the required columns: full_title, cpc_group, and best_year
final_result_df = merged_df[['full_title', 'cpc_group', 'best_year']]
final_result = final_result_df.to_json(orient='records')

print("__RESULT__:")
print(final_result)"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json', 'var_function-call-12997310755155396542': 'file_storage/function-call-12997310755155396542.json', 'var_function-call-2925605632421467179': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 5}], 'var_function-call-14461189417186399412': "'A61F', 'A43B'", 'var_function-call-1776554272434386262': [], 'var_function-call-14901571610843142513': [{'titleFull': 'CHARACTERISTIC FEATURES OF FOOTWEAR; PARTS OF FOOTWEAR', 'symbol': 'A43B', 'level': '5.0'}, {'titleFull': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS', 'symbol': 'A61F', 'level': '5.0'}], 'var_function-call-2445608865627351311': 'file_storage/function-call-2445608865627351311.json'}

exec(code, env_args)
