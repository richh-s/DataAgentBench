code = """import json

with open(locals()['var_function-call-16760421366032888909'], 'r') as f:
    etf_symbols_data = json.load(f)

symbols_list = [d['Symbol'] for d in etf_symbols_data]

union_queries = []
for symbol in symbols_list:
    union_queries.append(f"SELECT '{symbol}' AS Symbol, \"Adj Close\" FROM \"{symbol}\" WHERE Date LIKE '2015-%' AND \"Adj Close\" > 200")

full_query = " UNION ALL ".join(union_queries)

print('__RESULT__:')
print(json.dumps(full_query))"""

env_args = {'var_function-call-16760421366032888909': 'file_storage/function-call-16760421366032888909.json', 'var_function-call-10081194206272817670': 1435}

exec(code, env_args)
