code = """import json

# Read NYSE Arca ETFs
nyse_arca_file = locals()['var_functions.query_db:10']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)

etf_symbols = [item['Symbol'] for item in nyse_arca_data]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(etf_symbols),
    'first_50_symbols': etf_symbols[:50]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'count': 38, 'sample': 'file_stora', 'first_record': 'f'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:18': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 39, 'available_tickers_type': "<class 'str'>", 'available_tickers_length': 38, 'sample_nyse_arca': 'Not a list', 'sample_tickers': 'Not a list'}, 'var_functions.execute_python:20': {'nyse_arca_etfs_count': 1435, 'available_tickers_count': 2753, 'sample_nyse_arca': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'sample_tickers': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}, 'var_functions.execute_python:24': {'total_nyse_arca_etfs': 1435, 'total_available_tickers': 2753, 'available_nyse_arca_etfs': 1435, 'sample_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:26': {'message': 'Ready to query each ETF for 2015 price data', 'total_etfs_to_check': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:28': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:30': [{'max_price': '193.3121490478516'}]}

exec(code, env_args)
