code = """import json
import os

# Load NYSE Arca ETFs
etfs_file = locals()['var_functions.query_db:5']
with open(etfs_file, 'r') as f:
    etfs_data = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in etfs_data]

# Load tables list
tables_file = locals()['var_functions.list_db:2']
with open(tables_file, 'r') as f:
    available_tables = json.load(f)

# Find ETFs with price data
etfs_with_data = [etf for etf in nyse_arca_etfs if etf in available_tables]

# Check some known large ETFs for 2015 prices
test_etfs = ['SPY', 'IVV', 'VOO', 'VTI', 'DIA', 'QQQ', 'XLG', 'RSP', 'VUG', 'VTV']
test_results = {}

for etf in test_etfs:
    if etf in etfs_with_data:
        test_results[etf] = 'has_data'
    else:
        test_results[etf] = 'no_data'

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_etfs),
    'etfs_with_data_count': len(etfs_with_data),
    'test_etfs_in_database': test_results
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_nyse_arca_etfs': 1435, 'available_etfs_count': 1435, 'sample_available_etfs': ['AOR', 'IBDL', 'SBM', 'IIGD', 'XTL', 'DIV', 'IVV', 'LGLV', 'HEWC', 'URTH']}, 'var_functions.execute_python:10': {'etfs_to_check': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'count': 20}, 'var_functions.execute_python:12': {'total_etfs': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.execute_python:18': {'total_etfs': 1435, 'first_20_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:20': {'nyse_arca_etf_count': 1435, 'sample_checks': ['GLD', 'DIA', 'SPY', 'IVV', 'QQQ', 'VXX', 'VIXY', 'USO', 'UCO', 'SCO', 'BNO', 'DBO', 'USL', 'UHN', 'RJA', 'DBA', 'DBC']}, 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}], 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'Date': '2015-12-01', 'Adj Close': '110.42893981933594'}], 'var_functions.query_db:28': [{'max_close': '193.3121490478516'}], 'var_functions.execute_python:30': {'nyse_arca_etf_count': 1435, 'candidates_to_check': ['DIA', 'SPY', 'IVV', 'VOO', 'VTI', 'VT', 'RSP', 'QQQ', 'XLG'], 'candidates_in_list': ['DIA', 'SPY', 'IVV', 'VOO', 'VTI', 'VT', 'RSP', 'XLG']}, 'var_functions.query_db:32': [{'max_close': '163.6190185546875'}], 'var_functions.query_db:34': [{'max_close': '24.036970138549805'}], 'var_functions.query_db:36': [{'max_close': '193.5270538330078'}], 'var_functions.execute_python:38': {'candidates_to_check': ['XLG', 'SPLV', 'MGC', 'VV', 'VUG', 'VTV', 'VYM', 'MGK', 'MGV']}, 'var_functions.execute_python:40': {'total_nyse_arca_etfs': 1435, 'sample_size': 100, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}}

exec(code, env_args)
