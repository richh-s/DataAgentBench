code = """import json
import os

# Read the list of NYSE Arca ETFs with price data
symbols_file = 'file_storage/functions.execute_python:36.json'
with open(symbols_file, 'r') as f:
    symbols = json.load(f)

print(f'Will check {len(symbols)} NYSE Arca ETFs for 2015 high above $200')
print(f'First 20: {symbols[:20]}')
print(f'Last 20: {symbols[-20:]}')

# Check which of these might be in the price data
tickers_file = 'file_storage/functions.list_db:16.json'
if os.path.exists(tickers_file):
    with open(tickers_file, 'r') as f:
        db_symbols = json.load(f)
else:
    tickers_file2 = 'file_storage/functions.list_db:26.json'
    with open(tickers_file2, 'r') as f:
        db_symbols = json.load(f)

# Find overlap
overlap = set(symbols) & set(db_symbols)
print(f'Actual overlap with price tables: {len(overlap)}')

print('__RESULT__:')
print(json.dumps(list(symbols[:50])))  # Pass manageable list"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX'], 'var_functions.query_db:24': [{'max_adj_close': '193.3121490478516'}], 'var_functions.list_db:26': 'file_storage/functions.list_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'max_price': '125.2300033569336'}], 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': [{'max_price': '24.036970138549805'}], 'var_functions.query_db:40': [{'max_price': '163.6190185546875'}], 'var_functions.query_db:42': [{'max_price': '193.5270538330078'}]}

exec(code, env_args)
