code = """import json
import time

# Get NYSE Arca ETFs from stockinfo
result_key = 'var_functions.query_db:0'
etf_data = locals()[result_key]

if isinstance(etf_data, str):
    with open(etf_data, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_data

# Extract symbols
nyse_arca_symbols = [item['Symbol'] for item in nyse_arca_etfs]

# Get all available trade tables
result_key2 = 'var_functions.list_db:6'
all_tickers_data = locals()[result_key2]

if isinstance(all_tickers_data, str):
    with open(all_tickers_data, 'r') as f:
        all_tickers = json.load(f)
else:
    all_tickers = all_tickers_data

# Find intersection
etfs_with_data = sorted(list(set(nyse_arca_symbols) & set(all_tickers)))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_trade_tables': len(all_tickers),
    'etfs_with_trade_data': len(etfs_with_data),
    'first_10': etfs_with_data[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': 'Found 2753 tickers total', 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_tickers_in_trade_db': 2753, 'etfs_with_data': 1435}, 'var_functions.execute_python:14': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:16': [{'Date': '2015-01-30', 'Open': '112.3499984741211', 'High': '112.5199966430664', 'Low': '112.23999786376952', 'Close': '112.37999725341795', 'Adj Close': '98.26229858398438', 'Volume': '6252800'}, {'Date': '2015-02-02', 'Open': '112.05999755859376', 'High': '112.2300033569336', 'Low': '112.0', 'Close': '112.1999969482422', 'Adj Close': '98.25880432128906', 'Volume': '2792100'}, {'Date': '2015-04-17', 'Open': '111.52999877929688', 'High': '111.8000030517578', 'Low': '111.45999908447266', 'Close': '111.66999816894533', 'Adj Close': '98.14436340332033', 'Volume': '1274300'}, {'Date': '2015-04-15', 'Open': '111.66000366210938', 'High': '111.70999908447266', 'Low': '111.5500030517578', 'Close': '111.63999938964844', 'Adj Close': '98.11800384521484', 'Volume': '1296800'}, {'Date': '2015-04-20', 'Open': '111.66999816894533', 'High': '111.7300033569336', 'Low': '111.47000122070312', 'Close': '111.58999633789062', 'Adj Close': '98.07405853271484', 'Volume': '1289400'}], 'var_functions.execute_python:18': {'nyse_arca_etf_count': 1435, 'available_tickers_count': 2753, 'overlap_count': 1435, 'sample_symbols': ['GMF', 'LMLB', 'JKJ', 'PFFD', 'SLYV', 'DOL', 'FLAG', 'RINF', 'HACK', 'TAXF']}, 'var_functions.execute_python:20': 'Total NYSE Arca ETFs to check: 1435', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.execute_python:24': 'Processing 1435 NYSE Arca ETFs', 'var_functions.execute_python:26': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY'], 'var_functions.query_db:28': [{'max_adj_close': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.query_db:34': [{'max_adj_close': '24.036970138549805'}], 'var_functions.execute_python:36': {'total_to_check': 1435, 'first_20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:38': [{'max_adj_close': '193.3121490478516'}]}

exec(code, env_args)
