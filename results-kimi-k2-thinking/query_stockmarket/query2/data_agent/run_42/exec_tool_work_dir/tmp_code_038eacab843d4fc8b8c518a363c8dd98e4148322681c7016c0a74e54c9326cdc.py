code = """import json

# Read the NYSE Arca ETFs list
nyse_file = var_functions.query_db_42
with open(nyse_file, 'r') as f:
    nyse_data = json.load(f)

# Extract all symbols
all_symbols = [item['Symbol'] for item in nyse_data]
print(f"Total NYSE Arca ETFs to check: {len(all_symbols)}")
print(f"First 10: {all_symbols[:10]}")

# Check which symbols exist in stocktrade_database
# We'll need to query the stocktrade database to see what tables exist
# For now, let's create a batch query for a subset to test

# Let's start by testing a reasonable subset of symbols that might have high prices
test_symbols = all_symbols[:100]  # First 100 symbols

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(all_symbols),
    'test_symbols': test_symbols[:20],
    'message': 'Ready to query price data'
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'check_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_price': '121.58584594726562'}], 'var_functions.query_db:32': [{'max_price': '27.289674758911133'}], 'var_functions.execute_python:36': {'tested_etfs': ['GLD', 'DIA', 'SPY', 'TLT', 'QQQ', 'IWM', 'EFA', 'EEM', 'AGG', 'IVV'], 'next_steps': 'Need to query each ETF table for 2015 data'}, 'var_functions.query_db:40': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}, {'Symbol': 'AGG'}, {'Symbol': 'AGGP'}, {'Symbol': 'AGGY'}, {'Symbol': 'AGQ'}, {'Symbol': 'AGZ'}, {'Symbol': 'AIEQ'}, {'Symbol': 'AIIQ'}, {'Symbol': 'AMLP'}, {'Symbol': 'AMOM'}, {'Symbol': 'AMZA'}, {'Symbol': 'AOA'}, {'Symbol': 'AOK'}, {'Symbol': 'AOM'}, {'Symbol': 'AOR'}, {'Symbol': 'ARGT'}, {'Symbol': 'ARKF'}, {'Symbol': 'ARKK'}, {'Symbol': 'ARKW'}, {'Symbol': 'ARMR'}, {'Symbol': 'ASEA'}, {'Symbol': 'ASHR'}, {'Symbol': 'ASHS'}, {'Symbol': 'ASHX'}, {'Symbol': 'AUSF'}, {'Symbol': 'AVDE'}, {'Symbol': 'AVDV'}, {'Symbol': 'AVEM'}, {'Symbol': 'AVUS'}, {'Symbol': 'AVUV'}, {'Symbol': 'AWAY'}, {'Symbol': 'AWTM'}, {'Symbol': 'AXJL'}, {'Symbol': 'BAB'}, {'Symbol': 'BATT'}, {'Symbol': 'BBC'}, {'Symbol': 'BBP'}, {'Symbol': 'BCD'}, {'Symbol': 'BCI'}, {'Symbol': 'BDCY'}, {'Symbol': 'BDRY'}], 'var_functions.query_db:46': [{'max_price': '24.036970138549805'}]}

exec(code, env_args)
