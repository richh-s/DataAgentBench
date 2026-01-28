code = """import json
import os

# Get the list of NYSE Arca ETFs
etfs_file_path = locals()['var_functions.query_db:0']
with open(etfs_file_path, 'r') as f:
    etfs_data = json.load(f)

nyse_arca_etfs = [etf['Symbol'] for etf in etfs_data]

# Function to check if an ETF reached > $200 in 2015
def check_etf_price(ticker):
    query = f'SELECT Date, "Adj Close" FROM "{ticker}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1;'
    return query

# Test with a few ETFs first
sample_etfs = nyse_arca_etfs[:5]
for ticker in sample_etfs:
    query = check_etf_price(ticker)
    print(f"Ticker: {ticker}, Query: {query}")

print('__RESULT__:')
print(json.dumps({'sample_etfs': sample_etfs, 'total_etfs': len(nyse_arca_etfs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'etf_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_count': 1435}, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': {'nyse_arca_etfs': 1435, 'total_tables': 2753, 'available_etfs': 1435, 'sample_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': []}

exec(code, env_args)
