code = """import json

# Based on extensive checking of ETFs and finding none above $200 in 2015,
# let me do a final systematic check of a few remaining categories

nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    etf_symbols = json.load(f)

# Check some final categories that might have edge cases:
# 1. Some specialty bond ETFs
# 2. Some target risk/volatility ETFs
# 3. Some allocation ETFs that might have accumulated value

final_candidates = [
    # Specialty bond/fixed income
    'FTSM', 'JPST', 'MINT', 'PULS', 'FTSD', 'GSY', 'BIL', 'SPTS', 
    # Target allocation
    'AOK', 'AOM', 'AOR', 'AOA', 'TSLA', 'GLIF',
    # Specialty equity
    'DIA', 'MGC', 'MGK', 'MGV', 'VONE', 'VTHR',
    # Some potential high-value outliers
    'STIP', 'TIP', 'VTIP', 'SCHP', 'TIPX', 'TIPZ'
]

final_candidates = [etf for etf in final_candidates if etf in etf_symbols]

# Remove duplicates and sort
final_candidates = sorted(list(set(final_candidates)))

print(f"Final comprehensive check of {len(final_candidates)} ETFs")
print(f"List: {final_candidates}")

# Let's also check if any ETF in the entire dataset exceeds 200
# by querying a few random ones we haven't checked

random_sample = [etf for etf in etf_symbols if etf not in final_candidates][:10]
print(f"Random sample for double-check: {random_sample}")

result = {
    'final_candidates': final_candidates,
    'random_sample': random_sample
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:34': ['SPY', 'IVV', 'VOO', 'VTI', 'GLD', 'PPLT', 'GLDM', 'SLV', 'AGG', 'SSO', 'QLD', 'DDM'], 'var_functions.execute_python:36': ['AAAU', 'ARKF', 'AFMC', 'EMLC', 'ASHR', 'AMOM', 'HYG', 'AOK', 'BCD', 'ARMR', 'BBP', 'ARGT', 'ASHS', 'PPLT', 'AGG', 'AFLG', 'LQD', 'AOR', 'ACWF', 'USO', 'UNG', 'IAU', 'SLV', 'ASHX', 'ASEA', 'AVUV', 'AVDE', 'AXJL', 'BCI', 'AVEM', 'AOM', 'AWAY', 'AUSF', 'AVUS', 'BAB', 'AGZ', 'AGGP', 'AFSM', 'AFK', 'AIIQ', 'ARKK', 'AIEQ', 'AMLP', 'AGQ', 'BATT', 'ARKW', 'AWTM', 'BDCY', 'ACSG', 'NUGT', 'ABEQ', 'AMZA', 'BDRY', 'AVDV', 'AOA', 'GLD', 'AADR', 'AGGY', 'BBC', 'AFTY'], 'var_functions.query_db:38': [{'Symbol': 'SSO', 'max_price': '66.95523071289062'}], 'var_functions.execute_python:40': {'total_etfs': 1435, 'commodity_etfs': ['GLD', 'IAU', 'SLV', 'PPLT', 'NUGT', 'USO', 'UNG'], 'bond_etfs': ['LQD', 'HYG'], 'leveraged_etfs': ['SSO', 'QLD', 'DDM', 'UPRO']}, 'var_functions.execute_python:42': ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'VUG', 'MGK', 'IWF', 'GLD', 'IAU', 'PPLT', 'SLV', 'SSO', 'QLD', 'DDM', 'UPRO'], 'var_functions.execute_python:44': ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'QLD', 'GLD', 'IAU', 'PPLT', 'SLV', 'NUGT', 'SSO', 'UPRO', 'DDM', 'MZZ', 'LQD', 'HYG', 'EMLC', 'DIA', 'DOG', 'DXD', 'SDOW'], 'var_functions.query_db:46': [{'Symbol': 'GLD', 'max_price': '125.2300033569336', 'min_price': '100.5'}], 'var_functions.query_db:48': [{'Symbol': 'IVV', 'max_price': '193.5270538330078', 'min_price': '170.37913513183594'}], 'var_functions.query_db:50': [{'Symbol': 'TLT', 'max_price': '121.58584594726562'}], 'var_functions.query_db:52': [{'Symbol': 'IAU', 'max_price': '12.619999885559082'}], 'var_functions.query_db:54': [{'Symbol': 'UPRO', 'max_price': '24.036970138549805'}], 'var_functions.query_db:56': [{'Symbol': 'PPLT', 'max_price': '124.6999969482422'}], 'var_functions.execute_python:58': ['LQD', 'HYG', 'EMLC', 'MUB', 'AGG', 'TIP', 'MINT', 'SUB', 'BIL', 'UUP', 'FXE', 'FXY', 'GLD', 'IAU', 'SLV', 'USO', 'UNG', 'VIG', 'SCHD', 'DGRO', 'TBT', 'TMF', 'TMV'], 'var_functions.execute_python:60': ['DBP', 'SPTS', 'STPZ', 'FXF', 'SLV', 'SPTM', 'DTD', 'FXA', 'UNG', 'FVD', 'USDU', 'UUP', 'HDV', 'MUB', 'SCHP', 'GSY', 'DGRO', 'STIP', 'MINT', 'PULS', 'EDV', 'FXE', 'VIG', 'GLD', 'TFLO', 'DBO', 'SCHD', 'TIPZ', 'TIPX', 'SCHO', 'SUB', 'FXB', 'BNO', 'TIP', 'TLH', 'IAU', 'FXC', 'SPTL', 'PPLT', 'SDY', 'BIL', 'DLN', 'GCC', 'FXY', 'FTSD', 'SPAB', 'SPTI', 'USO'], 'var_functions.query_db:62': [{'Adj Close': '117.01538848876952'}], 'var_functions.query_db:64': [{'Symbol': 'BIL', 'max_price': '87.24989318847656'}], 'var_functions.execute_python:66': ['AOR', 'AOM', 'AOK', 'AOA', 'BLV', 'IGLB', 'LQDH', 'EMBH', 'PICB', 'CORP', 'BIV', 'VIG', 'SDY', 'DGRO', 'SCHD', 'HDV', 'DTD', 'DLN', 'FVD'], 'var_functions.query_db:68': [{'Symbol': 'SDY', 'max_price': '65.51783752441406'}]}

exec(code, env_args)
