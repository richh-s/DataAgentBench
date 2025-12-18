code = """import json

with open(locals()['var_function-call-12451871195317439682'], 'r') as f:
    etf_symbols_data = json.load(f)

etf_symbols = [d['Symbol'] for d in etf_symbols_data['query_db_response']['results']]

union_queries = []
for symbol in etf_symbols:
    union_queries.append(f"SELECT '{symbol}' AS Symbol, MAX(\"Adj Close\") AS MaxAdjClose FROM \"{symbol}\" WHERE Date LIKE '2015-%'")

full_query = " UNION ALL ".join(union_queries) + ";"

print("__RESULT__:")
print(json.dumps({"query": full_query}))"""

env_args = {'var_function-call-12451871195317439682': 'file_storage/function-call-12451871195317439682.json'}

exec(code, env_args)
