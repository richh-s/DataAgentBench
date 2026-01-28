code = """import json

# Get NYSE ARCA ETFs
nyse_arca_path = locals()['var_functions.query_db:0']
with open(nyse_arca_path, 'r') as f:
    nyse_arca_etfs = json.load(f)

nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Let's create batches to test multiple ETFs
# For now, let's test a focused sample of ETFs that might have higher prices
# These include leveraged, inverse, and commodity ETFs

# From the random sample and common knowledge, test these:
test_symbols_batch1 = [
    "TMF", "UBT",  # Leveraged Treasury ETFs
    "GLD", "IAU",  # Gold ETFs
    "DIA", "SPY", "QQQ",  # Major index ETFs
    "USL", "DBO", "BNO",  # Oil ETFs
    "DBA", "CORN", "WEAT",  # Agriculture
    "VIXY", "VXX",  # Volatility
    "TNA", "UPRO", "SOXL", "TECL"  # 3x leveraged
]

# Filter only those that are actually in NYSE Arca
test_symbols_batch1 = [sym for sym in test_symbols_batch1 if sym in nyse_arca_symbols]

print(f"Testing batch of {len(test_symbols_batch1)} ETFs: {test_symbols_batch1}")

result = {
    "batch_size": len(test_symbols_batch1),
    "test_symbols": test_symbols_batch1
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'etfs_with_data': 1435, 'etfs_without_data': 0, 'existing_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'missing_sample': []}, 'var_functions.query_db:18': [], 'var_functions.execute_python:20': {'total_etfs_checked': 1435, 'etfs_above_200': [], 'count': 0}, 'var_functions.query_db:22': [{'Adj Close': '193.3121490478516', 'Date': '2015-07-20'}, {'Adj Close': '193.212158203125', 'Date': '2015-07-17'}, {'Adj Close': '193.1998443603516', 'Date': '2015-05-21'}, {'Adj Close': '193.0484619140625', 'Date': '2015-07-16'}, {'Adj Close': '192.8638153076172', 'Date': '2015-11-03'}], 'var_functions.query_db:24': [{'Adj Close': '110.42893981933594', 'Date': '2015-12-01'}, {'Adj Close': '110.40975952148438', 'Date': '2015-12-04'}, {'Adj Close': '110.29467010498048', 'Date': '2015-11-04'}, {'Adj Close': '110.2851104736328', 'Date': '2015-11-03'}, {'Adj Close': '110.07412719726562', 'Date': '2015-11-06'}], 'var_functions.execute_python:26': {'sample_size': 50, 'etfs_to_test': ['YLD', 'ARKF', 'FNCL', 'FXC', 'MYY', 'WBII', 'SYE', 'DIVA', 'ISMD', 'CNXT', 'XLI', 'PCEF', 'XTH', 'PPSC', 'ICOL', 'TLEH', 'EQAL', 'HEWY', 'UBT', 'RWDC', 'IAI', 'DSTL', 'PALL', 'RLY', 'HIPS', 'PLAT', 'TOK', 'SCID', 'JKF', 'GOEX', 'HDIV', 'IYK', 'SPEM', 'TMF', 'FRAK', 'XOUT', 'FLMX', 'SCHE', 'SPHB', 'DTD', 'AOA', 'VV', 'DLBR', 'PFXF', 'INCO', 'SPMO', 'IYG', 'DYNF', 'NFLT', 'PASS']}, 'var_functions.query_db:28': [{'max_close': '31.778106689453125'}]}

exec(code, env_args)
