code = """import json
import os

# Load list of all tables in stocktrade_database (from earlier list_db)
tables_file = locals().get('var_functions.list_db:5')
with open(tables_file, 'r') as f:
    all_tables = json.load(f)

# Load NYSE Arca ETFs list
symbols_file = locals().get('var_functions.query_db:24')
with open(symbols_file, 'r') as f:
    etf_list = json.load(f)
nyse_arca_etfs = [item['Symbol'] for item in etf_list]

# Intersect with tables
valid_etfs = [sym for sym in nyse_arca_etfs if sym in all_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'tables_available': len(all_tables),
    'valid_etfs': len(valid_etfs),
    'sample_valid': valid_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 1435, 'sample': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_symbols': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'num_batches': 29, 'batch_size': 50, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_etfs': 1435, 'batch_size': 100, 'num_batches': 15, 'first_batch_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.execute_python:28': {'total_nyse_arca_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:34': [], 'var_functions.query_db:36': [], 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}, {'Date': '2015-01-30', 'Adj Close': '123.4499969482422'}, {'Date': '2015-01-28', 'Adj Close': '123.41999816894533'}, {'Date': '2015-01-26', 'Adj Close': '122.98999786376952'}, {'Date': '2015-01-16', 'Adj Close': '122.5199966430664'}, {'Date': '2015-02-02', 'Adj Close': '122.41999816894533'}]}

exec(code, env_args)
