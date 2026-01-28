code = """import json

# Load the complete list of NYSE Arca ETF symbols
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Current findings from our spot checks
known_high_etfs = {
    'DUST': 1923.28,
    'JNUG': 451.07,
    'UGL': 46.62,  # below 200
    'GLL': 118.28,  # below 200
    'AGQ': 51.71,   # below 200
    'JDST': 12988.41
}

# Let's continue checking the next batch of likely candidates
next_candidates = [
    'NUGT', 'DUST', 'JNUG', 'JDST',  # Leveraged miners
    'SPXL', 'UPRO', 'TQQQ', 'UDOW',  # Leveraged long
    'SPXS', 'SPXU', 'SQQQ', 'SDOW',  # Leveraged short
    'TNA', 'TZA',  # Small cap leveraged
    'FAS', 'FAZ',  # Financial leveraged
    'ERX', 'ERY',  # Energy leveraged
    'EDC', 'EDZ',  # Emerging markets leveraged
    'TMF', 'TMV',  # Treasury leveraged
    'UGL', 'GLL', 'AGQ', 'ZSL',  # Commodity leveraged
    'UCO', 'SCO',  # Oil leveraged
]

# Find which of these are in our NYSE Arca list
candidates_in_list = [sym for sym in next_candidates if sym in symbols]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'candidates_to_check': candidates_in_list,
    'num_candidates': len(candidates_in_list),
    'known_high_etfs': known_high_etfs
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 38, 'nyse_arca_etfs_sample': 'fil', 'all_tables_type': "<class 'str'>", 'all_tables_length': 37, 'all_tables_sample': 'fil'}, 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_tables_in_db': 2753, 'etfs_with_price_data': 1435, 'sample_etfs': ['CGW', 'EZA', 'AIIQ', 'CORN', 'HDMV', 'MDY', 'VB', 'TIPX', 'EDIV', 'TLH']}, 'var_functions.execute_python:20': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_symbols': ['CMF', 'MOO', 'AVDV', 'RECS', 'AFK', 'IRBO', 'FILL', 'TERM', 'GURU', 'SRLN']}, 'var_functions.query_db:22': [{'Symbol': 'SPY', 'count': '0'}], 'var_functions.query_db:24': [{'Date': '2015-01-02', 'Open': '206.3800048828125', 'High': '206.8800048828125', 'Low': '204.17999267578125', 'Close': '205.42999267578125', 'Adj Close': '185.07107543945312', 'Volume': '121465900'}, {'Date': '2015-01-05', 'Open': '204.1699981689453', 'High': '204.3699951171875', 'Low': '201.3500061035156', 'Close': '201.72000122070312', 'Adj Close': '181.72874450683597', 'Volume': '169632600'}, {'Date': '2015-01-06', 'Open': '202.08999633789065', 'High': '202.72000122070312', 'Low': '198.8600006103516', 'Close': '199.82000732421875', 'Adj Close': '180.01708984375', 'Volume': '209151400'}, {'Date': '2015-01-07', 'Open': '201.4199981689453', 'High': '202.72000122070312', 'Low': '200.8800048828125', 'Close': '202.30999755859372', 'Adj Close': '182.26026916503903', 'Volume': '125346700'}, {'Date': '2015-01-08', 'Open': '204.00999450683597', 'High': '206.16000366210935', 'Low': '203.9900054931641', 'Close': '205.8999938964844', 'Adj Close': '185.49449157714844', 'Volume': '147217800'}], 'var_functions.query_db:26': [{'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}], 'var_functions.execute_python:30': {'total_symbols': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:32': {'stage': 'preparation', 'total_symbols': 1435, 'status': 'ready to query each ETF for 2015 data', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:34': [{'Symbol': 'GLD', 'max_adj_close': '125.2300033569336'}], 'var_functions.execute_python:36': {'total_symbols': 1435, 'candidate_symbols': ['DUST', 'NUGT', 'SPXL', 'SPXS', 'UDOW', 'SDOW', 'UPRO', 'SPXU', 'DDM', 'DXD', 'QLD', 'QID', 'TNA', 'TZA', 'FAS', 'FAZ', 'ERX', 'ERY', 'EDC', 'EDZ', 'TMF', 'TMV', 'UGL', 'GLL', 'AGQ', 'ZSL', 'UCO', 'SCO'], 'num_candidates': 28}, 'var_functions.query_db:38': [{'max_price': '1923.278564453125'}], 'var_functions.query_db:40': [{'max_price': '162.96107482910156'}], 'var_functions.query_db:42': [{'max_price': '22.93797874450684'}], 'var_functions.execute_python:44': {'status': 'starting_queries', 'total_symbols': 1435, 'first_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.execute_python:48': {'batch_size': 50, 'sample_part': 'SELECT AAAU as Symbol, MAX(Adj Close) as max_price FROM AAAU WHERE Date BETWEEN 2015-01-01 AND 2015-12-31', 'batch_query_length': 5763}, 'var_functions.query_db:50': [], 'var_functions.query_db:52': [{'max_price': '1923.278564453125'}], 'var_functions.execute_python:54': {'total_symbols': 1435, 'batches': 48, 'batch_size': 30, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA']}, 'var_functions.query_db:58': [], 'var_functions.execute_python:60': 'file_storage/functions.execute_python:60.json', 'var_functions.query_db:62': [{'max("Adj Close")': '451.0675659179688'}], 'var_functions.query_db:63': [{'max("Adj Close")': '12988.4140625'}], 'var_functions.query_db:64': [{'max("Adj Close")': '51.709999084472656'}], 'var_functions.query_db:65': [{'max("Adj Close")': '46.619998931884766'}], 'var_functions.query_db:66': [{'max("Adj Close")': '118.27999877929688'}]}

exec(code, env_args)
