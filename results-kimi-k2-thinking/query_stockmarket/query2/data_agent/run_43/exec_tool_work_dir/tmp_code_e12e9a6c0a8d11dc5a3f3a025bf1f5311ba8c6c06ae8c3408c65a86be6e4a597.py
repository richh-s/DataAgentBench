code = """import json

# Read NYSE Arca ETFs
with open('file_storage/functions.query_db:26.json', 'r') as f:
    etf_symbols = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in etf_symbols]

# Process first batch of 50 ETFs
batch_size = 50
first_batch = nyse_arca_etfs[:batch_size]

# Build UNION ALL query for the first batch
union_parts = []
for symbol in first_batch:
    union_parts.append(
        f"SELECT '{symbol}' as Symbol, MAX(\"Adj Close\") as max_price "
        f"FROM \"{symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    )

query = " UNION ALL ".join(union_parts)

print('__RESULT__:')
print(json.dumps({
    'query': query,
    'batch_size': len(first_batch),
    'symbols': first_batch
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'value': 'file_storage/functions.query_db:0.json'}, 'var_functions.execute_python:10': {'num_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:12': [], 'var_functions.list_db:14': 'file_storage/functions.list_db:14.json', 'var_functions.query_db:16': [{'Date': '2015-01-02', 'Adj Close': '185.07107543945312'}, {'Date': '2015-01-05', 'Adj Close': '181.72874450683597'}, {'Date': '2015-01-06', 'Adj Close': '180.01708984375'}, {'Date': '2015-01-07', 'Adj Close': '182.26026916503903'}, {'Date': '2015-01-08', 'Adj Close': '185.49449157714844'}, {'Date': '2015-01-09', 'Adj Close': '184.0080108642578'}, {'Date': '2015-01-12', 'Adj Close': '182.56655883789065'}, {'Date': '2015-01-13', 'Adj Close': '182.0530548095703'}, {'Date': '2015-01-14', 'Adj Close': '180.95396423339844'}, {'Date': '2015-01-15', 'Adj Close': '179.29635620117188'}], 'var_functions.execute_python:18': {'count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:20': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:22': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:24': {'total_etfs': 1435, 'first_20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'Symbol': 'FXP', 'max_price': '206.0038299560547'}, {'Symbol': 'DIA', 'max_price': '163.6190185546875'}, {'Symbol': 'EEV', 'max_price': '138.3223114013672'}, {'Symbol': 'GLD', 'max_price': '125.2300033569336'}, {'Symbol': 'EDV', 'max_price': '117.01538848876952'}, {'Symbol': 'QQQ', 'max_price': '110.42893981933594'}], 'var_functions.query_db:30': [{'Symbol': 'UVXY', 'max_price': '81500.0'}, {'Symbol': 'JDST', 'max_price': '12988.4140625'}, {'Symbol': 'DUST', 'max_price': '1923.278564453125'}, {'Symbol': 'SQQQ', 'max_price': '507.2368774414063'}, {'Symbol': 'FXP', 'max_price': '206.0038299560547'}], 'var_functions.execute_python:32': {'message': 'Found 1435 NYSE Arca ETFs', 'count': 1435}, 'var_functions.execute_python:34': {'total_etfs': 1435, 'test_batch_size': 50, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
