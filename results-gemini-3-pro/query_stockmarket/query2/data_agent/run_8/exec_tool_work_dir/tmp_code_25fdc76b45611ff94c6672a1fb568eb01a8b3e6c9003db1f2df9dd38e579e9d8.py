code = """import json

# Load valid ETFs
with open(locals()['var_function-call-6325032711824725866'], 'r') as f:
    valid_etfs = json.load(f)

print(f"Number of valid ETFs: {len(valid_etfs)}")

# Generate SQL query
# We will create batches of 50 to avoid query length issues.
# Each batch will be a single UNION ALL query.
# We will print the batches as a JSON list of query strings.
batches = []
batch_size = 50
current_batch = []

for i, symbol in enumerate(valid_etfs):
    # Sanitize symbol if needed (DuckDB tables are quoted if they contain special chars, but here we assume standard names or quoted)
    # The database description says tables are named after ticker.
    # Tickers might contain special characters? In previous list_db, we saw "CARR#" etc.
    # We should wrap table names in double quotes.
    query_part = f"SELECT '{symbol}' as Symbol FROM \"{symbol}\" WHERE \"Adj Close\" > 200 AND Date BETWEEN '2015-01-01' AND '2015-12-31' LIMIT 1"
    current_batch.append(query_part)
    
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    batches.append(" UNION ALL ".join(current_batch))

print(f"Number of batches: {len(batches)}")
print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json'}

exec(code, env_args)
