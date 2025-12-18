code = """import json

etfs_on_nyse_arca_json_path = locals()['var_function-call-992299585120915343']
with open(etfs_on_nyse_arca_json_path, 'r') as f:
    etfs_on_nyse_arca = json.load(f)

symbols = [d['Symbol'] for d in etfs_on_nyse_arca]

sample_symbols = symbols[:5] # Process a small sample to test

union_parts = []
for symbol in sample_symbols:
    query_part = f"SELECT '{symbol}' AS Symbol FROM \"{symbol}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
    union_parts.append(query_part)

full_query = " UNION ALL ".join(union_parts)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-992299585120915343': 'file_storage/function-call-992299585120915343.json', 'var_function-call-16882642032979634513': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'var_function-call-13966784010077465726': 'AAAU'}

exec(code, env_args)
