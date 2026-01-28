code = """import json
import os

# Load ETF symbols
etf_file = locals()['var_functions.query_db:14']
if isinstance(etf_file, str) and os.path.exists(etf_file):
    with open(etf_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_file

nyse_arca_symbols = set([item['Symbol'] for item in nyse_arca_etfs])

# Load available tables
available_file = locals()['var_functions.list_db:6']
if isinstance(available_file, str) and os.path.exists(available_file):
    with open(available_file, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = available_file

available_symbols = set(all_tables)

# Find intersection
valid_symbols = list(nyse_arca_symbols.intersection(available_symbols))

# Select a smaller set of well-known ETFs to test
common_etfs = ['SPY', 'QQQ', 'DIA', 'IWB', 'IWM', 'EFA', 'EEM', 'TLT', 'GLD', 'AGG']
test_symbols = [s for s in common_etfs if s in valid_symbols]

# Add some additional random symbols if needed
if len(test_symbols) < 10:
    import random
    additional = random.sample(valid_symbols, 10 - len(test_symbols))
    test_symbols.extend(additional)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etfs': len(nyse_arca_symbols),
    'available_tables': len(available_symbols),
    'valid_intersection': len(valid_symbols),
    'test_symbols': test_symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 1435, 'head': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_arca_etf_count': 1435, 'available_tables_count': 2753, 'common_symbols_count': 1435, 'common_symbols_sample': ['LOWC', 'RYZZ', 'PPDM', 'XDIV', 'ZROZ', 'FXY', 'RYE', 'XSOE', 'IYY', 'ERUS']}, 'var_functions.execute_python:10': {'total_symbols': 1435, 'first_20_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:12': {'message': 'Need to query 1435 symbols for 2015 data', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:18': {'status': 'Stored ETF symbols', 'count': 1435}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.execute_python:26': {'total_symbols': 1435, 'batch_count': 29, 'first_batch_size': 50, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:28': {'total_symbols': 1435, 'batches_created': 15, 'batch_size': 100, 'first_batch_preview': '\n        SELECT \'AAAU\' as Symbol, "Adj Close", Date \n        FROM "AAAU" \n        WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200\n         UNION ALL \n        SELECT \'AADR\' as'}, 'var_functions.execute_python:30': {'total_nyse_arca_etfs': 1435, 'representative_sample_size': 45, 'sample_symbols': ['XSOE', 'VEA', 'VUG', 'VTEB', 'FIVG', 'PRF', 'IWV', 'DIVO', 'XLF', 'SCHE', 'XLY', 'IWM', 'IWD', 'DIA', 'FRI', 'IQSU', 'TWM', 'XLK', 'SBIO', 'SPY', 'VWO', 'EEM', 'DGRO', 'IWB', 'SCHD', 'VTV', 'AGG', 'SSO', 'XLV', 'XLE', 'GLD', 'EFA', 'ENFR', 'TPOR', 'NERD', 'IBDO', 'FPEI', 'VYM', 'WBIY', 'IWF', 'RFFC', 'EFO', 'USSG', 'VTI', 'OSCV']}}

exec(code, env_args)
