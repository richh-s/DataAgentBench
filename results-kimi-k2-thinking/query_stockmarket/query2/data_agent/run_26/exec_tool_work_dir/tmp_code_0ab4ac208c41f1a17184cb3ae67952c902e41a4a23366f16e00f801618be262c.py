code = """import json
import os

# Load NYSE Arca ETFs and trade tables
nyse_arca_file = '/tmp/tmp_query_db_68.json'
trade_tables_file = '/tmp/tmp_list_db_18.json'

with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)
with open(trade_tables_file, 'r') as f:
    trade_tables = json.load(f)

# Find common symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
common_symbols = sorted(list(nyse_arca_symbols.intersection(trade_tables)))

print(f"NYSE Arca ETFs with price data: {len(common_symbols)}")
print(f"First 10: {common_symbols[:10]}")

# Check high-value candidates first
high_value_candidates = ['DUST', 'NUGT', 'SPXL', 'UPRO', 'TQQQ', 'TECL', 'SOXL', 'FAS', 'DRN', 'URE', 'ROM', 'GLD', 'SPY', 'DIA', 'IVV']

print(f"\nChecking {len(high_value_candidates)} high-value candidates...")
available_candidates = [c for c in high_value_candidates if c in common_symbols]
print(f"Available: {available_candidates}")

print("__RESULT__:")
print(json.dumps({
    "total_common": len(common_symbols),
    "candidates_available": available_candidates
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': {'status': 'checked'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:24': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'Date': '2015-05-19', 'Adj Close': '163.6190185546875'}, {'Date': '2015-05-21', 'Adj Close': '163.4937286376953'}, {'Date': '2015-05-20', 'Adj Close': '163.42222595214844'}, {'Date': '2015-05-18', 'Adj Close': '163.39537048339844'}, {'Date': '2015-05-15', 'Adj Close': '163.21649169921875'}], 'var_functions.query_db:38': [{'max("Adj Close")': 'nan', 'min("Adj Close")': 'nan'}], 'var_functions.execute_python:42': {'error': 'file not found'}, 'var_functions.query_db:44': [{'max("Adj Close")': '193.3121490478516', 'min("Adj Close")': '170.28823852539062'}], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': [{'Symbol': 'DIA'}, {'Symbol': 'EEM'}, {'Symbol': 'EFA'}, {'Symbol': 'GLD'}, {'Symbol': 'IVV'}, {'Symbol': 'IWM'}, {'Symbol': 'SPY'}, {'Symbol': 'VTI'}, {'Symbol': 'VWO'}], 'var_functions.query_db:52': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:54': [{'max_price': '59.14651870727539'}], 'var_functions.query_db:58': [{'Symbol': 'AGG'}, {'Symbol': 'BIL'}, {'Symbol': 'DRN'}, {'Symbol': 'DUST'}, {'Symbol': 'FAS'}, {'Symbol': 'LABU'}, {'Symbol': 'MINT'}, {'Symbol': 'NUGT'}, {'Symbol': 'ROM'}, {'Symbol': 'SOXL'}, {'Symbol': 'SPXL'}, {'Symbol': 'SVXY'}, {'Symbol': 'TECL'}, {'Symbol': 'UPRO'}, {'Symbol': 'URE'}], 'var_functions.query_db:62': [{'Date': '2015-08-05', 'Adj Close': '1923.278564453125'}, {'Date': '2015-08-03', 'Adj Close': '1843.9783935546875'}, {'Date': '2015-08-04', 'Adj Close': '1841.5308837890625'}, {'Date': '2015-08-06', 'Adj Close': '1805.3070068359373'}, {'Date': '2015-08-07', 'Adj Close': '1786.2161865234375'}], 'var_functions.query_db:64': [{'max_price': '162.96107482910156'}], 'var_functions.query_db:66': [{'max_price': '22.93797874450684'}], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
