code = """import json

path = locals()['var_function-call-6178811675160687356']
with open(path, 'r') as f:
    valid_stocks = json.load(f)

# Extract symbols
symbols = [s['Symbol'] for s in valid_stocks]

# Create batches
batch_size = 50
batches = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    # Construct query
    parts = []
    for sym in batch:
        # Use single quotes for inner SQL string literals, escaped double quotes for table names
        part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        parts.append(part)
    full_query = " UNION ALL ".join(parts)
    batches.append(full_query)

print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_function-call-305604398678755186': 'file_storage/function-call-305604398678755186.json', 'var_function-call-2255113569688009603': 'file_storage/function-call-2255113569688009603.json', 'var_function-call-6178811675160687356': 'file_storage/function-call-6178811675160687356.json', 'var_function-call-8115388233719900790': 234}

exec(code, env_args)
