code = """import json

# Load the ETF symbols from the file obtained from the first query_db call
with open(locals()['var_function-call-7832565910337814431'], 'r') as f:
    etf_symbols_data = json.load(f)

all_symbols = [d['Symbol'] for d in etf_symbols_data]

# Define batch size
BATCH_SIZE = 50

# Initialize state for the iteration. This state will be passed across turns.
# For the first turn, processed_index is 0 and qualified_etfs is empty.
current_state = {
    'all_symbols': all_symbols,
    'processed_index': 0, # Index of the next symbol to process
    'qualified_etfs': [] # List to store symbols that meet the criteria
}

# Determine the current batch of symbols to process
start_index = current_state['processed_index']
end_index = min(start_index + BATCH_SIZE, len(current_state['all_symbols']))
current_batch_symbols = current_state['all_symbols'][start_index:end_index]

# Construct the UNION ALL query for the current batch
combined_query = None
if current_batch_symbols:
    union_queries = []
    for symbol in current_batch_symbols:
        # Each subquery selects the symbol if it meets the criteria in 2015
        # using double quotes for table (symbol) name and column name for DuckDB
        union_queries.append(f"SELECT '{symbol}' AS Symbol FROM \"{symbol}\" WHERE Date LIKE '2015-%' AND \"Adj Close\" > 200.0 LIMIT 1")
    combined_query = " UNION ALL ".join(union_queries)

# Prepare the output for the next tool call. This will include the state for the next turn
# and the query to be executed in this turn.
output = {
    'state': current_state, # Pass the current state to the next turn (or for internal use)
    'query_to_execute': combined_query # The query for the current batch
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-12924490716098124307': 'file_storage/function-call-12924490716098124307.json', 'var_function-call-4577222462637675700': 'file_storage/function-call-4577222462637675700.json', 'var_function-call-7832565910337814431': 'file_storage/function-call-7832565910337814431.json'}

exec(code, env_args)
