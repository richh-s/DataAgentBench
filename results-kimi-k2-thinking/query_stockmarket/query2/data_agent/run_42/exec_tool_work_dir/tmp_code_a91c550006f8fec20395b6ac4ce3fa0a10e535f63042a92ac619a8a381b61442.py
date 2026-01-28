code = """import json
import os

# Read the full list of NYSE Arca ETFs
with open('/tmp/tmp9s2j7n8i.json', 'r') as f:
    nyse_arca_etfs = json.load(f)

# Read the available ticker tables from stocktrade_database
with open('/tmp/tmpm8hwhm_u.json', 'r') as f:
    all_tickers = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_count': len(nyse_arca_etfs),
    'total_tickers_count': len(all_tickers)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
