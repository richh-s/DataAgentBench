code = """import json

# Read the NYSE Arca ETFs file
nyse_file = var_functions.query_db_60
with open(nyse_file, 'r') as f:
    nyse_data = json.load(f)

# Read the stocktrade tickers file  
tickers_file = var_functions.list_db_55
with open(tickers_file, 'r') as f:
    tickers_data = json.load(f)

# Extract symbols
nyse_symbols = {item['Symbol'] for item in nyse_data}
trade_symbols = set(tickers_data)

# Find common ETFs
common_etfs = nyse_symbols.intersection(trade_symbols)
common_list = sorted(list(common_etfs))

print(f"NYSE Arca ETFs: {len(nyse_symbols)}")
print(f"Stocktrade tickers: {len(trade_symbols)}")
print(f"Common ETFs with price data: {len(common_list)}")
print(f"First 20: {common_list[:20]}")

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_symbols),
    'total_trade_tickers': len(trade_symbols),
    'common_etfs_count': len(common_list),
    'common_etfs_sample': common_list[:20]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'check_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_price': '121.58584594726562'}], 'var_functions.query_db:32': [{'max_price': '27.289674758911133'}], 'var_functions.execute_python:36': {'tested_etfs': ['GLD', 'DIA', 'SPY', 'TLT', 'QQQ', 'IWM', 'EFA', 'EEM', 'AGG', 'IVV'], 'next_steps': 'Need to query each ETF table for 2015 data'}, 'var_functions.query_db:40': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}, {'Symbol': 'AGG'}, {'Symbol': 'AGGP'}, {'Symbol': 'AGGY'}, {'Symbol': 'AGQ'}, {'Symbol': 'AGZ'}, {'Symbol': 'AIEQ'}, {'Symbol': 'AIIQ'}, {'Symbol': 'AMLP'}, {'Symbol': 'AMOM'}, {'Symbol': 'AMZA'}, {'Symbol': 'AOA'}, {'Symbol': 'AOK'}, {'Symbol': 'AOM'}, {'Symbol': 'AOR'}, {'Symbol': 'ARGT'}, {'Symbol': 'ARKF'}, {'Symbol': 'ARKK'}, {'Symbol': 'ARKW'}, {'Symbol': 'ARMR'}, {'Symbol': 'ASEA'}, {'Symbol': 'ASHR'}, {'Symbol': 'ASHS'}, {'Symbol': 'ASHX'}, {'Symbol': 'AUSF'}, {'Symbol': 'AVDE'}, {'Symbol': 'AVDV'}, {'Symbol': 'AVEM'}, {'Symbol': 'AVUS'}, {'Symbol': 'AVUV'}, {'Symbol': 'AWAY'}, {'Symbol': 'AWTM'}, {'Symbol': 'AXJL'}, {'Symbol': 'BAB'}, {'Symbol': 'BATT'}, {'Symbol': 'BBC'}, {'Symbol': 'BBP'}, {'Symbol': 'BCD'}, {'Symbol': 'BCI'}, {'Symbol': 'BDCY'}, {'Symbol': 'BDRY'}], 'var_functions.query_db:46': [{'max_price': '24.036970138549805'}], 'var_functions.query_db:50': [{'max_price': '193.3121490478516'}], 'var_functions.query_db:52': [{'max_price': '110.42893981933594'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.list_db:55': 'file_storage/functions.list_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': [{'max_price': '163.6190185546875'}], 'var_functions.query_db:63': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:64': [{'max_price': '193.3121490478516'}], 'var_functions.query_db:65': [{'max_price': '110.42893981933594'}]}

exec(code, env_args)
