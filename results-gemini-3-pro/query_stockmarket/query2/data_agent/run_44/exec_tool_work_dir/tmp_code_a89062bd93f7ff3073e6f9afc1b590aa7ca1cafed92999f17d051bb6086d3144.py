code = """import json

path = locals()['var_function-call-7434327097366713516']
with open(path, 'r') as f:
    valid_symbols = json.load(f)

queries = []
BATCH_SIZE = 50

for i in range(0, len(valid_symbols), BATCH_SIZE):
    batch = valid_symbols[i:i+BATCH_SIZE]
    parts = []
    for sym in batch:
        # Use simple string concatenation
        q = "SELECT '" + sym + "' AS Symbol FROM \"" + sym + "\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
        parts.append(q)
    
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print(len(queries))
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-16817766424675427763': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12499338069894364565': 'file_storage/function-call-12499338069894364565.json', 'var_function-call-9293888739121941435': 'file_storage/function-call-9293888739121941435.json', 'var_function-call-14915668202036031869': 'file_storage/function-call-14915668202036031869.json', 'var_function-call-7434327097366713516': 'file_storage/function-call-7434327097366713516.json', 'var_function-call-2380757378116549886': [{'Date': '2018-08-15'}], 'var_function-call-7107660430946483903': 1435, 'var_function-call-3063757488003502576': 'Hello', 'var_function-call-16536889929438009237': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}

exec(code, env_args)
