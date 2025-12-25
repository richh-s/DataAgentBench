code = """import json
import pandas as pd

best_cpc_list_str = locals()['var_function-call-2925605632421467179']
best_cpc_list = json.loads(best_cpc_list_str)
cpc_group_symbols = [item['cpc_group'] for item in best_cpc_list]

# Construct the LIKE clauses for the SQL query
like_clauses = [f"symbol LIKE '{symbol}%'" for symbol in cpc_group_symbols]
query_condition = " OR ".join(like_clauses)

print("__RESULT__:")
print(json.dumps(query_condition))"""

env_args = {'var_function-call-12286119263325599604': 'file_storage/function-call-12286119263325599604.json', 'var_function-call-17238172386859849011': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 0.6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 0.5}], 'var_function-call-15995829258352346263': [], 'var_function-call-15786196653833816783': 'file_storage/function-call-15786196653833816783.json', 'var_function-call-2044574974618873207': [], 'var_function-call-6381926105834134672': 'file_storage/function-call-6381926105834134672.json', 'var_function-call-6484813827852245575': 'A61F, A43B', 'var_function-call-8800901605693715834': [], 'var_function-call-2936073602088239421': 'file_storage/function-call-2936073602088239421.json', 'var_function-call-3412235902006546830': 'file_storage/function-call-3412235902006546830.json', 'var_function-call-12997310755155396542': 'file_storage/function-call-12997310755155396542.json', 'var_function-call-2925605632421467179': [{'cpc_group': 'A61F', 'best_year': 2016, 'highest_ema': 6}, {'cpc_group': 'A43B', 'best_year': 2016, 'highest_ema': 5}], 'var_function-call-14461189417186399412': "'A61F', 'A43B'", 'var_function-call-1776554272434386262': []}

exec(code, env_args)
