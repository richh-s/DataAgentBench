code = """import json

# Load valid symbols
with open(locals()['var_function-call-7323746392053808009'], 'r') as f:
    data = json.load(f)
    valid_symbols = data['valid_symbols']

# Construct query
queries = []
for sym in valid_symbols:
    # Double quote the table name just in case of keywords, though these symbols seem fine.
    # But usually table names are case sensitive in some contexts or need quotes if they conflict.
    # The list_db output showed uppercase names.
    q = f"SELECT '{sym}' AS Symbol, COUNT(*) AS DayCount FROM \"{sym}\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.20 * Low)"
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY DayCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-12648435365939612161': 'file_storage/function-call-12648435365939612161.json', 'var_function-call-16816668521200579530': 'file_storage/function-call-16816668521200579530.json', 'var_function-call-7323746392053808009': 'file_storage/function-call-7323746392053808009.json'}

exec(code, env_args)
