code = """import json

key_etf = 'var_function-call-7361389423706829961'
key_tables = 'var_function-call-12571622607259600225'

with open(locals()[key_etf], 'r') as f:
    etf_list = json.load(f)

with open(locals()[key_tables], 'r') as f:
    tables_list = json.load(f)

etf_symbols = set([x['Symbol'] for x in etf_list])
table_symbols = set(tables_list)

valid_symbols = list(etf_symbols.intersection(table_symbols))
valid_symbols.sort()

batch_size = 300
batches = []
current_batch = []
for sym in valid_symbols:
    current_batch.append(sym)
    if len(current_batch) >= batch_size:
        batches.append(current_batch)
        current_batch = []
if current_batch:
    batches.append(current_batch)

queries = []
for batch in batches:
    parts = []
    for sym in batch:
        q = "SELECT '{}' as Symbol FROM \"{}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1".format(sym, sym)
        parts.append(q)
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print('Total valid symbols:', len(valid_symbols))
print('Number of queries:', len(queries))
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_function-call-4965379198154257053': ['stockinfo'], 'var_function-call-7361389423706829961': 'file_storage/function-call-7361389423706829961.json', 'var_function-call-2696260633542718629': 'file_storage/function-call-2696260633542718629.json', 'var_function-call-12571622607259600225': 'file_storage/function-call-12571622607259600225.json'}

exec(code, env_args)
