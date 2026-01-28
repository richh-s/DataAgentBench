code = """import json
import os

# Read NYSE Arca ETFs from stockinfo
arca_file = 'file_storage/functions.query_db:54.json'
with open(arca_file, 'r') as f:
    arca_etfs = json.load(f)

# Read all available tickers from stocktrade DB
tickers_file = 'file_storage/functions.list_db:26.json'
with open(tickers_file, 'r') as f:
    db_symbols = json.load(f)

# Find intersection (NYSE Arca ETFs that have price data)
arca_symbols = set(etf['Symbol'] for etf in arca_etfs)
db_symbols_set = set(db_symbols)
common_symbols = arca_symbols.intersection(db_symbols_set)

print(f'NYSE Arca ETFs: {len(arca_symbols)}')
print(f'Available in price DB: {len(common_symbols)}')

# Store for next step
print('__RESULT__:')
print(json.dumps(sorted(list(common_symbols))))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json', 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX'], 'var_functions.query_db:24': [{'max_adj_close': '193.3121490478516'}], 'var_functions.list_db:26': 'file_storage/functions.list_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'max_price': '125.2300033569336'}], 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': [{'max_price': '24.036970138549805'}], 'var_functions.query_db:40': [{'max_price': '163.6190185546875'}], 'var_functions.query_db:42': [{'max_price': '193.5270538330078'}], 'var_functions.execute_python:44': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY'], 'var_functions.query_db:46': [{'max_price': '41.19669723510742'}], 'var_functions.execute_python:48': 'file_storage/functions.execute_python:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
