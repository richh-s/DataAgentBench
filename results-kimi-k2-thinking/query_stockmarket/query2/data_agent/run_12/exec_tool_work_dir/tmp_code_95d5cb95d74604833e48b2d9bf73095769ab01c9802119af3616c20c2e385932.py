code = """import json

# Load NYSE Arca ETFs list
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nyse_arca_etfs = [item['Symbol'] for item in json.load(f)]

# Process first 100 ETFs to see if any had prices > $200 in 2015
# We'll generate the results to be checked via query_db
batch_size = 100
first_batch = nyse_arca_etfs[:batch_size]

print('__RESULT__:')
print(json.dumps(first_batch))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'total_etfs': 1435, 'test_symbols': ['GLD', 'SPY', 'IVV', 'VOO', 'AGG']}, 'var_functions.list_db:20': 'file_storage/functions.list_db:20.json', 'var_functions.execute_python:22': {'nyse_arca_etf_count': 1435, 'tables_in_db': 2753, 'intersection_count': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'Date': '2004-11-18', 'Open': '44.43000030517578', 'High': '44.4900016784668', 'Low': '44.06999969482422', 'Close': '44.380001068115234', 'Adj Close': '44.380001068115234', 'Volume': '5992000'}], 'var_functions.query_db:30': [], 'var_functions.query_db:32': [{'max_adj_close': '193.3121490478516'}], 'var_functions.execute_python:34': {'message': 'Will process 1435 ETFs', 'count': 1435}, 'var_functions.execute_python:36': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}, {'Date': '2015-05-18', 'Adj Close': '192.83792114257807'}, {'Date': '2015-06-23', 'Adj Close': '192.8120574951172'}, {'Date': '2015-05-19', 'Adj Close': '192.77456665039065'}, {'Date': '2015-05-22', 'Adj Close': '192.73838806152344'}, {'Date': '2015-06-22', 'Adj Close': '192.67564392089844'}], 'var_functions.query_db:40': [{'max_price': '110.42893981933594'}], 'var_functions.query_db:42': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:44': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:46': [{'max_price': '163.6190185546875'}]}

exec(code, env_args)
