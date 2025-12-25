code = """import json

# Load symbols and tables again
with open(locals()['var_function-call-4042981255458067865'], 'r') as f:
    stocks = json.load(f)
with open(locals()['var_function-call-9311016875752490112'], 'r') as f:
    tables = set(json.load(f))

valid_symbols = sorted([s['Symbol'] for s in stocks if s['Symbol'] in tables])

# Chunk size
chunk_size = 50
chunks = [valid_symbols[i:i + chunk_size] for i in range(0, len(valid_symbols), chunk_size)]

# Store chunks for later use if needed, or just print the first query
# We will generate queries for all chunks and return them as a list
queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        part = "SELECT '" + s + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + s + "\" WHERE Date LIKE '2017%'"
        parts.append(part)
    queries.append(" UNION ALL ".join(parts))

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-4042981255458067865': 'file_storage/function-call-4042981255458067865.json', 'var_function-call-10851517854372074132': 234, 'var_function-call-9311016875752490112': 'file_storage/function-call-9311016875752490112.json', 'var_function-call-2653908298918496600': 'file_storage/function-call-2653908298918496600.json', 'var_function-call-10536529764277001005': 'file_storage/function-call-10536529764277001005.json'}

exec(code, env_args)
