code = """import json

# Load ETF list
with open(locals()['var_function-call-7361389423706829961'], 'r') as f:
    etf_list = json.load(f)
etf_symbols = set([x['Symbol'] for x in etf_list])

# Load Table list
with open(locals()['var_function-call-12571622607259600225'], 'r') as f:
    tables_list = json.load(f)
table_symbols = set(tables_list)

# Intersection
valid_symbols = list(etf_symbols.intersection(table_symbols))
valid_symbols.sort()

# Create batches
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

# Generate queries
queries = []
for batch in batches:
    parts = []
    for sym in batch:
        # Use double quotes for table names in case of reserved words or special chars
        # DuckDB should handle "Sym"
        part = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
        parts.append(part)
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print(f"Total valid symbols: {len(valid_symbols)}")
print(f"Number of queries: {len(queries)}")
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-4965379198154257053': ['stockinfo'], 'var_function-call-7361389423706829961': 'file_storage/function-call-7361389423706829961.json', 'var_function-call-2696260633542718629': 'file_storage/function-call-2696260633542718629.json', 'var_function-call-12571622607259600225': 'file_storage/function-call-12571622607259600225.json'}

exec(code, env_args)
