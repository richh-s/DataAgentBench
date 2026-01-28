code = """import json

# Read ETF symbols from NYSE Arca
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_symbols = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in etf_symbols]

print('__RESULT__:')
print(json.dumps({'total_etfs': len(nyse_arca_etfs), 'first_20': nyse_arca_etfs[:20]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'value': 'file_storage/functions.query_db:0.json'}, 'var_functions.execute_python:10': {'num_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.list_db:14': 'file_storage/functions.list_db:14.json', 'var_functions.query_db:16': [{'Date': '2015-01-02', 'Adj Close': '185.07107543945312'}, {'Date': '2015-01-05', 'Adj Close': '181.72874450683597'}, {'Date': '2015-01-06', 'Adj Close': '180.01708984375'}, {'Date': '2015-01-07', 'Adj Close': '182.26026916503903'}, {'Date': '2015-01-08', 'Adj Close': '185.49449157714844'}, {'Date': '2015-01-09', 'Adj Close': '184.0080108642578'}, {'Date': '2015-01-12', 'Adj Close': '182.56655883789065'}, {'Date': '2015-01-13', 'Adj Close': '182.0530548095703'}, {'Date': '2015-01-14', 'Adj Close': '180.95396423339844'}, {'Date': '2015-01-15', 'Adj Close': '179.29635620117188'}], 'var_functions.execute_python:18': {'count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:20': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:22': [{'max_price': '193.3121490478516'}]}

exec(code, env_args)
