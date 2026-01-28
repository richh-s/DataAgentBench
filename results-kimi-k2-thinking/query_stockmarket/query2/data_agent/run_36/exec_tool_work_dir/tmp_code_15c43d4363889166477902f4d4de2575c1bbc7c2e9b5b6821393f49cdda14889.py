code = """import json

# Get the full list of NYSE Arca ETFs
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    etf_symbols = json.load(f)

# Instead of checking all 1435 ETFs individually (which would be too slow),
# let's check ETFs that are most likely to have exceeded $200 in 2015.

# After checking many broad market and commodity ETFs that were <$200, 
# let me check some specialized categories:

# 1. Bond ETFs that might trade at high unit values
bond_etfs = ['BIL', 'SUB', 'MUB', 'TFLO', 'SPTS', 'SPTI', 'SPTL', 'STPZ', 'TIP', 'SCHP', 
             'VTIP', 'STIP', 'TIPX', 'TIPZ', 'SCHO', 'SHY', 'SHV', 'IEI', 'TLH', 'IEF',
             'TLT', 'EDV', 'GOVT', 'VGIT', 'VGLT', 'SPTM', 'SPAB']
bond_etfs = [etf for etf in bond_etfs if etf in etf_symbols]

# 2. Money market / ultra-short term ETFs that might maintain $100+ values
money_market = ['MINT', 'BIL', 'SHV', 'FTSD', 'GSY', 'PULS', 'JPST', 'FTSM', 'FTSL']
money_market = [etf for etf in money_market if etf in etf_symbols]

# 3. Currency ETFs that might have high unit values
currency = ['UUP', 'FXE', 'FXY', 'FXB', 'FXC', 'FXF', 'FXA', 'USDU']
currency = [etf for etf in currency if etf in etf_symbols]

# 4. Some specialized commodity/infrastructure ETFs
specialized = ['GLD', 'IAU', 'PPLT', 'SLV', 'USO', 'UNG', 'BNO', 'DBO', 'DBP', 'GCC']
specialized = [etf for etf in specialized if etf in etf_symbols]

# 5. Dividend aristocrats/value ETFs that might have accumulated
value_div = ['VIG', 'DVY', 'SDY', 'SCHD', 'DGRO', 'HDV', 'DTD', 'DLN', 'FVD', 'NOBL']
value_div = [etf for etf in value_div if etf in etf_symbols]

# Combine all lists and remove duplicates
all_candidates = list(set(bond_etfs + money_market + currency + specialized + value_div))
print(f"Checking {len(all_candidates)} high-probability candidates")
print(f"Sample: {all_candidates[:10]}")

result = all_candidates
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:34': ['SPY', 'IVV', 'VOO', 'VTI', 'GLD', 'PPLT', 'GLDM', 'SLV', 'AGG', 'SSO', 'QLD', 'DDM'], 'var_functions.execute_python:36': ['AAAU', 'ARKF', 'AFMC', 'EMLC', 'ASHR', 'AMOM', 'HYG', 'AOK', 'BCD', 'ARMR', 'BBP', 'ARGT', 'ASHS', 'PPLT', 'AGG', 'AFLG', 'LQD', 'AOR', 'ACWF', 'USO', 'UNG', 'IAU', 'SLV', 'ASHX', 'ASEA', 'AVUV', 'AVDE', 'AXJL', 'BCI', 'AVEM', 'AOM', 'AWAY', 'AUSF', 'AVUS', 'BAB', 'AGZ', 'AGGP', 'AFSM', 'AFK', 'AIIQ', 'ARKK', 'AIEQ', 'AMLP', 'AGQ', 'BATT', 'ARKW', 'AWTM', 'BDCY', 'ACSG', 'NUGT', 'ABEQ', 'AMZA', 'BDRY', 'AVDV', 'AOA', 'GLD', 'AADR', 'AGGY', 'BBC', 'AFTY'], 'var_functions.query_db:38': [{'Symbol': 'SSO', 'max_price': '66.95523071289062'}], 'var_functions.execute_python:40': {'total_etfs': 1435, 'commodity_etfs': ['GLD', 'IAU', 'SLV', 'PPLT', 'NUGT', 'USO', 'UNG'], 'bond_etfs': ['LQD', 'HYG'], 'leveraged_etfs': ['SSO', 'QLD', 'DDM', 'UPRO']}, 'var_functions.execute_python:42': ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'VUG', 'MGK', 'IWF', 'GLD', 'IAU', 'PPLT', 'SLV', 'SSO', 'QLD', 'DDM', 'UPRO'], 'var_functions.execute_python:44': ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'QLD', 'GLD', 'IAU', 'PPLT', 'SLV', 'NUGT', 'SSO', 'UPRO', 'DDM', 'MZZ', 'LQD', 'HYG', 'EMLC', 'DIA', 'DOG', 'DXD', 'SDOW'], 'var_functions.query_db:46': [{'Symbol': 'GLD', 'max_price': '125.2300033569336', 'min_price': '100.5'}], 'var_functions.query_db:48': [{'Symbol': 'IVV', 'max_price': '193.5270538330078', 'min_price': '170.37913513183594'}], 'var_functions.query_db:50': [{'Symbol': 'TLT', 'max_price': '121.58584594726562'}], 'var_functions.query_db:52': [{'Symbol': 'IAU', 'max_price': '12.619999885559082'}], 'var_functions.query_db:54': [{'Symbol': 'UPRO', 'max_price': '24.036970138549805'}], 'var_functions.query_db:56': [{'Symbol': 'PPLT', 'max_price': '124.6999969482422'}], 'var_functions.execute_python:58': ['LQD', 'HYG', 'EMLC', 'MUB', 'AGG', 'TIP', 'MINT', 'SUB', 'BIL', 'UUP', 'FXE', 'FXY', 'GLD', 'IAU', 'SLV', 'USO', 'UNG', 'VIG', 'SCHD', 'DGRO', 'TBT', 'TMF', 'TMV']}

exec(code, env_args)
