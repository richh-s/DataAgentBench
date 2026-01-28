code = """import json

# The result is stored as a file path
result_file = 'file_storage/functions.query_db:0.json'

# Read the data from the file
with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

print('Found {} stocks in NASDAQ Capital Market'.format(len(nasdaq_capital_stocks)))
print('First 3 stocks:', nasdaq_capital_stocks[:3])

# Extract just the symbols
symbols = [stock['Symbol'] for stock in nasdaq_capital_stocks]

# Create result JSON
result_data = {
    'count': len(nasdaq_capital_stocks),
    'symbols': symbols[:10]  # Just get first 10 for now
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
