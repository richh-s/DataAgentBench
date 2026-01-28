code = """import json

# Read the ETF list from the JSON file
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_list = json.load(f)

# Extract ETF symbols from NYSE Arca (Listing Exchange = 'P')
etf_symbols = [etf['Symbol'] for etf in etf_list]
print('__RESULT__:')
print(json.dumps({'total_etfs': len(etf_symbols), 'sample_symbols': etf_symbols[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
