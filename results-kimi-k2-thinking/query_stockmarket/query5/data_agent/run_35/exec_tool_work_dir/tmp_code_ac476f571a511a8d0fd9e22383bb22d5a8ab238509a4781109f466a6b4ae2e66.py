code = """import json

# Read the symbols and descriptions
nasdaq_data_path = locals()['var_functions.execute_python:16']
with open(nasdaq_data_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
symbol_to_desc = data['symbol_to_desc']

# Create a comprehensive query - process all symbols in smaller batches
batch_size = 20
all_batches = []

for batch_start in range(0, len(symbols), batch_size):
    batch_symbols = symbols[batch_start:batch_start + batch_size]
    
    union_parts = []
    for symbol in batch_symbols:
        part = f"SELECT '{symbol}' as Symbol, COUNT(*) as HighVolDays FROM \"{symbol}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (Low * 0.2)"
        union_parts.append(part)
    
    batch_query = ' UNION ALL '.join(union_parts)
    all_batches.append(batch_query)

# Store batches information
result = {
    "total_symbols": len(symbols),
    "batch_count": len(all_batches),
    "batch_size": batch_size,
    "batches": all_batches
}

print(f"Created {len(all_batches)} batches of queries")

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'Symbol': 'PECK', 'HighVolDays': '19'}], 'var_functions.query_db:24': [{'Symbol': 'CBAT', 'HighVolDays': '23'}, {'Symbol': 'FAMI', 'HighVolDays': '23'}, {'Symbol': 'AGMH', 'HighVolDays': '13'}, {'Symbol': 'BHAT', 'HighVolDays': '10'}, {'Symbol': 'BOSC', 'HighVolDays': '3'}]}

exec(code, env_args)
