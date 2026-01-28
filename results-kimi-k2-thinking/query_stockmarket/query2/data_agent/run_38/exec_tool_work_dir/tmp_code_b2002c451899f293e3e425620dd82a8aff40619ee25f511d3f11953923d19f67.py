code = """import json

# Read the list of NYSE Arca ETFs
nyse_arca_file = locals()['var_functions.query_db:2']
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Create a dictionary to store which ETFs meet the criteria
etfs_above_200 = []

# For each symbol, we'll need to check if it exists in the stocktrade_db and query it
# Let's start by creating the queries we need
queries = []
for symbol in nyse_arca_symbols[:50]:  # Test with first 50 to avoid overwhelming the system
    query = f"""SELECT '{symbol}' as Symbol, COUNT(*) as count FROM "{symbol}" 
                 WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' 
                 AND "Adj Close" > 200.0"""
    queries.append(query)

print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(nyse_arca_symbols),
    'sample_symbols': nyse_arca_symbols[:10],
    'sample_queries': queries[:3]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:10': {'nyse_arca_etfs_type': "<class 'str'>", 'nyse_arca_etfs_length': 38, 'nyse_arca_etfs_sample': 'fil', 'all_tables_type': "<class 'str'>", 'all_tables_length': 37, 'all_tables_sample': 'fil'}, 'var_functions.execute_python:12': {'total_nyse_arca_etfs': 1435, 'total_tables_in_db': 2753, 'etfs_with_price_data': 1435, 'sample_etfs': ['CGW', 'EZA', 'AIIQ', 'CORN', 'HDMV', 'MDY', 'VB', 'TIPX', 'EDIV', 'TLH']}}

exec(code, env_args)
