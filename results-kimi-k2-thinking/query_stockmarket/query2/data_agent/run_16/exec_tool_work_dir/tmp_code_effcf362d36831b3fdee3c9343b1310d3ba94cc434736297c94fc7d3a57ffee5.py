code = """import json

# Get the file paths
nyse_arca_file = locals()['var_functions.query_db:0']

with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

symbols = [item['Symbol'] for item in nyse_arca_etfs]

print('__RESULT__:')
print(json.dumps({
    'count': len(symbols),
    'first_10': symbols[:10],
    'last_10': symbols[-10:]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:9': {'total_nyse_arca_etfs': 1435, 'available_trade_tables': 2753, 'intersection_size': 1435, 'sample_symbols': ['XRT', 'SPLB', 'XSLV', 'DPST', 'EJUL', 'SDOG', 'EGPT', 'AIEQ', 'DTN', 'FXH']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY'], 'var_functions.query_db:12': [{'Adj Close': '193.3121490478516'}], 'var_functions.query_db:14': [{'Adj Close': '125.2300033569336'}]}

exec(code, env_args)
