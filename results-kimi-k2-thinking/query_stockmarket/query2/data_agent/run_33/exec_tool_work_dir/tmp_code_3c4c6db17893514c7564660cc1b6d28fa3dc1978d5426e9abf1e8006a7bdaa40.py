code = """import json

# Read the NYSE Arca ETF list
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nyse_arca_etfs = json.load(f)

# Get symbols as a set
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}

# ETFs found with price > $200
found_etfs = ['GUSH', 'ERX', 'SQQQ', 'TZA', 'FAZ', 'DUST']

# Check which ones are actually NYSE Arca ETFs
nyse_arca_qualifying = []
for symbol in found_etfs:
    if symbol in nyse_arca_symbols:
        nyse_arca_qualifying.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'all_found_etfs': found_etfs,
    'nyse_arca_etfs': nyse_arca_qualifying,
    'total_nyse_arca_etfs_with_high_prices': len(nyse_arca_qualifying)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': [{'max_price': '163.6190185546875'}], 'var_functions.execute_python:36': {'total_nyse_arca_etfs': 1435, 'total_tables': 2753, 'common_etfs_to_check': 1435, 'checking_symbols': ['SPY', 'DIA', 'IVV', 'VOO', 'SSO', 'QLD', 'IVV', 'URE', 'RWL', 'USDU', 'UUP', 'FXE']}, 'var_functions.query_db:38': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:40': {'nyse_arca_etfs': 1435, 'total_tables': 2753, 'valid_etfs_to_check': 1435, 'sample_valid_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:42': [{'Symbol': 'QQQ', 'max_price': '110.42893981933594'}, {'Symbol': 'QLD', 'max_price': '41.19669723510742'}, {'Symbol': 'IVV', 'max_price': '193.5270538330078'}, {'Symbol': 'SSO', 'max_price': '66.95523071289062'}, {'Symbol': 'VOO', 'max_price': '177.17626953125'}], 'var_functions.query_db:44': [{'Symbol': 'DIA', 'max_price': 'nan'}], 'var_functions.query_db:46': [{'Symbol': 'GLD', 'max_price': '125.2300033569336'}], 'var_functions.query_db:50': [{'Symbol': 'TQQQ', 'max_price': '21.189502716064453'}], 'var_functions.query_db:52': [{'Symbol': 'UPRO', 'max_price': '24.036970138549805'}], 'var_functions.execute_python:54': {'total_nyse_arca_etfs': 1435, 'total_tables_in_db': 2753, 'etfs_with_data': 1435, 'sample_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:58': [{'symbol': 'SPY', 'max_price': 'nan'}], 'var_functions.execute_python:60': {'total_nyse_arca_etfs': 1435, 'tables_in_db': 2753, 'common_etfs': 1435, 'first_20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:62': [{'symbol': 'IWM', 'max_price': '120.37349700927734'}], 'var_functions.execute_python:66': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:68': [{'Symbol': 'GUSH', 'max_adj_close': '78699.21875'}, {'Symbol': 'ERX', 'max_adj_close': '645.1613159179688'}, {'Symbol': 'SQQQ', 'max_adj_close': '507.2368774414063'}, {'Symbol': 'TZA', 'max_adj_close': '272.6275939941406'}, {'Symbol': 'FAZ', 'max_adj_close': '288.5361328125'}, {'Symbol': 'DUST', 'max_adj_close': '1923.278564453125'}]}

exec(code, env_args)
