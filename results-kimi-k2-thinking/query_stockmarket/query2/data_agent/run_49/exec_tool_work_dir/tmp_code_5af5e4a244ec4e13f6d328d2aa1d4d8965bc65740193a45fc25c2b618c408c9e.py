code = """import json
import os
from collections import defaultdict

# Load ETF symbols
etf_file = locals()['var_functions.query_db:40']
if isinstance(etf_file, str) and os.path.exists(etf_file):
    with open(etf_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_file

all_symbols = [item['Symbol'] for item in nyse_arca_etfs]

# Get available tables
tables_file = locals()['var_functions.list_db:6']
if isinstance(tables_file, str) and os.path.exists(tables_file):
    with open(tables_file, 'r') as f:
        available_tables = json.load(f)
else:
    available_tables = tables_file

available_set = set(available_tables)
valid_symbols = [s for s in all_symbols if s in available_set]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(all_symbols),
    'available_in_trade_db': len(valid_symbols),
    'missing_symbols': len(all_symbols) - len(valid_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 1435, 'head': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_arca_etf_count': 1435, 'available_tables_count': 2753, 'common_symbols_count': 1435, 'common_symbols_sample': ['LOWC', 'RYZZ', 'PPDM', 'XDIV', 'ZROZ', 'FXY', 'RYE', 'XSOE', 'IYY', 'ERUS']}, 'var_functions.execute_python:10': {'total_symbols': 1435, 'first_20_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:12': {'message': 'Need to query 1435 symbols for 2015 data', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:18': {'status': 'Stored ETF symbols', 'count': 1435}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.execute_python:26': {'total_symbols': 1435, 'batch_count': 29, 'first_batch_size': 50, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:28': {'total_symbols': 1435, 'batches_created': 15, 'batch_size': 100, 'first_batch_preview': '\n        SELECT \'AAAU\' as Symbol, "Adj Close", Date \n        FROM "AAAU" \n        WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200\n         UNION ALL \n        SELECT \'AADR\' as'}, 'var_functions.execute_python:30': {'total_nyse_arca_etfs': 1435, 'representative_sample_size': 45, 'sample_symbols': ['XSOE', 'VEA', 'VUG', 'VTEB', 'FIVG', 'PRF', 'IWV', 'DIVO', 'XLF', 'SCHE', 'XLY', 'IWM', 'IWD', 'DIA', 'FRI', 'IQSU', 'TWM', 'XLK', 'SBIO', 'SPY', 'VWO', 'EEM', 'DGRO', 'IWB', 'SCHD', 'VTV', 'AGG', 'SSO', 'XLV', 'XLE', 'GLD', 'EFA', 'ENFR', 'TPOR', 'NERD', 'IBDO', 'FPEI', 'VYM', 'WBIY', 'IWF', 'RFFC', 'EFO', 'USSG', 'VTI', 'OSCV']}, 'var_functions.execute_python:32': {'nyse_arca_etfs': 1435, 'available_tables': 2753, 'valid_intersection': 1435, 'test_symbols': ['SPY', 'DIA', 'IWB', 'IWM', 'EFA', 'EEM', 'GLD', 'AGG', 'ICOL', 'IQDF']}, 'var_functions.query_db:34': [], 'var_functions.query_db:36': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}], 'var_functions.query_db:38': [{'Date': '2015-05-19', 'Adj Close': '163.6190185546875'}, {'Date': '2015-05-21', 'Adj Close': '163.4937286376953'}, {'Date': '2015-05-20', 'Adj Close': '163.42222595214844'}, {'Date': '2015-05-18', 'Adj Close': '163.39537048339844'}, {'Date': '2015-05-15', 'Adj Close': '163.21649169921875'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_symbols': 1435, 'number_of_queries': 29, 'first_query_preview': '\n        SELECT \'AAAU\' as Symbol, MAX("Adj Close") as max_price, MIN("Adj Close") as min_price, COUNT(*) as days_above_threshold\n        FROM "AAAU" \n        WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200\n         UNION ALL \n        SELECT \'AADR\' as Symbol, MAX("Adj Close"'}}

exec(code, env_args)
