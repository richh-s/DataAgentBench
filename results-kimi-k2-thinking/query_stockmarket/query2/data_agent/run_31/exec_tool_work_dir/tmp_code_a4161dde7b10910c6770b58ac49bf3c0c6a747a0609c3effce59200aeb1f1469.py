code = """import json

# Check a few specific ETFs that might have prices above $200 in 2015
# These are either leveraged or priced differently
potential_high_value = [
    'ZROZ',  # 25+ Year Zero Coupon Treasury
    'UPRO',  # 3x S&P 500
    'SPXL',  # 3x S&P 500 (Direxion)
    'TQQQ',  # 3x NASDAQ-100
    'TMF',   # 3x 20+ Year Treasury
    'UDOW',  # 3x Dow Jones
    'UMDD',  # 3x S&P 400 MidCap
    
]

# Check which ones are in our NYSE Arca list
etf_file_path = 'file_storage/functions.query_db:8.json'
with open(etf_file_path, 'r') as f:
    etf_list = json.load(f)

symbols = [item['Symbol'] for item in etf_list]
nyse_arca_set = set(symbols)

candidates = [symbol for symbol in potential_high_value if symbol in nyse_arca_set]

print('__RESULT__:')
print(json.dumps({
    'candidates_found': len(candidates),
    'candidates': candidates,
    'total_nyse_arca_etfs': len(symbols)
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'file_path': 'file_storage/functions.query_db:8.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:16': {'total_symbols': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_nyse_arca_etfs': 1435, 'tables_in_trade_db': 2753, 'available_for_query': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:24': [{'count': '0'}], 'var_functions.query_db:26': [{'count': '0'}], 'var_functions.execute_python:30': {'total_nyse_arca_etfs': 1435, 'high_value_candidates': 25, 'candidates': ['AGG', 'DDM', 'DIA', 'EEM', 'EFA', 'FXE', 'GLD', 'IVV', 'IWM', 'MVV', 'QLD', 'ROM', 'SAA', 'SPXL', 'SPY', 'SSO', 'UPRO', 'URE', 'USO', 'UUP', 'UWM', 'VEA', 'VOO', 'VTI', 'VWO']}, 'var_functions.query_db:36': [{'days_above_200': '0'}], 'var_functions.query_db:38': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:40': {'message': 'Found 1435 NYSE Arca ETFs to check', 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'last_10': ['YYY', 'ZCAN', 'ZDEU', 'ZGBR', 'ZHOK', 'ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}, 'var_functions.query_db:42': [{'Symbol': 'IVV', 'max_price': '193.5270538330078'}, {'Symbol': 'SPY', 'max_price': '193.3121490478516'}, {'Symbol': 'DIA', 'max_price': '163.6190185546875'}, {'Symbol': 'QQQ', 'max_price': '110.42893981933594'}], 'var_functions.query_db:44': [], 'var_functions.query_db:46': [{'Symbol': 'GLD', 'max_price': '125.2300033569336'}, {'Symbol': 'TLT', 'max_price': '121.58584594726562'}, {'Symbol': 'IWM', 'max_price': '120.37349700927734'}, {'Symbol': 'FXE', 'max_price': '118.1999969482422'}, {'Symbol': 'AGG', 'max_price': '98.26229858398438'}, {'Symbol': 'UUP', 'max_price': '25.669574737548828'}, {'Symbol': 'USO', 'max_price': '20.81999969482422'}], 'var_functions.query_db:48': [{'Symbol': 'SSO', 'max_price': '66.95523071289062'}, {'Symbol': 'QLD', 'max_price': '41.19669723510742'}], 'var_functions.execute_python:52': {'total_etfs': 1435, 'first_few': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'last_few': ['ZIG', 'ZJPN', 'ZMLP', 'ZROZ', 'ZSL']}, 'var_functions.query_db:54': [{'symbol': 'SSO', 'days_above_200': '0', 'max_price': 'nan'}], 'var_functions.query_db:56': [{'max_price': '100.54161834716795'}], 'var_functions.execute_python:62': {'total_symbols': 1435, 'message': 'Ready to check price data for all NYSE Arca ETFs in 2015', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
