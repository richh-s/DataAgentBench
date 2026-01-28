code = """import json

# Get the file paths
nyse_arca_file = var_functions.query_db_54
stocktrade_tickers_file = var_functions.list_db_55

print(f"NYSE Arca file: {nyse_arca_file}")
print(f"Stocktrade tickers file: {stocktrade_tickers_file}")

# Load the data
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

with open(stocktrade_tickers_file, 'r') as f:
    stocktrade_tickers = json.load(f)

# Extract symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
stocktrade_symbols = set(stocktrade_tickers)

print(f"Total NYSE Arca ETFs: {len(nyse_arca_symbols)}")
print(f"Total tickers in stocktrade database: {len(stocktrade_symbols)}")

# Find common ETFs
common_etfs = nyse_arca_symbols.intersection(stocktrade_symbols)
common_list = sorted(list(common_etfs))

print(f"NYSE Arca ETFs with price data: {len(common_list)}")

# Check which ones have price > $200 in 2015
# Let's start by checking a few that are likely to be high-priced
high_priced_candidates = []

# First, let's see if any of these well-known ETFs had prices > $200 in 2015
test_symbols = ['SPY', 'IVV', 'QQQ', 'DIA', 'VFINX', 'GLD', 'EFA', 'EEM', 'AGG']
potential_symbols = [s for s in test_symbols if s in common_list]

print(f"Testing well-known symbols: {potential_symbols}")

# We'll need to query each of these
print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etf_count': len(nyse_arca_symbols),
    'common_etfs_count': len(common_list),
    'test_symbols': potential_symbols,
    'common_list_sample': common_list[:20]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'check_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_price': '121.58584594726562'}], 'var_functions.query_db:32': [{'max_price': '27.289674758911133'}], 'var_functions.execute_python:36': {'tested_etfs': ['GLD', 'DIA', 'SPY', 'TLT', 'QQQ', 'IWM', 'EFA', 'EEM', 'AGG', 'IVV'], 'next_steps': 'Need to query each ETF table for 2015 data'}, 'var_functions.query_db:40': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}, {'Symbol': 'AGG'}, {'Symbol': 'AGGP'}, {'Symbol': 'AGGY'}, {'Symbol': 'AGQ'}, {'Symbol': 'AGZ'}, {'Symbol': 'AIEQ'}, {'Symbol': 'AIIQ'}, {'Symbol': 'AMLP'}, {'Symbol': 'AMOM'}, {'Symbol': 'AMZA'}, {'Symbol': 'AOA'}, {'Symbol': 'AOK'}, {'Symbol': 'AOM'}, {'Symbol': 'AOR'}, {'Symbol': 'ARGT'}, {'Symbol': 'ARKF'}, {'Symbol': 'ARKK'}, {'Symbol': 'ARKW'}, {'Symbol': 'ARMR'}, {'Symbol': 'ASEA'}, {'Symbol': 'ASHR'}, {'Symbol': 'ASHS'}, {'Symbol': 'ASHX'}, {'Symbol': 'AUSF'}, {'Symbol': 'AVDE'}, {'Symbol': 'AVDV'}, {'Symbol': 'AVEM'}, {'Symbol': 'AVUS'}, {'Symbol': 'AVUV'}, {'Symbol': 'AWAY'}, {'Symbol': 'AWTM'}, {'Symbol': 'AXJL'}, {'Symbol': 'BAB'}, {'Symbol': 'BATT'}, {'Symbol': 'BBC'}, {'Symbol': 'BBP'}, {'Symbol': 'BCD'}, {'Symbol': 'BCI'}, {'Symbol': 'BDCY'}, {'Symbol': 'BDRY'}], 'var_functions.query_db:46': [{'max_price': '24.036970138549805'}], 'var_functions.query_db:50': [{'max_price': '193.3121490478516'}], 'var_functions.query_db:52': [{'max_price': '110.42893981933594'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.list_db:55': 'file_storage/functions.list_db:55.json'}

exec(code, env_args)
