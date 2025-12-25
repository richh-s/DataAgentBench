code = """import json

# Load valid symbols
file_path = locals()['var_function-call-7434327097366713516']
with open(file_path, 'r') as f:
    valid_symbols = json.load(f)

# Batch size
BATCH_SIZE = 80
queries = []

for i in range(0, len(valid_symbols), BATCH_SIZE):
    batch = valid_symbols[i:i+BATCH_SIZE]
    # specific SQL dialect for DuckDB
    # SELECT 'SYM' AS Symbol FROM SYM WHERE "Adj Close" > 200 AND Date BETWEEN '2015-01-01' AND '2015-12-31' LIMIT 1
    # UNION ALL ...
    
    parts = []
    for sym in batch:
        # Ensure symbol is safe (though they seem alphanumeric)
        # Using double quotes for table identifier if needed, but simple names work.
        # Check for reserved words?
        # Enclosing table name in quotes "SYM" is safer.
        part = f"SELECT '{sym}' AS Symbol FROM \"{sym}\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
        parts.append(part)
    
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print(f"Generated {len(queries)} queries.")
print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-16817766424675427763': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12499338069894364565': 'file_storage/function-call-12499338069894364565.json', 'var_function-call-9293888739121941435': 'file_storage/function-call-9293888739121941435.json', 'var_function-call-14915668202036031869': 'file_storage/function-call-14915668202036031869.json', 'var_function-call-7434327097366713516': 'file_storage/function-call-7434327097366713516.json', 'var_function-call-2380757378116549886': [{'Date': '2018-08-15'}], 'var_function-call-7107660430946483903': 1435}

exec(code, env_args)
