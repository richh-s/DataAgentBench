code = """import json

# Get all NYSE Arca ETFs
nyse_arca_path = locals()['var_functions.query_db:0']
with open(nyse_arca_path, 'r') as f:
    nyse_arca_etfs = json.load(f)

nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Let's create a systematic test plan
# We'll test the main broad market ETFs first which are most likely to have high prices
main_etfs_to_test = [
    "SPY", "IVV", "VOO", "DIA", "QQQ", "IWM", "MDY", "IJH", "IJR",
    "XLF", "XLE", "XLK", "XLV", "XLY", "XLP", "XLI", "XLB", "XLU"
]

# Filter to only those that are actually NYSE Arca ETFs
main_etfs_filtered = [etf for etf in main_etfs_to_test if etf in nyse_arca_symbols]

# Test SPY prices
print(f"Main ETFs to test: {main_etfs_filtered}")

result = {
    "filtered_etfs": main_etfs_filtered,
    "total_nyse_arca_etfs": len(nyse_arca_symbols)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'etfs_with_data': 1435, 'etfs_without_data': 0, 'existing_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'missing_sample': []}, 'var_functions.query_db:18': [], 'var_functions.execute_python:20': {'total_etfs_checked': 1435, 'etfs_above_200': [], 'count': 0}, 'var_functions.query_db:22': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}], 'var_functions.query_db:24': [{'Adj Close': '110.42893981933594', 'Date': '2015-12-01'}, {'Adj Close': '110.40975952148438', 'Date': '2015-12-04'}, {'Adj Close': '110.29467010498048', 'Date': '2015-11-04'}, {'Adj Close': '110.2851104736328', 'Date': '2015-11-03'}, {'Adj Close': '110.07412719726562', 'Date': '2015-11-06'}], 'var_functions.execute_python:26': {'sample_size': 50, 'etfs_to_test': ['YLD', 'ARKF', 'FNCL', 'FXC', 'MYY', 'WBII', 'SYE', 'DIVA', 'ISMD', 'CNXT', 'XLI', 'PCEF', 'XTH', 'PPSC', 'ICOL', 'TLEH', 'EQAL', 'HEWY', 'UBT', 'RWDC', 'IAI', 'DSTL', 'PALL', 'RLY', 'HIPS', 'PLAT', 'TOK', 'SCID', 'JKF', 'GOEX', 'HDIV', 'IYK', 'SPEM', 'TMF', 'FRAK', 'XOUT', 'FLMX', 'SCHE', 'SPHB', 'DTD', 'AOA', 'VV', 'DLBR', 'PFXF', 'INCO', 'SPMO', 'IYG', 'DYNF', 'NFLT', 'PASS']}, 'var_functions.query_db:28': [{'max_close': '31.778106689453125'}], 'var_functions.execute_python:30': {'batch_size': 17, 'test_symbols': ['TMF', 'UBT', 'GLD', 'IAU', 'DIA', 'SPY', 'USL', 'DBO', 'BNO', 'DBA', 'CORN', 'WEAT', 'VIXY', 'TNA', 'UPRO', 'SOXL', 'TECL']}, 'var_functions.query_db:32': [{'max_adj_close': '27.289674758911133'}], 'var_functions.query_db:34': [{'max_adj_close': '125.2300033569336'}], 'var_functions.execute_python:36': {'test_count': 33, 'test_symbols': ['SPY', 'IVV', 'VOO', 'DIA', 'XLF', 'XLE', 'XLK', 'XLV', 'XLP', 'XLY', 'XLI', 'XLB', 'XLU', 'XRT', 'GLD', 'SLV', 'FXE', 'FXI', 'FXY', 'EEM', 'EFA', 'EWZ', 'SSO', 'QLD', 'DDM', 'UYG', 'DIG', 'UWM', 'MVV', 'HYG', 'LQD', 'AGG', 'MUB']}, 'var_functions.execute_python:38': {'total_symbols': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:40': [{'symbol': 'SPY', 'max_adj_close': 'nan'}], 'var_functions.execute_python:42': {'sample_size': 50, 'test_symbols': ['UEVM', 'NUAG', 'DVYE', 'EDC', 'FLSW', 'IBDM', 'LOUP', 'JKH', 'SBIO', 'SH', 'SCHZ', 'LDRS', 'AOA', 'TYO', 'RIGS', 'SPEM', 'FNI', 'RWSL', 'SPFF', 'FHLC', 'CZA', 'JHSC', 'EFU', 'PFFD', 'VPL', 'GSEU', 'HDGE', 'XSLV', 'FLTR', 'EWJ', 'ILF', 'IQIN', 'HTEC', 'KOMP', 'MMTM', 'VRAI', 'VIG', 'CHIX', 'TIPZ', 'EPHE', 'SDOW', 'IQSU', 'CNXT', 'ROAM', 'SCIX', 'FLQE', 'EPI', 'FLTW', 'EMMF', 'LEMB']}, 'var_functions.query_db:44': [{'max_price': '120.45299530029295'}], 'var_functions.execute_python:46': {'total_symbols': 1435, 'batch_count': 15, 'priority_symbols': ['TNA', 'FAS', 'SPXL', 'UPRO', 'TECL', 'SOXL', 'UDOW', 'ERX', 'DRN', 'URE', 'TMF', 'TYD', 'TMV', 'TBF', 'SSO', 'QLD', 'DDM', 'MVV', 'SAA', 'UWM', 'UYG', 'DIG', 'SPY', 'IVV', 'VOO', 'DIA', 'GLD', 'IAU', 'OIH', 'XLE', 'XLF']}, 'var_functions.query_db:48': [{'max_price': '48.85812377929688'}], 'var_functions.execute_python:52': {'total_etfs': 1435, 'batch_count': 15, 'priority_etfs': ['SPY', 'IVV', 'VOO', 'DIA', 'IWM', 'MDY', 'IJH', 'IJR', 'XLF', 'XLE', 'XLK', 'XLV', 'XLI', 'XLY', 'XLP', 'XLB', 'XLU', 'VNQ', 'GLD', 'IAU', 'SLV', 'EFA', 'VEA', 'EEM', 'VWO']}, 'var_functions.query_db:54': [{'symbol': 'DIA', 'max_adj_close': 'nan'}], 'var_functions.query_db:56': [{'symbol': 'DIA', 'max_adj_close': '163.6190185546875'}]}

exec(code, env_args)
