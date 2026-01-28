code = """import json
import os
from collections import defaultdict

# Load NYSE Arca ETF symbols
etf_file = locals()['var_functions.query_db:40']
if isinstance(etf_file, str) and os.path.exists(etf_file):
    with open(etf_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_file

all_symbols = [item['Symbol'] for item in nyse_arca_etfs]

# Based on initial tests, let's prioritize checking:
# 1. Leveraged/inverse ETFs (which tend to have higher prices)
# 2. Then check a broader sample

leveraged_inverse_etfs = [
    'SSO', 'SDS', 'UPRO', 'SPXU', 'SPXL', 'SPXS',
    'QQQ', 'QLD', 'QID', 'SQQQ', 'TQQQ',
    'DDM', 'DXD', 'UDOW', 'SDOW',
    'TNA', 'TZA', 'UMDD', 'SMDD', 'TWM', 'UWM',
    'UYM', 'SMN', 'UGE', 'SZK', 'UXI', 'SIJ',
    'FINU', 'FINZ', 'DPST', 'RETL', 'LABU', 'LABD',
    'NUGT', 'DUST', 'GUSH', 'DRIP', 'JNUG', 'JDST'
]

# Filter for ETFs that are actually listed on NYSE Arca
valid_leveraged = [etf for etf in leveraged_inverse_etfs if etf in all_symbols]

# Add random sample of other ETFs
import random
other_samples = random.sample([s for s in all_symbols if s not in valid_leveraged], 100)

test_symbols = valid_leveraged + other_samples
print('__RESULT__:')
print(json.dumps({
    'leveraged_etfs': len(valid_leveraged),
    'other_samples': len(other_samples),
    'total_test_symbols': len(test_symbols),
    'sample_symbols': valid_leveraged[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 1435, 'head': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_arca_etf_count': 1435, 'available_tables_count': 2753, 'common_symbols_count': 1435, 'common_symbols_sample': ['LOWC', 'RYZZ', 'PPDM', 'XDIV', 'ZROZ', 'FXY', 'RYE', 'XSOE', 'IYY', 'ERUS']}, 'var_functions.execute_python:10': {'total_symbols': 1435, 'first_20_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:12': {'message': 'Need to query 1435 symbols for 2015 data', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:18': {'status': 'Stored ETF symbols', 'count': 1435}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.execute_python:26': {'total_symbols': 1435, 'batch_count': 29, 'first_batch_size': 50, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:28': {'total_symbols': 1435, 'batches_created': 15, 'batch_size': 100, 'first_batch_preview': '\n        SELECT \'AAAU\' as Symbol, "Adj Close", Date \n        FROM "AAAU" \n        WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200\n         UNION ALL \n        SELECT \'AADR\' as'}, 'var_functions.execute_python:30': {'total_nyse_arca_etfs': 1435, 'representative_sample_size': 45, 'sample_symbols': ['XSOE', 'VEA', 'VUG', 'VTEB', 'FIVG', 'PRF', 'IWV', 'DIVO', 'XLF', 'SCHE', 'XLY', 'IWM', 'IWD', 'DIA', 'FRI', 'IQSU', 'TWM', 'XLK', 'SBIO', 'SPY', 'VWO', 'EEM', 'DGRO', 'IWB', 'SCHD', 'VTV', 'AGG', 'SSO', 'XLV', 'XLE', 'GLD', 'EFA', 'ENFR', 'TPOR', 'NERD', 'IBDO', 'FPEI', 'VYM', 'WBIY', 'IWF', 'RFFC', 'EFO', 'USSG', 'VTI', 'OSCV']}, 'var_functions.execute_python:32': {'nyse_arca_etfs': 1435, 'available_tables': 2753, 'valid_intersection': 1435, 'test_symbols': ['SPY', 'DIA', 'IWB', 'IWM', 'EFA', 'EEM', 'GLD', 'AGG', 'ICOL', 'IQDF']}, 'var_functions.query_db:34': [], 'var_functions.query_db:36': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}], 'var_functions.query_db:38': [{'Date': '2015-05-19', 'Adj Close': '163.6190185546875'}, {'Date': '2015-05-21', 'Adj Close': '163.4937286376953'}, {'Date': '2015-05-20', 'Adj Close': '163.42222595214844'}, {'Date': '2015-05-18', 'Adj Close': '163.39537048339844'}, {'Date': '2015-05-15', 'Adj Close': '163.21649169921875'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_symbols': 1435, 'number_of_queries': 29, 'first_query_preview': '\n        SELECT \'AAAU\' as Symbol, MAX("Adj Close") as max_price, MIN("Adj Close") as min_price, COUNT(*) as days_above_threshold\n        FROM "AAAU" \n        WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200\n         UNION ALL \n        SELECT \'AADR\' as Symbol, MAX("Adj Close"'}, 'var_functions.execute_python:44': {'total_nyse_arca_etfs': 1435, 'available_in_trade_db': 1435, 'missing_symbols': 0}, 'var_functions.query_db:46': [{'Symbol': 'AAAU', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AADR', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'ABEQ', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'ACSG', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'ACWF', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AFK', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AFLG', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AFMC', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AFSM', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AFTY', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AGG', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AGGP', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AGGY', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AGQ', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AGZ', 'max_price': 'nan', 'days_above_threshold': '0'}], 'var_functions.query_db:48': [{'Date': '2015-12-01', 'Adj Close': '110.42893981933594'}, {'Date': '2015-12-04', 'Adj Close': '110.40975952148438'}, {'Date': '2015-11-04', 'Adj Close': '110.29467010498048'}, {'Date': '2015-11-03', 'Adj Close': '110.2851104736328'}, {'Date': '2015-11-06', 'Adj Close': '110.07412719726562'}], 'var_functions.execute_python:50': {'total_symbols_checked': 15, 'ets_with_valid_data': 0, 'sample_results': [{'Symbol': 'AAAU', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'AADR', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'ABEQ', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'ACSG', 'max_price': 'nan', 'days_above_threshold': '0'}, {'Symbol': 'ACWF', 'max_price': 'nan', 'days_above_threshold': '0'}]}, 'var_functions.query_db:52': [{'Symbol': 'GLD', 'max_price': '125.2300033569336'}, {'Symbol': 'TLT', 'max_price': '121.58584594726562'}, {'Symbol': 'IAU', 'max_price': '12.619999885559082'}], 'var_functions.execute_python:56': {'nyse_arca_etf_count': 1435, 'test_symbols_count': 35, 'test_symbols': ['SPY', 'DIA', 'IVV', 'VOO', 'IWB', 'IWM', 'IWV', 'VTI', 'EFA', 'EEM', 'VEA', 'VWO', 'XLF', 'XLV', 'XLK', 'XLE', 'XLY', 'LQD', 'GLD', 'SLV', 'MINT', 'BIL', 'VYM', 'SCHD', 'DGRO', 'XSLV', 'TAN', 'TOLZ', 'UCC', 'OVF', 'SCHA', 'SPDW', 'DFE', 'AFSM', 'PWC']}, 'var_functions.execute_python:60': {'total_symbols': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.execute_python:62': {'total_symbols': 1435, 'status': 'Ready to query stocktrade_database'}, 'var_functions.execute_python:64': {'total_symbols': 1435, 'message': 'Symbol list prepared for batched queries'}, 'var_functions.query_db:66': [{'Symbol': 'BIL', 'max_price': '87.24989318847656'}, {'Symbol': 'MINT', 'max_price': '92.57964324951172'}, {'Symbol': 'SHV', 'max_price': '104.59674072265624'}, {'Symbol': 'MUB', 'max_price': '100.25205993652344'}, {'Symbol': 'VCLT', 'max_price': '78.16940307617188'}, {'Symbol': 'EDV', 'max_price': '117.01538848876952'}], 'var_functions.query_db:68': [{'Symbol': 'DDM', 'max_price': '22.4426212310791'}, {'Symbol': 'QLD', 'max_price': '41.19669723510742'}, {'Symbol': 'SSO', 'max_price': '66.95523071289062'}, {'Symbol': 'TWM', 'max_price': '43.75156021118164'}, {'Symbol': 'SDS', 'max_price': '97.26858520507812'}, {'Symbol': 'UPRO', 'max_price': '24.036970138549805'}, {'Symbol': 'SPXL', 'max_price': '22.93797874450684'}, {'Symbol': 'SPXS', 'max_price': '119.74252319335938'}, {'Symbol': 'SQQQ', 'max_price': '507.2368774414063'}]}

exec(code, env_args)
