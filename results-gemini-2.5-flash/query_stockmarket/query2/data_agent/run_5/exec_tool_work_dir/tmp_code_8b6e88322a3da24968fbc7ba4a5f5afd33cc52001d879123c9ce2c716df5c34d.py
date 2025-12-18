code = """import json

# Load the ETF symbols from the file
with open(locals()['var_function-call-12924490716098124307'], 'r') as f:
    etf_symbols_data = json.load(f)

all_symbols = [d['Symbol'] for d in etf_symbols_data]

BATCH_SIZE = 50
processed_symbols_count = 0
qualified_etfs = []

current_batch_symbols = all_symbols[processed_symbols_count : processed_symbols_count + BATCH_SIZE]

query_parts = []
if current_batch_symbols:
    for symbol in current_batch_symbols:
        # Ensure double quotes around table names (symbols) and column names for DuckDB
        query_parts.append(f"SELECT '{symbol}' AS Symbol FROM \"{symbol}\" WHERE Date LIKE '2015-%' AND \"Adj Close\" > 200.0")
    
    combined_query = " UNION ALL ".join(query_parts)
else:
    combined_query = None

# Prepare the state for the next step.
# This JSON output will be available as a variable in the next tool call.
output_state = {
    'query_to_run': combined_query,
    'processed_symbols_count': processed_symbols_count,
    'qualified_etfs': qualified_etfs,
    'all_symbols': all_symbols # Keep all symbols for subsequent batching
}

print("__RESULT__:")
print(json.dumps(output_state))"""

env_args = {'var_function-call-12924490716098124307': 'file_storage/function-call-12924490716098124307.json'}

exec(code, env_args)
