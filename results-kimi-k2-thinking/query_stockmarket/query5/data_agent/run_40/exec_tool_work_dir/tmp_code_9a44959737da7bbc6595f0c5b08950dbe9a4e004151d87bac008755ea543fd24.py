code = """import json

# Access the companies list using locals()
companies_list = locals()['var_functions.query_db:0']

# Get ticker symbols from NASDAQ Capital Market companies (Market Category = 'S')
nasdaq_cap_tickers = [company['Symbol'] for company in companies_list]

print('__RESULT__:')
print(json.dumps({'tickers_sample': nasdaq_cap_tickers[:10], 'total_count': len(nasdaq_cap_tickers)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
