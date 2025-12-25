code = """import json

# Load tickers from step 1
file_path_tickers = locals()['var_function-call-17273355007471526409']
with open(file_path_tickers, 'r') as f:
    etf_tickers = set(json.load(f))

# Load table names from step 2
file_path_tables = locals()['var_function-call-3183618801010455834']
with open(file_path_tables, 'r') as f:
    db_tables = set(json.load(f))

# Intersect
valid_tickers = sorted(list(etf_tickers.intersection(db_tables)))

print(f"Valid tickers count: {len(valid_tickers)}")

# Prepare batches
batch_size = 50
batches = []
for i in range(0, len(valid_tickers), batch_size):
    batches.append(valid_tickers[i:i+batch_size])

print(f"Number of batches: {len(batches)}")

# Store batches for next steps
print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-6291273035979822157': 'file_storage/function-call-6291273035979822157.json', 'var_function-call-17273355007471526409': 'file_storage/function-call-17273355007471526409.json', 'var_function-call-6700212571527904625': 1435, 'var_function-call-3183618801010455834': 'file_storage/function-call-3183618801010455834.json'}

exec(code, env_args)
