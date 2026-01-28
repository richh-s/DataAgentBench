code = """import json

# Based on 2015 market data and ETF characteristics, let's identify potential candidates
# Most ETFs won't reach $200, but some might:

# 1. Broad market ETFs (S&P 500, Total Market) - around $180-210 range in 2015
# 2. Commodity ETFs (GLD, PPLT, etc.) - precious metals
# 3. Some leveraged/inverse ETFs (though adjustments for splits make this complex)
# 4. Bond ETFs with high prices

# Let's systematically check a reasonable subset based on 2015 data

# First, let's check several categories:
candidates = [
    # Broad Market (likely above or near $200)
    'SPY', 'IVV', 'VOO', 'VTI', 
    # Tech-heavy (QQQ, etc. likely under $200 in 2015)
    'QQQ', 
    # High-priced commodity ETFs
    'GLD', 'PPLT', 'GLDM', 'SLV',
    # Some bond ETFs
    'TLT', 'IEF', 'BND', 'AGG',
    # Leveraged (be careful with adjustments)
    'SSO', 'QLD', 'DDM'
]

# Get only those that are NYSE Arca listed
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    nysearca_etfs = json.load(f)

nysearca_set = set(nysearca_etfs)
candidates = [etf for etf in candidates if etf in nysearca_set]

print(f"Checking {len(candidates)} potential candidates: {candidates}")

result = candidates
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}]}

exec(code, env_args)
