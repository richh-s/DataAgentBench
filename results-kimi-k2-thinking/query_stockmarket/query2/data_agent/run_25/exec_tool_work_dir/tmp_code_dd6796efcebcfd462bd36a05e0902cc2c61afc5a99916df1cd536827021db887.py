code = """import json
import os

# Load the query result from the file
with open(locals()['var_functions.query_db:0'], 'r') as f:
    tickers_data = json.load(f)

# Extract ticker symbols for NYSE Arca ETFs
nyse_arca_etfs = [item['Symbol'] for item in tickers_data]

# Print count and first few symbols
print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'first_10_symbols': nyse_arca_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
