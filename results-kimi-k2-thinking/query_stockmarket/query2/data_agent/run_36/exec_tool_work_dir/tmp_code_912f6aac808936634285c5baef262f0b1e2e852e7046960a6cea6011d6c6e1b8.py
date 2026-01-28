code = """import json

# Get the list of NYSE Arca ETFs
nysearca_file = locals()['var_functions.execute_python:10']
with open(nysearca_file, 'r') as f:
    nysearca_etfs = json.load(f)

# Check a sample of these ETFs systematically
# Let's start with the first 50 and some known high-value ETFs
sample_etfs = nysearca_etfs[:50]

# Add some specific ETFs that might have high prices based on their nature
high_price_candidates = ['GLD', 'PPLT', 'SLV', 'IAU', 'NUGT', 'USO', 'UNG', 'TLT', 'IEF', 'LQD', 'HYG', 'EMLC']
high_price_candidates = [etf for etf in high_price_candidates if etf in nysearca_etfs]
sample_etfs = list(set(sample_etfs + high_price_candidates))

print(f"Will check {len(sample_etfs)} ETFs: {sorted(sample_etfs)}")
print('__RESULT__:')
print(json.dumps(sample_etfs))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}, {'Date': '1993-02-01', 'Open': '43.96875', 'High': '44.25', 'Low': '43.96875', 'Close': '44.25', 'Adj Close': '26.48632431030273', 'Volume': '480500'}, {'Date': '1993-02-02', 'Open': '44.21875', 'High': '44.375', 'Low': '44.125', 'Close': '44.34375', 'Adj Close': '26.54244804382324', 'Volume': '201300'}], 'var_functions.execute_python:14': {'etf_count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'max_adj_close': '193.5270538330078'}], 'var_functions.execute_python:26': {'total': 1435, 'candidates': ['SPY', 'IVV', 'VOO', 'VTI', 'VUG', 'VTV'], 'batch1_count': 100}, 'var_functions.query_db:28': [{'max_adj_close': '177.17626953125'}], 'var_functions.query_db:30': [{'Symbol': 'IVV', 'max_adj_close': 'nan'}], 'var_functions.query_db:32': [{'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:34': ['SPY', 'IVV', 'VOO', 'VTI', 'GLD', 'PPLT', 'GLDM', 'SLV', 'AGG', 'SSO', 'QLD', 'DDM']}

exec(code, env_args)
