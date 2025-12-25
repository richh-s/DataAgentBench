code = """import json

# Get filenames
etf_file = locals()['var_function-call-17042838615002828598']
tables_file = locals()['var_function-call-1654927262755686554']

with open(etf_file, 'r') as f:
    etf_data = json.load(f)
etf_symbols = set([item['Symbol'] for item in etf_data])

with open(tables_file, 'r') as f:
    tables = json.load(f)
table_set = set(tables)

valid_etfs = list(etf_symbols.intersection(table_set))

# Construct query
subqueries = []
for sym in valid_etfs:
    # Use double quotes for table name in case of special chars or keywords, though symbols are usually safe.
    # Also escape double quotes in symbol if any (unlikely for tickers).
    q = f'SELECT \'{sym}\' as Symbol, MAX("Adj Close") as MaxPrice FROM "{sym}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\''
    subqueries.append(q)

full_query = "SELECT Symbol FROM (" + " UNION ALL ".join(subqueries) + ") WHERE MaxPrice > 200"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json', 'var_function-call-8866745000760518391': 'file_storage/function-call-8866745000760518391.json', 'var_function-call-802954950120546445': 1435}

exec(code, env_args)
