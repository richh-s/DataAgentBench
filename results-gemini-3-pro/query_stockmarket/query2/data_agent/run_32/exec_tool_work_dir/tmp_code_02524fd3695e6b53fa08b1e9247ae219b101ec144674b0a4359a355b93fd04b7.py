code = """import json

# Get file path from local variables
valid_symbols_path = locals()['var_function-call-17904107048790784824']

# Load valid symbols
with open(valid_symbols_path, 'r') as f:
    valid_symbols = json.load(f)

# Batch size
BATCH_SIZE = 500
batches = []

for i in range(0, len(valid_symbols), BATCH_SIZE):
    batch = valid_symbols[i:i+BATCH_SIZE]
    queries = []
    for sym in batch:
        # Use double quotes for table name in case of reserved words or special chars
        q = f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        queries.append(q)
    
    full_query = " UNION ALL ".join(queries)
    batches.append(full_query)

print(f"Total symbols: {len(valid_symbols)}")
print(f"Number of batches: {len(batches)}")

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-8664818229940641972': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-925302824515021952': 'file_storage/function-call-925302824515021952.json', 'var_function-call-16367137017631694844': 'file_storage/function-call-16367137017631694844.json', 'var_function-call-17904107048790784824': 'file_storage/function-call-17904107048790784824.json'}

exec(code, env_args)
