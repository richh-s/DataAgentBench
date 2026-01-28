code = """import json

# Load the relevant queries results
nyse_file = locals()['var_functions.query_db:10']
trade_tables_file = locals()['var_functions.list_db:16']

with open(nyse_file, 'r') as f:
    nyse_etfs = [item['Symbol'] for item in json.load(f)]

with open(trade_tables_file, 'r') as f:
    trade_tables = json.load(f)

nyse_etfs_set = set(nyse_etfs)
trade_tables_set = set(trade_tables)

# Find ETFs that have price data tables
common_etfs = nyse_etfs_set.intersection(trade_tables_set)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_etfs_set),
    'total_trade_tables': len(trade_tables_set),
    'common_etfs': len(common_etfs),
    'sample_common': list(common_etfs)[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:8': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}, {'table_name': 'ABEQ'}, {'table_name': 'ABMD'}, {'table_name': 'ACAD'}, {'table_name': 'ACES'}, {'table_name': 'ACIO'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json'}

exec(code, env_args)
