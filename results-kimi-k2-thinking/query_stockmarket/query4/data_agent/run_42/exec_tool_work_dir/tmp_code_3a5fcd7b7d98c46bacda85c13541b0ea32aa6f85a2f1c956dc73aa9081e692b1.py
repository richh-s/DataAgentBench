code = """import json

# Access the stored results using the correct keys
nyse_result_path = locals()['var_functions.query_db:2']
tables_result_path = locals()['var_functions.list_db:5']

print(f"NYSE result path: {nyse_result_path}")
print(f"Tables result path: {tables_result_path}")

# Load the data
with open(nyse_result_path, 'r') as f:
    nyse_stocks = json.load(f)

with open(tables_result_path, 'r') as f:
    available_tables = json.load(f)

print(f"Total NYSE non-ETF stocks: {len(nyse_stocks)}")
print(f"Total available tables: {len(available_tables)}")

# Find intersection (stocks with both NYSE listing and trade data)
available_set = set(available_tables)
matching_stocks = []
for stock in nyse_stocks:
    if stock['Symbol'] in available_set:
        matching_stocks.append(stock)

print(f"Matching stocks: {len(matching_stocks)}")
print("First 5 matching stocks:", [(s['Symbol'], s['Company Description'][:50]) for s in matching_stocks[:5]])

result = {
    'nyse_count': len(nyse_stocks),
    'tables_count': len(available_tables),
    'matching_count': len(matching_stocks),
    'matching_symbols': [s['Symbol'] for s in matching_stocks[:10]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}], 'var_functions.query_db:14': [{'test': 'AAPL'}]}

exec(code, env_args)
