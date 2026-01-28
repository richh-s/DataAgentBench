code = """import json

# Load the NYSE Arca ETF symbols
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Generate a simpler approach - process in batches
print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'first_10_symbols': symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 38, 'nyse_arca_etfs_sample': 'fil', 'all_tables_type': "<class 'str'>", 'all_tables_length': 37, 'all_tables_sample': 'fil'}, 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_tables_in_db': 2753, 'etfs_with_price_data': 1435, 'sample_etfs': ['CGW', 'EZA', 'AIIQ', 'CORN', 'HDMV', 'MDY', 'VB', 'TIPX', 'EDIV', 'TLH']}, 'var_functions.execute_python:20': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_symbols': ['CMF', 'MOO', 'AVDV', 'RECS', 'AFK', 'IRBO', 'FILL', 'TERM', 'GURU', 'SRLN']}, 'var_functions.query_db:22': [{'Symbol': 'SPY', 'count': '0'}], 'var_functions.query_db:24': [{'Date': '2015-01-02', 'Open': '206.3800048828125', 'High': '206.8800048828125', 'Low': '204.17999267578125', 'Close': '205.42999267578125', 'Adj Close': '185.07107543945312', 'Volume': '121465900'}, {'Date': '2015-01-05', 'Open': '204.1699981689453', 'High': '204.3699951171875', 'Low': '201.3500061035156', 'Close': '201.72000122070312', 'Adj Close': '181.72874450683597', 'Volume': '169632600'}, {'Date': '2015-01-06', 'Open': '202.08999633789065', 'High': '202.72000122070312', 'Low': '198.8600006103516', 'Close': '199.82000732421875', 'Adj Close': '180.01708984375', 'Volume': '209151400'}, {'Date': '2015-01-07', 'Open': '201.4199981689453', 'High': '202.72000122070312', 'Low': '200.8800048828125', 'Close': '202.30999755859372', 'Adj Close': '182.26026916503903', 'Volume': '125346700'}, {'Date': '2015-01-08', 'Open': '204.00999450683597', 'High': '206.16000366210935', 'Low': '203.9900054931641', 'Close': '205.8999938964844', 'Adj Close': '185.49449157714844', 'Volume': '147217800'}], 'var_functions.query_db:26': [{'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}]}

exec(code, env_args)
