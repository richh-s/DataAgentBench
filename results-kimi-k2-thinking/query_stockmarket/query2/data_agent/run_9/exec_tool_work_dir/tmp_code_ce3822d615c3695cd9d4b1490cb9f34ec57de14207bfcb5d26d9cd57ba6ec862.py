code = """import json
# Load the NYSE Arca ETFs data (this is the full result stored in the file)
with open(var_functions.query_db:0, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Get the key name for the list_db result
list_db_key = 'var_functions.list_db:2'
# Load the list of available tables (tickers)
with open(locals()[list_db_key], 'r') as f:
    available_tickers = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etfs_count': len(nyse_arca_etfs),
    'available_tickers_count': len(available_tickers),
    'sample_etfs': nyse_arca_etfs[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
