code = """import json

# Load NYSE Arca ETF symbols
nyse_arca_file = locals()['var_functions.query_db:10']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)

nyse_arca_symbols = [item['Symbol'] for item in nyse_arca_data]

# Check high-priced ETFs we've found
high_price_etfs = []

# Check JNUG
jnug_result = locals()['var_functions.query_db:127']
jnug_max = float(jnug_result[0]['max_price'])
if 'JNUG' in nyse_arca_symbols and jnug_max > 200:
    high_price_etfs.append({'symbol': 'JNUG', 'max_price': jnug_max})

# Check JDST
jdst_result = locals()['var_functions.query_db:139']
jdst_max = float(jdst_result[0]['max_price'])
if 'JDST' in nyse_arca_symbols and jdst_max > 200:
    high_price_etfs.append({'symbol': 'JDST', 'max_price': jdst_max})

# Check DUST
dust_result = locals()['var_functions.query_db:138']
dust_max = float(dust_result[0]['max_price'])
if 'DUST' in nyse_arca_symbols and dust_max > 200:
    high_price_etfs.append({'symbol': 'DUST', 'max_price': dust_max})

print('__RESULT__:')
print(json.dumps({
    'high_price_etf_count': len(high_price_etfs),
    'high_price_etfs': high_price_etfs,
    'all_are_nyse_arca': all(etf['symbol'] in nyse_arca_symbols for etf in high_price_etfs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'count': 38, 'sample': 'file_stora', 'first_record': 'f'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:18': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 39, 'available_tickers_type': "<class 'str'>", 'available_tickers_length': 38, 'sample_nyse_arca': 'Not a list', 'sample_tickers': 'Not a list'}, 'var_functions.execute_python:20': {'nyse_arca_etfs_count': 1435, 'available_tickers_count': 2753, 'sample_nyse_arca': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'sample_tickers': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}, 'var_functions.execute_python:24': {'total_nyse_arca_etfs': 1435, 'total_available_tickers': 2753, 'available_nyse_arca_etfs': 1435, 'sample_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:26': {'message': 'Ready to query each ETF for 2015 price data', 'total_etfs_to_check': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:28': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:30': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:32': {'total_nyse_arca_etfs': 1435, 'first_50_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:34': 'file_storage/functions.execute_python:34.json', 'var_functions.execute_python:36': {'all_nyse_arca_etfs': 1435, 'likely_candidates_total': 10, 'filtered_to_nyse_arca': 8, 'candidates_to_check': ['SPY', 'DIA', 'IWM', 'GLD', 'EFA', 'EEM', 'HYG', 'VGK']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [{'max_price': '193.3121490478516'}], 'var_functions.query_db:41': [{'max_price': '163.6190185546875'}], 'var_functions.query_db:42': [{'max_price': '110.42893981933594'}], 'var_functions.query_db:43': [{'max_price': '120.37349700927734'}], 'var_functions.execute_python:48': {'SPY_max_2015': 193.3121490478516, 'DIA_max_2015': 163.6190185546875, 'QQQ_max_2015': 110.42893981933594, 'IWM_max_2015': 120.37349700927734, 'over_200': []}, 'var_functions.query_db:50': [{'max_price': '37.28549957275391'}], 'var_functions.query_db:51': [{'max_price': '24.036970138549805'}], 'var_functions.query_db:52': [{'max_price': '21.189502716064453'}], 'var_functions.query_db:53': [{'max_price': '46.619998931884766'}], 'var_functions.query_db:58': [{'max_price': '121.58584594726562'}], 'var_functions.query_db:59': [{'max_price': '99.8505401611328'}], 'var_functions.query_db:60': [{'max_price': '70.25736999511719'}], 'var_functions.query_db:61': [{'max_price': '89.62258911132812'}], 'var_functions.query_db:69': [{'max_price': '22.93797874450684'}], 'var_functions.query_db:70': [{'max_price': '119.74252319335938'}], 'var_functions.query_db:71': [{'max_price': '35.73018264770508'}], 'var_functions.query_db:72': [{'max_price': '97.26858520507812'}], 'var_functions.query_db:76': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:77': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:78': [{'max_price': '100.54161834716795'}], 'var_functions.query_db:79': [{'max_price': '36.54500198364258'}], 'var_functions.query_db:84': [{'max_price': '98.26229858398438'}], 'var_functions.query_db:85': [{'max_price': '73.04174041748047'}], 'var_functions.query_db:86': [{'max_price': '46.62751388549805'}], 'var_functions.query_db:87': [{'max_price': '71.3005142211914'}], 'var_functions.query_db:92': [{'max_price': '22.22186088562012'}], 'var_functions.query_db:93': [{'max_price': '35.013790130615234'}], 'var_functions.query_db:94': [{'max_price': '68.05343627929688'}], 'var_functions.query_db:95': [{'max_price': '14.538848876953123'}], 'var_functions.query_db:100': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}], 'var_functions.query_db:101': [{'max_price': '33.38571548461914'}], 'var_functions.query_db:102': [{'max_price': '59.14651870727539'}], 'var_functions.query_db:103': [{'max_price': '93.8613052368164'}], 'var_functions.query_db:108': [{'max_price': '92.57964324951172'}], 'var_functions.query_db:109': [{'max_price': '47.5942268371582'}], 'var_functions.query_db:110': [{'max_price': '80.04315948486328'}], 'var_functions.query_db:111': [{'max_price': '104.59674072265624'}], 'var_functions.query_db:116': [{'Date': '2015-01-30', 'Adj Close': '121.58584594726562'}], 'var_functions.query_db:117': [{'Date': '2015-01-30', 'Adj Close': '99.8505401611328'}], 'var_functions.query_db:118': [{'max_price': '117.01538848876952'}], 'var_functions.query_db:119': [{'max_price': '121.0569839477539'}], 'var_functions.execute_python:124': {'total_checked': 10, 'over_200': [], 'highest_found': 193.53}, 'var_functions.query_db:126': [{'max_price': '162.96107482910156'}], 'var_functions.query_db:127': [{'max_price': '451.0675659179688'}], 'var_functions.query_db:128': [{'max_price': '27.289674758911133'}], 'var_functions.query_db:129': [{'max_price': '90.47310638427734'}], 'var_functions.execute_python:134': {'JNUG_in_nyse_arca': True, 'JNUG_max_2015': 451.0675659179688, 'message': 'Found one ETF > $200!'}, 'var_functions.query_db:136': [{'max_price': '162.96107482910156'}], 'var_functions.query_db:137': [{'max_price': '118.27999877929688'}], 'var_functions.query_db:138': [{'max_price': '1923.278564453125'}], 'var_functions.query_db:139': [{'max_price': '12988.4140625'}]}

exec(code, env_args)
