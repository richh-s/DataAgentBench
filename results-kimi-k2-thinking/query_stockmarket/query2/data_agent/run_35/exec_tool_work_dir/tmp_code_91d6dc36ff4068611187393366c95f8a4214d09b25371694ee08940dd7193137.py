code = """import json

# Read NYSE Arca ETFs data
nyse_arca_file = locals()['var_functions.query_db:10']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_data = json.load(f)

# Extract symbols
nyse_arca_symbols = [item['Symbol'] for item in nyse_arca_data]

# Read available tickers
available_tickers_file = locals()['var_functions.list_db:11']
with open(available_tickers_file, 'r') as f:
    available_tickers = json.load(f)

# Find intersection - ETFs that are both NYSE Arca listed AND have price data
available_nyse_arca_etfs = list(set(nyse_arca_symbols) & set(available_tickers))

print('__RESULT__:')
print(json.dumps({
    'total_nyse_arca_etfs': len(nyse_arca_symbols),
    'total_available_tickers': len(available_tickers),
    'available_nyse_arca_etfs': len(available_nyse_arca_etfs),
    'sample_available': sorted(available_nyse_arca_etfs)[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'count': 38, 'sample': 'file_stora', 'first_record': 'f'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:18': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 39, 'available_tickers_type': "<class 'str'>", 'available_tickers_length': 38, 'sample_nyse_arca': 'Not a list', 'sample_tickers': 'Not a list'}, 'var_functions.execute_python:20': {'nyse_arca_etfs_count': 1435, 'available_tickers_count': 2753, 'sample_nyse_arca': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}], 'sample_tickers': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}}

exec(code, env_args)
