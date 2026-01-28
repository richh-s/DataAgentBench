code = """import json

# Get the valid tickers from previous result
valid_tickers = locals()['var_functions.execute_python:8']

# Filter valid tickers (remove tickers with special characters that might cause SQL issues)
clean_tickers = [ticker for ticker in valid_tickers if ticker.replace('_', '').replace('-', '').isalnum()]

print(f'Clean tickers: {len(clean_tickers)}')
print('__RESULT__:')
print(json.dumps(clean_tickers[:10]))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}

exec(code, env_args)
