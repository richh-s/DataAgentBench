code = """import json

# Load stocks
with open(locals()['var_function-call-4042981255458067865'], 'r') as f:
    stocks = json.load(f)

# Load tables
with open(locals()['var_function-call-9311016875752490112'], 'r') as f:
    tables = set(json.load(f))

# Filter
valid_symbols = [s['Symbol'] for s in stocks if s['Symbol'] in tables]

# Build query
parts = []
for s in valid_symbols:
    # Use simple string concat to avoid f-string quote issues
    part = "SELECT '" + s + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + s + "\" WHERE Date LIKE '2017%'"
    parts.append(part)

full_query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps({"query": full_query, "count": len(valid_symbols)}))"""

env_args = {'var_function-call-4042981255458067865': 'file_storage/function-call-4042981255458067865.json', 'var_function-call-10851517854372074132': 234, 'var_function-call-9311016875752490112': 'file_storage/function-call-9311016875752490112.json'}

exec(code, env_args)
