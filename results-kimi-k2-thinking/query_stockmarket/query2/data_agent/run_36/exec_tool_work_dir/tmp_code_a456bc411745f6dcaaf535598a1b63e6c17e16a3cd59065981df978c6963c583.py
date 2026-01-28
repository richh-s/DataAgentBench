code = """import json

# Get the full list of NYSE Arca ETFs
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    nysearca_etfs = json.load(f)

print(f"Total NYSE Arca ETFs to process: {len(nysearca_etfs)}")

# To avoid timeout, let's start with ETFs most likely to exceed $200 in 2015
# Based on 2015 market data, these are the categories:

# Category 1: Broad Market ETFs (should be close to $200+ range since S&P 500 hit 2130 in 2015)
broad_market = ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG']

# Category 2: Large Cap Growth (QQQ and related - might be close)
tech_large = ['QQQ', 'QTEC', 'VUG', 'MGK', 'IWF']

# Category 3: Precious Metals (different price scales)
metals = ['GLD', 'IAU', 'PPLT', 'SLV']

# Category 4: Leveraged Broad Market (2x, 3x - adjusted for splits)
leveraged = ['SSO', 'QLD', 'DDM', 'UPRO', 'TQQQ']

# Combine all candidates and filter to only NYSE Arca listed
candidate_symbols = []
for etf in (broad_market + tech_large + metals + leveraged):
    if etf in nysearca_etfs:
        candidate_symbols.append(etf)

print(f"High-priority candidates: {candidate_symbols}")
print(f"Will query these first, then batch process remaining {len(nysearca_etfs) - len(candidate_symbols)} ETFs")

result = candidate_symbols
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:34': ['SPY', 'IVV', 'VOO', 'VTI', 'GLD', 'PPLT', 'GLDM', 'SLV', 'AGG', 'SSO', 'QLD', 'DDM'], 'var_functions.execute_python:36': ['AAAU', 'ARKF', 'AFMC', 'EMLC', 'ASHR', 'AMOM', 'HYG', 'AOK', 'BCD', 'ARMR', 'BBP', 'ARGT', 'ASHS', 'PPLT', 'AGG', 'AFLG', 'LQD', 'AOR', 'ACWF', 'USO', 'UNG', 'IAU', 'SLV', 'ASHX', 'ASEA', 'AVUV', 'AVDE', 'AXJL', 'BCI', 'AVEM', 'AOM', 'AWAY', 'AUSF', 'AVUS', 'BAB', 'AGZ', 'AGGP', 'AFSM', 'AFK', 'AIIQ', 'ARKK', 'AIEQ', 'AMLP', 'AGQ', 'BATT', 'ARKW', 'AWTM', 'BDCY', 'ACSG', 'NUGT', 'ABEQ', 'AMZA', 'BDRY', 'AVDV', 'AOA', 'GLD', 'AADR', 'AGGY', 'BBC', 'AFTY'], 'var_functions.query_db:38': [{'Symbol': 'SSO', 'max_price': '66.95523071289062'}], 'var_functions.execute_python:40': {'total_etfs': 1435, 'commodity_etfs': ['GLD', 'IAU', 'SLV', 'PPLT', 'NUGT', 'USO', 'UNG'], 'bond_etfs': ['LQD', 'HYG'], 'leveraged_etfs': ['SSO', 'QLD', 'DDM', 'UPRO']}}

exec(code, env_args)
