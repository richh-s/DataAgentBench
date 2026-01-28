code = """import json

# Get the ETF list
etf_data = locals()['var_functions.execute_python:22']
if isinstance(etf_data, str) and etf_data.endswith('.json'):
    with open(etf_data, 'r') as f:
        etf_info = json.load(f)
else:
    etf_info = etf_data

etf_symbols = etf_info['etfs']

# Check if SPY is in the list
has_spy = 'SPY' in etf_symbols
has_ivv = 'IVV' in etf_symbols
has_upro = 'UPRO' in etf_symbols
has_sso = 'SSO' in etf_symbols

print("__RESULT__:")
print(json.dumps({
    "SPY_available": has_spy,
    "IVV_available": has_ivv,
    "UPRO_available": has_upro,
    "SSO_available": has_sso,
    "total_etfs": len(etf_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_arca_etfs': 1435, 'available_in_stocktrade': 1435, 'sample_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'Date': '2015-01-02', 'Open': '37.25', 'High': '37.25', 'Low': '36.63999938964844', 'Close': '36.63999938964844', 'Adj Close': '35.3997688293457', 'Volume': '2000'}, {'Date': '2015-01-05', 'Open': '36.130001068115234', 'High': '36.43999862670898', 'Low': '36.130001068115234', 'Close': '36.18999862670898', 'Adj Close': '34.96500015258789', 'Volume': '600'}, {'Date': '2015-01-06', 'Open': '35.56999969482422', 'High': '35.88999938964844', 'Low': '35.560001373291016', 'Close': '35.88999938964844', 'Adj Close': '34.6751594543457', 'Volume': '600'}, {'Date': '2015-01-07', 'Open': '35.88999938964844', 'High': '35.88999938964844', 'Low': '35.88999938964844', 'Close': '35.88999938964844', 'Adj Close': '34.6751594543457', 'Volume': '0'}, {'Date': '2015-01-08', 'Open': '36.72999954223633', 'High': '36.79999923706055', 'Low': '36.45000076293945', 'Close': '36.45000076293945', 'Adj Close': '35.21620559692383', 'Volume': '1100'}], 'var_functions.execute_python:12': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.execute_python:14': {'message': 'Found 1435 NYSE Arca ETFs', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'etf_count': 1435, 'message': 'Ready to process 1435 NYSE Arca ETFs'}, 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': [{'max_adj_close': '193.3121490478516'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': [{'max_adj_close': '125.2300033569336'}], 'var_functions.execute_python:26': {'message': 'Found 1435 NYSE Arca ETFs', 'high_value_candidates_in_list': ['SPY', 'IVV', 'VOO', 'DIA', 'IWM', 'EFA', 'EEM', 'GLD', 'SLV', 'USO']}, 'var_functions.execute_python:30': {'total_etfs': 1435, 'sample_test_symbols': ['SPY', 'IVV', 'VOO', 'QQQ', 'DIA', 'IWM', 'EFA', 'TLT', 'GLD']}, 'var_functions.query_db:32': [{'max_adj_close': '193.5270538330078'}], 'var_functions.query_db:34': [{'max_adj_close': '110.42893981933594'}], 'var_functions.query_db:36': [{'max_adj_close': '163.6190185546875'}]}

exec(code, env_args)
