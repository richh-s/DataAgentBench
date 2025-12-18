code = """import pandas as pd
import json

best_cpc_df = pd.read_json(locals()['var_function-call-17238172386859849011'])
cpc_group_symbols = best_cpc_df['cpc_group'].tolist()

query_symbols = []
for symbol in cpc_group_symbols:
    query_symbols.append(f"symbol LIKE '{symbol}%'")

query_string = " OR ".join(query_symbols)

print("__RESULT__:")
print(json.dumps(query_string))"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json'}

exec(code, env_args)
