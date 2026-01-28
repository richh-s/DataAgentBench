code = """import json

# Read the full result from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    nasdaq_capital_companies = json.load(f)

# Extract ticker symbols
tickers = [company['Symbol'] for company in nasdaq_capital_companies]
print('__RESULT__:')
print(json.dumps({'tickers': tickers, 'count': len(tickers)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
