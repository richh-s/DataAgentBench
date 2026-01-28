code = """import json

# Get NYSE Arca ETFs
etfs_file = locals()['var_functions.query_db:5']
with open(etfs_file, 'r') as f:
    etfs_data = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in etfs_data]

# Check a few potentially high-priced ETFs
high_price_candidates = ['DIA', 'SPY', 'IVV', 'VOO', 'VTI', 'VT', 'RSP', 'QQQ', 'XLG']

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_etfs),
    'candidates_to_check': high_price_candidates,
    'candidates_in_list': [etf for etf in high_price_candidates if etf in nyse_arca_etfs]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_nyse_arca_etfs': 1435, 'available_etfs_count': 1435, 'sample_available_etfs': ['AOR', 'IBDL', 'SBM', 'IIGD', 'XTL', 'DIV', 'IVV', 'LGLV', 'HEWC', 'URTH']}, 'var_functions.execute_python:10': {'etfs_to_check': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'count': 20}, 'var_functions.execute_python:12': {'total_etfs': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:14': [], 'var_functions.query_db:16': [], 'var_functions.execute_python:18': {'total_etfs': 1435, 'first_20_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:20': {'nyse_arca_etf_count': 1435, 'sample_checks': ['GLD', 'DIA', 'SPY', 'IVV', 'QQQ', 'VXX', 'VIXY', 'USO', 'UCO', 'SCO', 'BNO', 'DBO', 'USL', 'UHN', 'RJA', 'DBA', 'DBC']}, 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}], 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'Date': '2015-12-01', 'Adj Close': '110.42893981933594'}], 'var_functions.query_db:28': [{'max_close': '193.3121490478516'}]}

exec(code, env_args)
