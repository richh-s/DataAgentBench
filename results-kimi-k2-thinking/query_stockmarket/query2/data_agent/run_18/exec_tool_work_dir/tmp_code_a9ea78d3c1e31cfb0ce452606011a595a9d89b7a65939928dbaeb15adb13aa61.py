code = """import json

# Load the full list of NYSE Arca ETFs
with open('file_storage/functions.query_db:30.json', 'r') as f:
    etf_data = json.load(f)

nyse_arca_symbols = [item['Symbol'] for item in etf_data]

# Current results we have
results_so_far = {
    'DUST': 1923.278564453125,
    'LABD': 624.0791625976562,
    'LABU': 230.2828063964844,
    'TZA': 272.6275939941406,
    'FAZ': 288.5361328125,
    'QID': 162.42510986328125,  # < 200
    'SDS': 97.26858520507812,   # < 200
    'ERY': 194.72789001464844,  # < 200, but close
    'EDZ': None,  # Need to check
    'NUGT': 162.96107482910156,  # < 200
    'SOXS': None,  # Need to check
    'SOXL': 39.06019592285156,   # < 200
    'SPXS': None,  # Need to check
    'TNA': 48.85812377929688,    # < 200
    'FAS': 34.572391510009766,   # < 200
    'SSO': None,   # Need to check
    'QLD': 41.19669723510742,    # < 200
    'EDC': 120.45299530029295    # < 200
}

# Identify which we need to check
need_to_check = [sym for sym, val in results_so_far.items() if val is None and sym in nyse_arca_symbols]

print('Already found ETFs > $200:', [sym for sym, val in results_so_far.items() if val and val > 200])
print('\nNeed to check remaining:', need_to_check)

# Also check some additional candidates
additional = ['SPXU', 'VXX', 'UVXY', 'TVIX', 'XIV', 'SVXY']
additional_on_nyse = [sym for sym in additional if sym in nyse_arca_symbols]

print('\nAdditional candidates:', additional_on_nyse)

results = {
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'current_high_etfs': [sym for sym, val in results_so_far.items() if val and val > 200],
    'need_to_check': need_to_check,
    'additional_candidates': additional_on_nyse
}

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['test'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:22': [], 'var_functions.query_db:26': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}, {'Adj Close': '192.83792114257807', 'Date': '2015-05-18'}, {'Adj Close': '192.8120574951172', 'Date': '2015-06-23'}, {'Adj Close': '192.77456665039065', 'Date': '2015-05-19'}, {'Adj Close': '192.73838806152344', 'Date': '2015-05-22'}, {'Adj Close': '192.67564392089844', 'Date': '2015-06-22'}], 'var_functions.query_db:28': [{'Date': '2015-01-02', 'Open': '112.48999786376952', 'High': '114.8000030517578', 'Low': '112.31999969482422', 'Close': '114.08000183105467', 'Adj Close': '114.08000183105467', 'Volume': '7109600'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'max_close': '125.2300033569336'}], 'var_functions.query_db:34': [{'max_close': '110.42893981933594'}], 'var_functions.query_db:36': [{'max_close': '163.6190185546875'}], 'var_functions.execute_python:38': {'count': 1435}, 'var_functions.query_db:40': [{'Symbol': 'SPY', 'max_close': '193.3121490478516'}], 'var_functions.query_db:42': [{'max_close': '120.37349700927734'}], 'var_functions.execute_python:44': {'total_symbols': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:48': [{'max_close': '193.3121490478516'}], 'var_functions.query_db:50': [{'max_close': '507.2368774414063'}], 'var_functions.query_db:52': [{'Symbol': 'SQQQ', 'Listing Exchange': 'Q'}], 'var_functions.execute_python:54': {'total': 1435, 'checking_now': 100}, 'var_functions.query_db:56': [{'max_close': '125.2300033569336'}], 'var_functions.query_db:58': [{'max_close': '193.5270538330078'}], 'var_functions.execute_python:60': {'total_nyse_arca_etfs': 1435, 'sample_major_etfs': ['SPY', 'IVV', 'VOO', 'DIA', 'IWM', 'GLD', 'SLV', 'EFA', 'EEM', 'VTI', 'AGG']}, 'var_functions.query_db:62': [{'max_close': '100.54161834716795'}], 'var_functions.query_db:64': [{'max_close': '66.95523071289062'}], 'var_functions.query_db:66': [{'max_close': '22.93797874450684'}], 'var_functions.query_db:68': [], 'var_functions.query_db:70': [{'max_close': '24.036970138549805'}], 'var_functions.query_db:74': [{'max_close': '76.05020141601562'}], 'var_functions.execute_python:76': {'batch_size': 50, 'symbols_to_check': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY'], 'summary': 'Checking 50 symbols from total of 1435'}, 'var_functions.execute_python:78': ['SDS', 'SSO', 'QLD', 'QID', 'DUST', 'NUGT', 'SOXL', 'SOXS', 'SPXS', 'SPXL', 'LABD', 'LABU', 'TZA', 'TNA', 'FAZ', 'FAS'], 'var_functions.query_db:80': [{'Symbol': 'SQQQ', 'max_close': '507.2368774414063'}], 'var_functions.query_db:82': [{'max_close': '97.26858520507812'}], 'var_functions.query_db:84': [{'max_close': '41.19669723510742'}], 'var_functions.execute_python:86': ['SDS', 'SSO', 'QLD', 'QID', 'DUST', 'NUGT', 'SOXL', 'SOXS', 'SPXS', 'SPXL', 'LABD', 'LABU', 'TZA', 'TNA', 'FAZ', 'FAS'], 'var_functions.query_db:88': [{'max_close': '162.42510986328125'}], 'var_functions.query_db:90': [{'max_close': '1923.278564453125'}], 'var_functions.query_db:92': [{'max_close': '162.96107482910156'}], 'var_functions.query_db:94': [{'Symbol': 'DUST', 'Listing Exchange': 'P'}], 'var_functions.query_db:96': [{'max_close': '39.06019592285156'}], 'var_functions.query_db:98': [{'max_close': '624.0791625976562'}], 'var_functions.query_db:100': [{'Symbol': 'DUST', 'Listing Exchange': 'P'}, {'Symbol': 'FAS', 'Listing Exchange': 'P'}, {'Symbol': 'FAZ', 'Listing Exchange': 'P'}, {'Symbol': 'LABD', 'Listing Exchange': 'P'}, {'Symbol': 'LABU', 'Listing Exchange': 'P'}, {'Symbol': 'TNA', 'Listing Exchange': 'P'}, {'Symbol': 'TZA', 'Listing Exchange': 'P'}], 'var_functions.query_db:102': [{'max_close': '272.6275939941406'}], 'var_functions.query_db:104': [{'max_close': '230.2828063964844'}], 'var_functions.query_db:106': [{'max_close': '48.85812377929688'}], 'var_functions.query_db:108': [{'max_close': '34.572391510009766'}], 'var_functions.execute_python:110': ['DUST', 'NUGT', 'LABD', 'LABU', 'TZA', 'TNA', 'FAZ', 'FAS', 'SDS', 'SSO', 'QLD', 'QID', 'SOXL', 'SOXS', 'SPXS', 'SPXL', 'EDC', 'EDZ', 'ERY', 'ERX'], 'var_functions.query_db:112': [{'max_close': '194.72789001464844'}], 'var_functions.query_db:114': [{'Symbol': 'EDC'}, {'Symbol': 'EDZ'}, {'Symbol': 'SOXL'}, {'Symbol': 'SOXS'}, {'Symbol': 'SPXL'}, {'Symbol': 'SPXS'}], 'var_functions.query_db:116': [{'max_close': '120.45299530029295'}], 'var_functions.query_db:118': [{'max_close': '288.5361328125'}]}

exec(code, env_args)
