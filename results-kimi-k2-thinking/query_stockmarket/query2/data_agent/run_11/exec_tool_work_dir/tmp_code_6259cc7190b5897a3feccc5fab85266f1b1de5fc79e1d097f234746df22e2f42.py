code = """import json

# Get NYSE ARCA ETFs
nyse_arca_path = locals()['var_functions.query_db:0']
with open(nyse_arca_path, 'r') as f:
    nyse_arca_etfs = json.load(f)

nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# More comprehensive list of ETFs to test that might have higher prices
# Including index ETFs, some leveraged/inverse, and older established ETFs
focused_test = [
    # Major index ETFs
    "SPY", "IVV", "VOO", "DIA", "QQQ",
    # Sector SPDRs and similar
    "XLF", "XLE", "XLK", "XLV", "XLP", "XLY", "XLI", "XLB", "XLU", "XRT",
    # Commodity/FX
    "GLD", "SLV", "FXE", "FXI", "FXY", "EEM", "EFA", "EWZ",
    # Leveraged/inverse
    "SSO", "QLD", "DDM", "UYG", "DIG", "UWM", "MVV",
    # Bond/fixed income
    "TLT", "HYG", "LQD", "IEF", "SHY", "AGG", "MUB"  
]

# Filter only those in NYSE Arca
focused_test = [sym for sym in focused_test if sym in nyse_arca_symbols]

print(f"Comprehensive test of {len(focused_test)} ETFs")

result = {
    "test_count": len(focused_test),
    "test_symbols": focused_test
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'etfs_with_data': 1435, 'etfs_without_data': 0, 'existing_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'missing_sample': []}, 'var_functions.query_db:18': [], 'var_functions.execute_python:20': {'total_etfs_checked': 1435, 'etfs_above_200': [], 'count': 0}, 'var_functions.query_db:22': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}], 'var_functions.query_db:24': [{'Adj Close': '110.42893981933594', 'Date': '2015-12-01'}, {'Adj Close': '110.40975952148438', 'Date': '2015-12-04'}, {'Adj Close': '110.29467010498048', 'Date': '2015-11-04'}, {'Adj Close': '110.2851104736328', 'Date': '2015-11-03'}, {'Adj Close': '110.07412719726562', 'Date': '2015-11-06'}], 'var_functions.execute_python:26': {'sample_size': 50, 'etfs_to_test': ['YLD', 'ARKF', 'FNCL', 'FXC', 'MYY', 'WBII', 'SYE', 'DIVA', 'ISMD', 'CNXT', 'XLI', 'PCEF', 'XTH', 'PPSC', 'ICOL', 'TLEH', 'EQAL', 'HEWY', 'UBT', 'RWDC', 'IAI', 'DSTL', 'PALL', 'RLY', 'HIPS', 'PLAT', 'TOK', 'SCID', 'JKF', 'GOEX', 'HDIV', 'IYK', 'SPEM', 'TMF', 'FRAK', 'XOUT', 'FLMX', 'SCHE', 'SPHB', 'DTD', 'AOA', 'VV', 'DLBR', 'PFXF', 'INCO', 'SPMO', 'IYG', 'DYNF', 'NFLT', 'PASS']}, 'var_functions.query_db:28': [{'max_close': '31.778106689453125'}], 'var_functions.execute_python:30': {'batch_size': 17, 'test_symbols': ['TMF', 'UBT', 'GLD', 'IAU', 'DIA', 'SPY', 'USL', 'DBO', 'BNO', 'DBA', 'CORN', 'WEAT', 'VIXY', 'TNA', 'UPRO', 'SOXL', 'TECL']}, 'var_functions.query_db:32': [{'max_adj_close': '27.289674758911133'}], 'var_functions.query_db:34': [{'max_adj_close': '125.2300033569336'}]}

exec(code, env_args)
