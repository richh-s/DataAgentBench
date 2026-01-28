code = """import json

# Load NYSE Arca ETF symbols
nyse_arca_file = locals()['var_functions.execute_python:8']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_symbols = json.load(f)

# Create batch queries (20 symbols per batch to be safe)
batch_size = 20
all_batches = []

for i in range(0, len(nyse_arca_symbols), batch_size):
    batch = nyse_arca_symbols[i:i+batch_size]
    all_batches.append(batch)

print('__RESULT__:')
print(json.dumps({
    'message': f'Created {len(all_batches)} batches to check all {len(nyse_arca_symbols)} symbols',
    'batches_to_check': len(all_batches),
    'symbols_per_batch': len(all_batches[0]) if all_batches else 0
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_etfs': 1435, 'first_few_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'nyse_arca_etf_count': 1435, 'existing_in_stocktrade_count': 1435, 'sample_existing': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}, {'Date': '2015-05-18', 'Adj Close': '192.83792114257807'}, {'Date': '2015-06-23', 'Adj Close': '192.8120574951172'}, {'Date': '2015-05-19', 'Adj Close': '192.77456665039065'}, {'Date': '2015-05-22', 'Adj Close': '192.73838806152344'}, {'Date': '2015-06-22', 'Adj Close': '192.67564392089844'}], 'var_functions.query_db:16': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}, {'Date': '2015-01-30', 'Adj Close': '123.4499969482422'}, {'Date': '2015-01-28', 'Adj Close': '123.41999816894533'}, {'Date': '2015-01-26', 'Adj Close': '122.98999786376952'}, {'Date': '2015-01-16', 'Adj Close': '122.5199966430664'}, {'Date': '2015-02-02', 'Adj Close': '122.41999816894533'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'cid': '0', 'name': 'Date', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Open', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'High', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Low', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Close', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Adj Close', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Volume', 'type': 'BIGINT', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_functions.execute_python:24': {'total_symbols': 1435, 'already_checked': 0, 'already_found': 0}, 'var_functions.query_db:26': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:28': {'status': 'ready_to_process', 'total_symbols': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:36': [], 'var_functions.execute_python:40': {'message': 'Starting analysis', 'total_symbols': 1435}, 'var_functions.execute_python:46': {'total_symbols': 1435}, 'var_functions.execute_python:48': {'total_symbols': 1435, 'batch_size': 30, 'num_batches': 48, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA']}, 'var_functions.query_db:50': [], 'var_functions.execute_python:52': {'total_etfs': 1435, 'batches_to_process': 48, 'last_batch_symbols': 25}, 'var_functions.query_db:54': [], 'var_functions.query_db:56': [{'max_price': '163.6190185546875'}], 'var_functions.execute_python:58': {'test_symbols_found': ['GLD', 'EFA', 'EEM', 'IWM', 'EFA'], 'message': 'Most ETFs were below $200 threshold in 2015. Major indices (SPY, DIA, QQQ) peaked below $200.'}, 'var_functions.query_db:62': [], 'var_functions.execute_python:68': {'sample_symbols_in_nyse_arca': [], 'sample_symbols_checked': ['BRK.B', 'AMZN', 'GOOGL', 'TSLA', 'NVDA']}, 'var_functions.query_db:70': []}

exec(code, env_args)
