code = """import json

# Read NYSE Arca ETF list
with open('file_storage/functions.query_db:30.json', 'r') as f:
    etf_data = json.load(f)

nyse_arca_symbols = [item['Symbol'] for item in etf_data]
print(f"Total NYSE Arca ETFs in database: {len(nyse_arca_symbols)}")

# Initialize results
etfs_above_200 = []

# List of some major ETFs I can check systematically
major_etfs = ['SPY', 'IVV', 'VOO', 'QQQ', 'DIA', 'IWM', 'GLD', 'SLV', 'EFA', 'EEM', 'VTI', 'VXUS', 'BND', 'AGG']

# Filter to only those in NYSE Arca
nyse_major_etfs = [etf for etf in major_etfs if etf in nyse_arca_symbols]

print(f"Major ETFs on NYSE Arca: {nyse_major_etfs}")
print("(Checking these first as representatives...)")

print('__RESULT__:')
print(json.dumps({'total_nyse_arca_etfs': len(nyse_arca_symbols), 'sample_major_etfs': nyse_major_etfs}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['test'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:22': [], 'var_functions.query_db:26': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}, {'Adj Close': '192.83792114257807', 'Date': '2015-05-18'}, {'Adj Close': '192.8120574951172', 'Date': '2015-06-23'}, {'Adj Close': '192.77456665039065', 'Date': '2015-05-19'}, {'Adj Close': '192.73838806152344', 'Date': '2015-05-22'}, {'Adj Close': '192.67564392089844', 'Date': '2015-06-22'}], 'var_functions.query_db:28': [{'Date': '2015-01-02', 'Open': '112.48999786376952', 'High': '114.8000030517578', 'Low': '112.31999969482422', 'Close': '114.08000183105467', 'Adj Close': '114.08000183105467', 'Volume': '7109600'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'max_close': '125.2300033569336'}], 'var_functions.query_db:34': [{'max_close': '110.42893981933594'}], 'var_functions.query_db:36': [{'max_close': '163.6190185546875'}], 'var_functions.execute_python:38': {'count': 1435}, 'var_functions.query_db:40': [{'Symbol': 'SPY', 'max_close': '193.3121490478516'}], 'var_functions.query_db:42': [{'max_close': '120.37349700927734'}], 'var_functions.execute_python:44': {'total_symbols': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:48': [{'max_close': '193.3121490478516'}], 'var_functions.query_db:50': [{'max_close': '507.2368774414063'}], 'var_functions.query_db:52': [{'Symbol': 'SQQQ', 'Listing Exchange': 'Q'}], 'var_functions.execute_python:54': {'total': 1435, 'checking_now': 100}, 'var_functions.query_db:56': [{'max_close': '125.2300033569336'}], 'var_functions.query_db:58': [{'max_close': '193.5270538330078'}]}

exec(code, env_args)
