code = """import json

# Load candidates from previous step
previous_result_file = locals()['var_function-call-14133125675221425702']
with open(previous_result_file, 'r') as f:
    data = json.load(f)
    candidates = data['candidates']

# Generate SQL
queries = []
for item in candidates:
    sym = item['Symbol']
    # Use double quotes for table names just in case of keywords/case sensitivity, though usually uppercase is fine.
    # DuckDB is case insensitive for unquoted identifiers usually, but let's be safe.
    q = f"SELECT '{sym}' AS Symbol, Open, Close FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-15963372887811120509': 'file_storage/function-call-15963372887811120509.json', 'var_function-call-11545474830056359161': 'file_storage/function-call-11545474830056359161.json', 'var_function-call-14133125675221425702': 'file_storage/function-call-14133125675221425702.json', 'var_function-call-5008870228021754307': [{'Date': '2019-10-24'}]}

exec(code, env_args)
