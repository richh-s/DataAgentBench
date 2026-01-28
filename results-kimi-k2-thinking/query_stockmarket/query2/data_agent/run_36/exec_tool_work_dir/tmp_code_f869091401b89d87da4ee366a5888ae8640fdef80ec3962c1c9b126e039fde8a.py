code = """import json
import os

# Get the file path for the full ETF list
nysearca_file = locals()['var_functions.execute_python:10']

# Read the full list of NYSE Arca ETFs
with open(nysearca_file, 'r') as f:
    nysearca_etfs = json.load(f)

print(f"Total NYSE Arca ETFs available: {len(nysearca_etfs)}")

# Let's batch process these ETFs in smaller chunks to find which exceeded $200 in 2015
# We'll create batches and check them systematically

# First, let's understand what we're looking for:
# ETFs that at ANY POINT in 2015 had "Adj Close" > 200

# Given that SPY maxed at ~193 in 2015, we need special ETFs:
# 1. ETFs that track high-price commodities
# 2. ETFs that had split adjustments making historical prices appear higher
# 3. Currency or bond ETFs with high unit values
# 4. Possibly some errors in data

# Let's start by checking a representative sample including commodity ETFs
commodity_etfs = [etf for etf in ['GLD', 'IAU', 'SLV', 'PPLT', 'NUGT', 'USO', 'UNG'] if etf in nysearca_etfs]
bond_etfs = [etf for etf in ['TLT', 'IEF', 'LQD', 'HYG'] if etf in nysearca_etfs]
leveraged_etfs = [etf for etf in ['SSO', 'QLD', 'DDM', 'UPRO', 'TQQQ'] if etf in nysearca_etfs]

print(f"Commodity ETFs: {commodity_etfs}")
print(f"Bond ETFs: {bond_etfs}")
print(f"Leveraged ETFs: {leveraged_etfs}")

result = {
    'total_etfs': len(nysearca_etfs),
    'commodity_etfs': commodity_etfs,
    'bond_etfs': bond_etfs,
    'leveraged_etfs': leveraged_etfs
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:34': ['SPY', 'IVV', 'VOO', 'VTI', 'GLD', 'PPLT', 'GLDM', 'SLV', 'AGG', 'SSO', 'QLD', 'DDM'], 'var_functions.execute_python:36': ['AAAU', 'ARKF', 'AFMC', 'EMLC', 'ASHR', 'AMOM', 'HYG', 'AOK', 'BCD', 'ARMR', 'BBP', 'ARGT', 'ASHS', 'PPLT', 'AGG', 'AFLG', 'LQD', 'AOR', 'ACWF', 'USO', 'UNG', 'IAU', 'SLV', 'ASHX', 'ASEA', 'AVUV', 'AVDE', 'AXJL', 'BCI', 'AVEM', 'AOM', 'AWAY', 'AUSF', 'AVUS', 'BAB', 'AGZ', 'AGGP', 'AFSM', 'AFK', 'AIIQ', 'ARKK', 'AIEQ', 'AMLP', 'AGQ', 'BATT', 'ARKW', 'AWTM', 'BDCY', 'ACSG', 'NUGT', 'ABEQ', 'AMZA', 'BDRY', 'AVDV', 'AOA', 'GLD', 'AADR', 'AGGY', 'BBC', 'AFTY'], 'var_functions.query_db:38': [{'Symbol': 'SSO', 'max_price': '66.95523071289062'}]}

exec(code, env_args)
