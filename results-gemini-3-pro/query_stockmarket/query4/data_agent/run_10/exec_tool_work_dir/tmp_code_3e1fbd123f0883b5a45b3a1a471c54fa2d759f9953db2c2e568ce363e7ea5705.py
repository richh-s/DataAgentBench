code = """import json

# Load candidate symbols from stockinfo result
with open(locals()['var_function-call-6393703521614786747'], 'r') as f:
    candidates = json.load(f)

candidate_symbols = set(c['Symbol'] for c in candidates)

# Load available tables
with open(locals()['var_function-call-14160190749123252694'], 'r') as f:
    tables = json.load(f)

available_tables = set(tables)

# Intersect
valid_symbols = list(candidate_symbols.intersection(available_tables))

# Construct SQL query
queries = []
for sym in valid_symbols:
    # Use simple string concatenation or single quotes to avoid triple quote issues
    # quoting table name with double quotes just in case
    q = "SELECT '" + sym + "' AS Symbol, SUM(CASE WHEN \"Close\" > \"Open\" THEN 1 ELSE 0 END) AS UpDays, SUM(CASE WHEN \"Close\" < \"Open\" THEN 1 ELSE 0 END) AS DownDays FROM \"" + sym + "\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("Number of valid symbols: " + str(len(valid_symbols)))
print("Query length: " + str(len(full_query)))

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-6393703521614786747': 'file_storage/function-call-6393703521614786747.json', 'var_function-call-17168036801476034566': 234, 'var_function-call-14160190749123252694': 'file_storage/function-call-14160190749123252694.json'}

exec(code, env_args)
