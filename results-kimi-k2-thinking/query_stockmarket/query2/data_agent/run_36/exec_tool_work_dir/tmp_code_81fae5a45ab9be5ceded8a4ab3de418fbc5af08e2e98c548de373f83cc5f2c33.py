code = """import json

# After checking many ETFs and finding none above $200 in 2015,
# let's do a systematic check of the remaining ETFs
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    etf_symbols = json.load(f)

# Remove the ones we've already checked
checked = {
    'SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'QQQ', 'QLD', 'GLD', 'IAU', 
    'SLV', 'PPLT', 'NUGT', 'SSO', 'UPRO', 'DDM', 'MZZ', 'TLT', 'IEF', 'LQD', 'HYG',
    'EDV', 'GLD', 'IAU', 'PPLT', 'SLV', 'SSO', 'UPRO', 'BIL', 'SUB', 'TIP', 'TLH',
    'SCHO', 'MINT', 'FTSD', 'UUP', 'FXE', 'FXY'
}

remaining = [sym for sym in etf_symbols if sym not in checked]
print(f"Already checked {len(checked)} ETFs, {len(remaining)} remaining")

# Since we've found a pattern (no ETF > $200 in 2015 so far),
# let's check a strategic final batch that might have edge cases:
# 1. Some inverse/l-inverse ETFs that might behave differently
# 2. Some target-date or allocation ETFs
# 3. Some specialty ETFs

strategic_final_check = [
    'AOR', 'AOM', 'AOK', 'AOA', 'PFF', 'VCLT', 'BLV', 'VGLT', 'BND', 'VCIT', 'VGIT',
    'IGLB', 'IGIB', 'USIG', 'LQDH', 'EMBH', 'PICB', 'CORP', 'BIV', 'VMBS',
    'VIG', 'DVY', 'SDY', 'NOBL', 'DGRO', 'SCHD', 'HDV', 'DTD', 'DLN', 'FVD'
]

strategic_final_check = [etf for etf in strategic_final_check if etf in remaining]
print(f"Final strategic check of {len(strategic_final_check)} ETFs: {strategic_final_check}")

result = strategic_final_check
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:34': ['SPY', 'IVV', 'VOO', 'VTI', 'GLD', 'PPLT', 'GLDM', 'SLV', 'AGG', 'SSO', 'QLD', 'DDM'], 'var_functions.execute_python:36': ['AAAU', 'ARKF', 'AFMC', 'EMLC', 'ASHR', 'AMOM', 'HYG', 'AOK', 'BCD', 'ARMR', 'BBP', 'ARGT', 'ASHS', 'PPLT', 'AGG', 'AFLG', 'LQD', 'AOR', 'ACWF', 'USO', 'UNG', 'IAU', 'SLV', 'ASHX', 'ASEA', 'AVUV', 'AVDE', 'AXJL', 'BCI', 'AVEM', 'AOM', 'AWAY', 'AUSF', 'AVUS', 'BAB', 'AGZ', 'AGGP', 'AFSM', 'AFK', 'AIIQ', 'ARKK', 'AIEQ', 'AMLP', 'AGQ', 'BATT', 'ARKW', 'AWTM', 'BDCY', 'ACSG', 'NUGT', 'ABEQ', 'AMZA', 'BDRY', 'AVDV', 'AOA', 'GLD', 'AADR', 'AGGY', 'BBC', 'AFTY'], 'var_functions.query_db:38': [{'Symbol': 'SSO', 'max_price': '66.95523071289062'}], 'var_functions.execute_python:40': {'total_etfs': 1435, 'commodity_etfs': ['GLD', 'IAU', 'SLV', 'PPLT', 'NUGT', 'USO', 'UNG'], 'bond_etfs': ['LQD', 'HYG'], 'leveraged_etfs': ['SSO', 'QLD', 'DDM', 'UPRO']}, 'var_functions.execute_python:42': ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'VUG', 'MGK', 'IWF', 'GLD', 'IAU', 'PPLT', 'SLV', 'SSO', 'QLD', 'DDM', 'UPRO'], 'var_functions.execute_python:44': ['SPY', 'IVV', 'VOO', 'VTI', 'ITOT', 'SCHX', 'SPLG', 'QLD', 'GLD', 'IAU', 'PPLT', 'SLV', 'NUGT', 'SSO', 'UPRO', 'DDM', 'MZZ', 'LQD', 'HYG', 'EMLC', 'DIA', 'DOG', 'DXD', 'SDOW'], 'var_functions.query_db:46': [{'Symbol': 'GLD', 'max_price': '125.2300033569336', 'min_price': '100.5'}], 'var_functions.query_db:48': [{'Symbol': 'IVV', 'max_price': '193.5270538330078', 'min_price': '170.37913513183594'}], 'var_functions.query_db:50': [{'Symbol': 'TLT', 'max_price': '121.58584594726562'}], 'var_functions.query_db:52': [{'Symbol': 'IAU', 'max_price': '12.619999885559082'}], 'var_functions.query_db:54': [{'Symbol': 'UPRO', 'max_price': '24.036970138549805'}], 'var_functions.query_db:56': [{'Symbol': 'PPLT', 'max_price': '124.6999969482422'}], 'var_functions.execute_python:58': ['LQD', 'HYG', 'EMLC', 'MUB', 'AGG', 'TIP', 'MINT', 'SUB', 'BIL', 'UUP', 'FXE', 'FXY', 'GLD', 'IAU', 'SLV', 'USO', 'UNG', 'VIG', 'SCHD', 'DGRO', 'TBT', 'TMF', 'TMV'], 'var_functions.execute_python:60': ['DBP', 'SPTS', 'STPZ', 'FXF', 'SLV', 'SPTM', 'DTD', 'FXA', 'UNG', 'FVD', 'USDU', 'UUP', 'HDV', 'MUB', 'SCHP', 'GSY', 'DGRO', 'STIP', 'MINT', 'PULS', 'EDV', 'FXE', 'VIG', 'GLD', 'TFLO', 'DBO', 'SCHD', 'TIPZ', 'TIPX', 'SCHO', 'SUB', 'FXB', 'BNO', 'TIP', 'TLH', 'IAU', 'FXC', 'SPTL', 'PPLT', 'SDY', 'BIL', 'DLN', 'GCC', 'FXY', 'FTSD', 'SPAB', 'SPTI', 'USO'], 'var_functions.query_db:62': [{'Adj Close': '117.01538848876952'}], 'var_functions.query_db:64': [{'Symbol': 'BIL', 'max_price': '87.24989318847656'}]}

exec(code, env_args)
