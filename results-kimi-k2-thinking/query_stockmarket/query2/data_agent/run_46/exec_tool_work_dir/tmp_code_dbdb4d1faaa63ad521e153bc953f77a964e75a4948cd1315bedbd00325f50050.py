code = """import json

# Get the NYSE Arca ETFs list from the previous storage
etfs_file = locals()['var_functions.query_db:5']

# Load the ETF symbols
with open(etfs_file, 'r') as f:
    etfs_data = json.load(f)

nyse_arca_etf_symbols = [item['Symbol'] for item in etfs_data]

print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(nyse_arca_etf_symbols),
    'test_check_symbols': nyse_arca_etf_symbols[:50]  # Show first 50
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_nyse_arca_etfs': 1435, 'available_etfs_count': 1435, 'sample_available_etfs': ['AOR', 'IBDL', 'SBM', 'IIGD', 'XTL', 'DIV', 'IVV', 'LGLV', 'HEWC', 'URTH']}, 'var_functions.execute_python:10': {'etfs_to_check': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'count': 20}, 'var_functions.execute_python:12': {'total_etfs': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.execute_python:18': {'total_etfs': 1435, 'first_20_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:20': {'nyse_arca_etf_count': 1435, 'sample_checks': ['GLD', 'DIA', 'SPY', 'IVV', 'QQQ', 'VXX', 'VIXY', 'USO', 'UCO', 'SCO', 'BNO', 'DBO', 'USL', 'UHN', 'RJA', 'DBA', 'DBC']}, 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}], 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'Date': '2015-12-01', 'Adj Close': '110.42893981933594'}], 'var_functions.query_db:28': [{'max_close': '193.3121490478516'}], 'var_functions.execute_python:30': {'nyse_arca_etf_count': 1435, 'candidates_to_check': ['DIA', 'SPY', 'IVV', 'VOO', 'VTI', 'VT', 'RSP', 'QQQ', 'XLG'], 'candidates_in_list': ['DIA', 'SPY', 'IVV', 'VOO', 'VTI', 'VT', 'RSP', 'XLG']}, 'var_functions.query_db:32': [{'max_close': '163.6190185546875'}], 'var_functions.query_db:34': [{'max_close': '24.036970138549805'}], 'var_functions.query_db:36': [{'max_close': '193.5270538330078'}], 'var_functions.execute_python:38': {'candidates_to_check': ['XLG', 'SPLV', 'MGC', 'VV', 'VUG', 'VTV', 'VYM', 'MGK', 'MGV']}, 'var_functions.execute_python:40': {'total_nyse_arca_etfs': 1435, 'sample_size': 100, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:42': {'total_nyse_arca_etfs': 1435, 'etfs_with_data_count': 1435, 'test_etfs_in_database': {'SPY': 'has_data', 'IVV': 'has_data', 'VOO': 'has_data', 'VTI': 'has_data', 'DIA': 'has_data', 'QQQ': 'no_data', 'XLG': 'has_data', 'RSP': 'has_data', 'VUG': 'has_data', 'VTV': 'has_data'}}}

exec(code, env_args)
