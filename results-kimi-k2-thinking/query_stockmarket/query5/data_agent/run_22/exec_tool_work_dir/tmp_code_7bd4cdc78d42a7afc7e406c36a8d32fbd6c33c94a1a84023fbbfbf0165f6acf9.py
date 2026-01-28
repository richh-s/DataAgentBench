code = """import json

# Load the full result from the file
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    capital_market_companies = json.load(f)

# Extract ticker symbols
tickers = [company['Symbol'] for company in capital_market_companies]

print('__RESULT__:')
print(json.dumps({
    'num_companies': len(tickers),
    'sample_tickers': tickers[:10],
    'tickers': tickers
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
