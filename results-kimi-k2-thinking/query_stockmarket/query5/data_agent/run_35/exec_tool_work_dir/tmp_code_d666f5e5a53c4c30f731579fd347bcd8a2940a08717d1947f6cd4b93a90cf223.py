code = """import json

# Read the list of symbols and descriptions
nasdaq_data_path = locals()['var_functions.execute_python:16']
with open(nasdaq_data_path, 'r') as f:
    data = json.load(f)

symbols = data['symbols']
symbol_to_desc = data['symbol_to_desc']

# Create the combined query
query_parts = []
for symbol in symbols:
    query_part = "SELECT '{}' as Symbol, COUNT(*) as HighVolDays FROM '{}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (Low * 0.2)".format(symbol, symbol)
    query_parts.append(query_part)

# Combine with UNION ALL for efficiency
combined_query = ' UNION ALL '.join(query_parts) + ' ORDER BY HighVolDays DESC'

print(f"Generated combined query with {len(symbols)} symbols")
print(f"First 200 characters of query: {combined_query[:200]}...")

# Save the query and related info
result = {
    "combined_query": combined_query,
    "symbol_count": len(symbols)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)
