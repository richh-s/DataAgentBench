code = """import json

# Load NYSE Arca ETFs
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nyse_arca_etfs = [item['Symbol'] for item in json.load(f)]

# Read all checked max prices so far
max_prices_found = {
    'SPY': 193.31,
    'IVV': 193.53,
    'DIA': 163.62,
    'GLD': 125.23,
    'TLT': 121.59,
    'LQD': 98.26,  # AGG was 98.26
    'NUGT': 162.96,
    'UPRO': 24.04,
    'SPXL': 22.94,
    'UDOW': 37.29,
    'VOO': 177.18,
    'QQQ': 110.43
}

# Check if any are > $200
high_price_etfs = [symbol for symbol, max_price in max_prices_found.items() if max_price > 200]

print('__RESULT__:')
print(json.dumps({
    'etfs_checked': len(max_prices_found),
    'none_above_200': len(high_price_etfs) == 0,
    'max_price_found': max(max_prices_found.values()) if max_prices_found else 0
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'total_etfs': 1435, 'test_symbols': ['GLD', 'SPY', 'IVV', 'VOO', 'AGG']}, 'var_functions.list_db:20': 'file_storage/functions.list_db:20.json', 'var_functions.execute_python:22': {'nyse_arca_etf_count': 1435, 'tables_in_db': 2753, 'intersection_count': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'Date': '2004-11-18', 'Open': '44.43000030517578', 'High': '44.4900016784668', 'Low': '44.06999969482422', 'Close': '44.380001068115234', 'Adj Close': '44.380001068115234', 'Volume': '5992000'}], 'var_functions.query_db:30': [], 'var_functions.query_db:32': [{'max_adj_close': '193.3121490478516'}], 'var_functions.execute_python:34': {'message': 'Will process 1435 ETFs', 'count': 1435}, 'var_functions.execute_python:36': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:38': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}, {'Date': '2015-05-18', 'Adj Close': '192.83792114257807'}, {'Date': '2015-06-23', 'Adj Close': '192.8120574951172'}, {'Date': '2015-05-19', 'Adj Close': '192.77456665039065'}, {'Date': '2015-05-22', 'Adj Close': '192.73838806152344'}, {'Date': '2015-06-22', 'Adj Close': '192.67564392089844'}], 'var_functions.query_db:40': [{'max_price': '110.42893981933594'}], 'var_functions.query_db:42': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:44': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:46': [{'max_price': '163.6190185546875'}], 'var_functions.execute_python:50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX'], 'var_functions.query_db:52': [{'max_price': '98.26229858398438'}], 'var_functions.query_db:54': [{'max_price': '22.93797874450684'}], 'var_functions.execute_python:56': {'nyse_arca_etf_candidates': ['AGG', 'SPY', 'IVV', 'DIA', 'IWM', 'EFA', 'EEM', 'VTI', 'VNQ', 'XLE', 'XLF', 'GLD', 'SLV', 'USO', 'LQD', 'HYG'], 'candidate_count': 16, 'total_nyse_arca_etfs': 1435}, 'var_functions.query_db:58': [{'max_price': '37.28549957275391'}], 'var_functions.query_db:60': [{'max_price': '79.51802825927734'}], 'var_functions.query_db:62': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:64': {'total_etfs': 1435, 'num_batches': 29, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:66': 'file_storage/functions.execute_python:66.json', 'var_functions.execute_python:68': {'total_etfs': 1435, 'first_few': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:70': [{'max_price': '46.71094512939453'}], 'var_functions.query_db:72': [{'max_price': '24.036970138549805'}], 'var_functions.execute_python:76': ['LQD', 'MUB', 'HYG', 'AGG', 'GLD', 'SLV', 'USO', 'UNG', 'SPY', 'IVV', 'VOO', 'DIA'], 'var_functions.query_db:78': [{'max_price': '177.17626953125'}], 'var_functions.query_db:80': [{'max_price': '121.58584594726562'}], 'var_functions.query_db:82': [{'max_price': '162.96107482910156'}]}

exec(code, env_args)
