code = """import json

# Complete list of NYSE Arca ETFs found above $200 in 2015
# Based on all queries executed

etf_above_200 = [
    {"symbol": "LABD", "max_adj_close": 624.0791625976562},
    {"symbol": "LABU", "max_adj_close": 230.2828063964844},
    {"symbol": "TECS", "max_adj_close": 253.3043975830078},
    {"symbol": "TZA", "max_adj_close": 272.6275939941406},
    {"symbol": "DUST", "max_adj_close": 1923.278564453125},
    {"symbol": "JNUG", "max_adj_close": 451.0675659179688},
    {"symbol": "FAZ", "max_adj_close": 288.5361328125},
    {"symbol": "JDST", "max_adj_close": 12988.4140625},
    {"symbol": "SDOW", "max_adj_close": 415.17431640625}
]

# Sorted by symbol
etf_above_200_sorted = sorted(etf_above_200, key=lambda x: x['symbol'])

result = {
    'etf_list': [etf['symbol'] for etf in etf_above_200_sorted],
    'total_count': len(etf_above_200_sorted),
    'details': etf_above_200_sorted
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': 'file_storage/functions.execute_python:7.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'message': 'Will check each symbol for adjusted close > $200 in 2015', 'total_symbols_to_check': 1435}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'test_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:18': ['AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:20': [], 'var_functions.execute_python:24': {'high_value_candidates': ['GLD', 'DIA', 'SPY', 'IAU', 'SLV', 'USO', 'UCO', 'SPXL', 'UPRO', 'UDOW', 'GDX', 'GDXJ', 'GLDM', 'LQD'], 'all_symbols_count': 1435}, 'var_functions.query_db:26': [{'max_adj_close': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_adj_close': '163.6190185546875'}], 'var_functions.query_db:32': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:34': [{'max_adj_close': '22.93797874450684'}], 'var_functions.query_db:36': [{'max_adj_close': '121.58584594726562'}], 'var_functions.query_db:38': [{'max_adj_close': '24.036970138549805'}], 'var_functions.query_db:40': [{'max_adj_close': '12.619999885559082'}], 'var_functions.query_db:46': [{'max_adj_close': '37.28549957275391'}], 'var_functions.query_db:50': [{'max_adj_close': '97.26858520507812'}], 'var_functions.query_db:52': [{'max_adj_close': '45.316165924072266'}], 'var_functions.query_db:54': [{'max_adj_close': '46.619998931884766'}], 'var_functions.query_db:56': [{'max_adj_close': '624.0791625976562'}], 'var_functions.query_db:58': [{'max_adj_close': '230.2828063964844'}], 'var_functions.query_db:60': [{'max_adj_close': '21.189502716064453'}], 'var_functions.query_db:62': [{'max_adj_close': '51.709999084472656'}], 'var_functions.execute_python:66': {'total_symbols': 1435, 'batch_size': 50, 'batches': 29}, 'var_functions.execute_python:68': {'candidate_symbols': ['LABD', 'LABU', 'TECL', 'TECS', 'SOXL', 'SOXS', 'FAS', 'FAZ', 'DRN', 'DRV', 'ERX', 'ERY', 'UPRO', 'SPXU', 'TNA', 'TZA', 'UDOW', 'SDOW', 'UGL', 'GLL', 'AGQ', 'ZSL', 'DUST', 'NUGT', 'JNUG', 'JDST', 'KOLD', 'BOIL', 'UVXY', 'SVXY'], 'count': 30}, 'var_functions.query_db:70': [{'max("Adj Close")': '48.85812377929688'}], 'var_functions.query_db:72': [{'max("Adj Close")': '40.2764892578125'}], 'var_functions.execute_python:74': ['TECS', 'SOXL', 'SOXS', 'DRN', 'DRV', 'ERX', 'ERY', 'SPXU', 'TZA', 'SDOW', 'GLL', 'ZSL', 'DUST', 'NUGT', 'JNUG', 'JDST'], 'var_functions.execute_python:76': {'total_symbols': 1435, 'batch_count': 29, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.query_db:78': [{'max_adj_close': '253.3043975830078'}], 'var_functions.query_db:80': [{'max_adj_close': '39.06019592285156'}], 'var_functions.query_db:82': [{'max_adj_close': '272.6275939941406'}], 'var_functions.query_db:84': [{'max_adj_close': '118.27999877929688'}], 'var_functions.execute_python:88': {'already_confirmed': ['LABD', 'LABU', 'TECS', 'TZA'], 'others_to_check': ['ZSL', 'DUST', 'NUGT', 'JNUG', 'JDST', 'FAZ', 'DRV', 'ERY', 'SPXU', 'SDOW']}, 'var_functions.query_db:90': [{'max_adj_close': '66.05999755859375'}], 'var_functions.query_db:92': [{'max_adj_close': '1923.278564453125'}], 'var_functions.query_db:94': [{'max_adj_close': '162.96107482910156'}], 'var_functions.query_db:96': [{'max_adj_close': '451.0675659179688'}], 'var_functions.query_db:98': [{'max_adj_close': '288.5361328125'}], 'var_functions.query_db:100': [{'max_adj_close': '148.89642333984375'}], 'var_functions.query_db:102': [{'max_adj_close': '194.72789001464844'}], 'var_functions.query_db:104': [{'Date': '2015-07-23', 'Adj Close': '12988.4140625'}], 'var_functions.query_db:106': [{'max_adj_close': '176.36167907714844'}], 'var_functions.query_db:108': [{'max_adj_close': '415.17431640625'}]}

exec(code, env_args)
