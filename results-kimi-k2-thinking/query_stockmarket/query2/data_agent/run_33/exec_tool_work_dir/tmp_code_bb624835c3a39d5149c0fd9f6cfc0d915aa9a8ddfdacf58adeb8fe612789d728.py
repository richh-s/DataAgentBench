code = """import json

# Read NYSE Arca ETFs
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nyse_arca_list = json.load(f)

# Get symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_list}

# Read all tables in stocktrade_database
with open('file_storage/functions.query_db:26.json', 'r') as f:
    all_tables = json.load(f)

# Get all table names
all_table_names = {table['name'] for table in all_tables}

# Find ETFs that are both on NYSE Arca and have data files
target_etfs = sorted(nyse_arca_symbols.intersection(all_table_names))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'tables_in_db': len(all_table_names),
    'common_etfs': len(target_etfs),
    'first_20': target_etfs[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': [{'max_price': '163.6190185546875'}], 'var_functions.execute_python:36': {'total_nyse_arca_etfs': 1435, 'total_tables': 2753, 'common_etfs_to_check': 1435, 'checking_symbols': ['SPY', 'DIA', 'IVV', 'VOO', 'SSO', 'QLD', 'IVV', 'URE', 'RWL', 'USDU', 'UUP', 'FXE']}, 'var_functions.query_db:38': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:40': {'nyse_arca_etfs': 1435, 'total_tables': 2753, 'valid_etfs_to_check': 1435, 'sample_valid_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:42': [{'Symbol': 'QQQ', 'max_price': '110.42893981933594'}, {'Symbol': 'QLD', 'max_price': '41.19669723510742'}, {'Symbol': 'IVV', 'max_price': '193.5270538330078'}, {'Symbol': 'SSO', 'max_price': '66.95523071289062'}, {'Symbol': 'VOO', 'max_price': '177.17626953125'}], 'var_functions.query_db:44': [{'Symbol': 'DIA', 'max_price': 'nan'}], 'var_functions.query_db:46': [{'Symbol': 'GLD', 'max_price': '125.2300033569336'}], 'var_functions.query_db:50': [{'Symbol': 'TQQQ', 'max_price': '21.189502716064453'}], 'var_functions.query_db:52': [{'Symbol': 'UPRO', 'max_price': '24.036970138549805'}], 'var_functions.execute_python:54': {'total_nyse_arca_etfs': 1435, 'total_tables_in_db': 2753, 'etfs_with_data': 1435, 'sample_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:58': [{'symbol': 'SPY', 'max_price': 'nan'}]}

exec(code, env_args)
