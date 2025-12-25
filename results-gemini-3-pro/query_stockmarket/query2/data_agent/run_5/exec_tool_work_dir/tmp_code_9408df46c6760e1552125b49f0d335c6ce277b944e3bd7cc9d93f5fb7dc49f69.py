code = """import json

# Get file path
valid_symbols_path = locals()['var_function-call-11973061372010644575']

with open(valid_symbols_path, 'r') as f:
    valid_symbols = json.load(f)

# Construct query
# Use Date LIKE '2015-%' or string comparison. String comparison is standard for ISO dates.
# Note: Table names in DuckDB are case sensitive if quoted, but usually these tickers are uppercase.
# I will use double quotes for table names just in case.

subqueries = []
for sym in valid_symbols:
    # Escape symbol if necessary (though usually they are just letters)
    # DuckDB/SQL requires doubling single quotes if they exist, but tickers don't usually have them.
    # But I should double quote the identifier.
    q = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
    subqueries.append(q)

full_query = " UNION ALL ".join(subqueries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-16341739704993987166': 'file_storage/function-call-16341739704993987166.json', 'var_function-call-17860090179265240781': 'file_storage/function-call-17860090179265240781.json', 'var_function-call-11973061372010644575': 'file_storage/function-call-11973061372010644575.json', 'var_function-call-16861433214838265826': 1435}

exec(code, env_args)
