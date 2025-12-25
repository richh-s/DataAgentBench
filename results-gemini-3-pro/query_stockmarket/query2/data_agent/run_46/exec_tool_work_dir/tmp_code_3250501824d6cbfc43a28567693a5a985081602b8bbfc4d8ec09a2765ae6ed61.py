code = """import json

# Read valid symbols
with open(locals()['var_function-call-10604229133623975260'], 'r') as f:
    symbols = json.load(f)

queries = []
for sym in symbols:
    # constructing the query string carefully
    # SELECT 'SYM' as Symbol, MAX("Adj Close") as MaxPrice FROM "SYM" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX("Adj Close") > 200
    q = "SELECT '" + sym + "' as Symbol, MAX(\"Adj Close\") as MaxPrice FROM \"" + sym + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX(\"Adj Close\") > 200"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5162594856234074983': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12055750503848787858': 'file_storage/function-call-12055750503848787858.json', 'var_function-call-1195933028834543906': 'file_storage/function-call-1195933028834543906.json', 'var_function-call-4479522260417322904': 'file_storage/function-call-4479522260417322904.json', 'var_function-call-10604229133623975260': 'file_storage/function-call-10604229133623975260.json'}

exec(code, env_args)
