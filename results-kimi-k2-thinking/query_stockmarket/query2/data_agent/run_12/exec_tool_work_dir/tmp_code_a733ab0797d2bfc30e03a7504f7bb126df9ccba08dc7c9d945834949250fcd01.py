code = """import json

# Load NYSE Arca ETFs
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nyse_arca_etfs = [item['Symbol'] for item in json.load(f)]

# Load all available tables in stocktrade_database
with open('file_storage/functions.list_db:20.json', 'r') as f:
    all_tables = json.load(f)

# Find intersection (ETFs that have price data)
nyse_arca_etfs_with_data = [symbol for symbol in nyse_arca_etfs if symbol in all_tables]

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_etfs),
    'tables_in_db': len(all_tables),
    'intersection_count': len(nyse_arca_etfs_with_data),
    'sample_etfs': nyse_arca_etfs_with_data[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'total_etfs': 1435, 'test_symbols': ['GLD', 'SPY', 'IVV', 'VOO', 'AGG']}, 'var_functions.list_db:20': 'file_storage/functions.list_db:20.json'}

exec(code, env_args)
