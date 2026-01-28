code = """import json

# Load the NYSE non-ETF stocks data
nyse_file = '/tmp/stocked_result_functions.query_db:2.json'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Load the available tables data
tables_file = '/tmp/stocked_result_functions.list_db:5.json'
with open(tables_file, 'r') as f:
    available_tables = json.load(f)

print(f"Total NYSE non-ETF stocks: {len(nyse_stocks)}")
print(f"Total available tables: {len(available_tables)}")

# Create a set for faster lookup
available_set = set(available_tables)

# Find matching stocks
matching_stocks = []
for stock in nyse_stocks:
    if stock['Symbol'] in available_set:
        matching_stocks.append(stock)

print(f"Stocks with both NYSE listing and trade data: {len(matching_stocks)}")
print(f"First 5: {[s['Symbol'] for s in matching_stocks[:5]]}")

result = {
    'count': len(matching_stocks),
    'stocks': matching_stocks[:10]  # Just a sample for preview
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}]}

exec(code, env_args)
