code = """import pandas as pd
import json

best_cpc_groups_data = json.loads(locals()['var_function-call-17238172386859849011'])
best_cpc_df = pd.DataFrame(best_cpc_groups_data)

cpc_definitions_data = pd.read_json(locals()['var_function-call-3412235902006546830'])

def get_full_title(symbol, definitions_df):
    filtered_df = definitions_df[definitions_df['symbol'] == symbol]
    if not filtered_df.empty:
        return filtered_df['titleFull'].iloc[0]
    return None

best_cpc_df['full_title'] = best_cpc_df['cpc_group'].apply(lambda x: get_full_title(x, cpc_definitions_data))

final_result = best_cpc_df[best_cpc_df['full_title'].notna()].to_json(orient='records')

print("__RESULT__:")
print(final_result)"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json'}

exec(code, env_args)
