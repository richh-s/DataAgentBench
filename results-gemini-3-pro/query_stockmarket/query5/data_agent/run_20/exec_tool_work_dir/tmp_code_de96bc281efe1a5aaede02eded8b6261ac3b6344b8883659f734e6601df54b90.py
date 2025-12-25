code = """import json

# Load symbols from step 1
file_path_symbols = locals()['var_function-call-9762896799442664376']
with open(file_path_symbols, 'r') as f:
    symbols_data = json.load(f)
    target_symbols = set([item['Symbol'] for item in symbols_data])

# Load tables from step 2
file_path_tables = locals()['var_function-call-15346480681916956948']
with open(file_path_tables, 'r') as f:
    all_tables = set(json.load(f))

# Intersection
valid_symbols = target_symbols.intersection(all_tables)
print(f"Valid symbols found: {len(valid_symbols)}")

# Construct Query
# (High - Low) > 0.2 * Low
sub_queries = []
for sym in valid_symbols:
    # Use double quotes for table names to handle special chars if any
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    sub_queries.append(q)

full_query = " UNION ALL ".join(sub_queries)
full_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-9762896799442664376': 'file_storage/function-call-9762896799442664376.json', 'var_function-call-7368161656916448319': 86, 'var_function-call-15346480681916956948': 'file_storage/function-call-15346480681916956948.json'}

exec(code, env_args)
