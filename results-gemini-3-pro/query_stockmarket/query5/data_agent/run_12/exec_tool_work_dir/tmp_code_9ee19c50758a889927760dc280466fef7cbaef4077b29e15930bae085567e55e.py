code = """import json

with open(locals()['var_function-call-2084531363548133324'], 'r') as f:
    stock_data = json.load(f)
target_symbols = set([row['Symbol'] for row in stock_data])

with open(locals()['var_function-call-13796056807525861367'], 'r') as f:
    tables = json.load(f)
existing_tables = set(tables)

valid_symbols = sorted(list(target_symbols.intersection(existing_tables)))

chunk_size = 30
chunks = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

queries = []
for chunk in chunks:
    subqueries = []
    for sym in chunk:
        # Use single quotes for the python string to avoid backslash issues with double quotes
        q = 'SELECT \'{0}\' as Symbol, COUNT(*) as Days FROM "{0}" WHERE Date LIKE \'2019-%\' AND (High - Low) > 0.20 * Low'.format(sym)
        subqueries.append(q)
    full_q = " UNION ALL ".join(subqueries)
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-2084531363548133324': 'file_storage/function-call-2084531363548133324.json', 'var_function-call-241126668365207331': {'count': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-13796056807525861367': 'file_storage/function-call-13796056807525861367.json', 'var_function-call-10907591971367091177': 'file_storage/function-call-10907591971367091177.json', 'var_function-call-216696704061701173': 'file_storage/function-call-216696704061701173.json'}

exec(code, env_args)
