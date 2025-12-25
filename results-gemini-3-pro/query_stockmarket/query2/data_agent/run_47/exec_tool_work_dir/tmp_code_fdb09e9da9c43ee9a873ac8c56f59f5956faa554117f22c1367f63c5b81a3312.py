code = """import json

with open(locals()['var_function-call-18089665588996577560'], 'r') as f:
    valid_symbols = json.load(f)

# Chunk into 3 parts
chunk_size = (len(valid_symbols) + 2) // 3
batches = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

queries = []
for batch in batches:
    subqueries = []
    for sym in batch:
        # Escape double quotes in symbol if any (unlikely for tickers but safe practice)
        # But usually tickers are just alphanumeric.
        # We need to be careful about table names.
        q = f'SELECT \'{sym}\' as Symbol FROM "{sym}" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'
        subqueries.append(q)
    full_query = " UNION ALL ".join(subqueries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-7344486637286600100': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2454856655276099395': 'file_storage/function-call-2454856655276099395.json', 'var_function-call-6642693361376335155': 'file_storage/function-call-6642693361376335155.json', 'var_function-call-18089665588996577560': 'file_storage/function-call-18089665588996577560.json', 'var_function-call-8976669871907571712': 1435}

exec(code, env_args)
