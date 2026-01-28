code = """import json

# Get the result keys
spy_result = locals()['var_functions.query_db:40']
dia_result = locals()['var_functions.query_db:41']
qqq_result = locals()['var_functions.query_db:42']
iwm_result = locals()['var_functions.query_db:43']

# Extract max prices
spy_max = float(spy_result[0]['max_price'])
dia_max = float(dia_result[0]['max_price'])
qqq_max = float(qqq_result[0]['max_price'])
iwm_max = float(iwm_result[0]['max_price'])

print('__RESULT__:')
print(json.dumps({
    'SPY_max_2015': spy_max,
    'DIA_max_2015': dia_max,
    'QQQ_max_2015': qqq_max,
    'IWM_max_2015': iwm_max,
    'over_200': []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'count': 38, 'sample': 'file_stora', 'first_record': 'f'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:18': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 39, 'available_tickers_type': "<class 'str'>", 'available_tickers_length': 38, 'sample_nyse_arca': 'Not a list', 'sample_tickers': 'Not a list'}, 'var_functions.execute_python:20': {'nyse_arca_etfs_count': 1435, 'available_tickers_count': 2753, 'sample_nyse_arca': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'sample_tickers': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}, 'var_functions.execute_python:24': {'total_nyse_arca_etfs': 1435, 'total_available_tickers': 2753, 'available_nyse_arca_etfs': 1435, 'sample_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:26': {'message': 'Ready to query each ETF for 2015 price data', 'total_etfs_to_check': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:28': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:30': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:32': {'total_nyse_arca_etfs': 1435, 'first_50_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:34': 'file_storage/functions.execute_python:34.json', 'var_functions.execute_python:36': {'all_nyse_arca_etfs': 1435, 'likely_candidates_total': 10, 'filtered_to_nyse_arca': 8, 'candidates_to_check': ['SPY', 'DIA', 'IWM', 'GLD', 'EFA', 'EEM', 'HYG', 'VGK']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'max_price': '193.3121490478516'}], 'var_functions.query_db:41': [{'max_price': '163.6190185546875'}], 'var_functions.query_db:42': [{'max_price': '110.42893981933594'}], 'var_functions.query_db:43': [{'max_price': '120.37349700927734'}]}

exec(code, env_args)
