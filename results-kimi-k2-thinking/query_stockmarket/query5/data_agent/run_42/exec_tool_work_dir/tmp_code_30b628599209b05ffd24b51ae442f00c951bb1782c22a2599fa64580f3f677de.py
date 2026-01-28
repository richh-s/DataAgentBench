code = """import json

# Read the file path from the storage
data_file = locals()['var_functions.query_db:0']

# Load the JSON data from the file
with open(data_file, 'r') as f:
    stock_data = json.load(f)

# Extract tickers from NASDAQ Capital Market Companies
tickers = [stock['Symbol'] for stock in stock_data]

print('__RESULT__:')
print(json.dumps({
    'tickers': tickers,
    'count': len(tickers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
