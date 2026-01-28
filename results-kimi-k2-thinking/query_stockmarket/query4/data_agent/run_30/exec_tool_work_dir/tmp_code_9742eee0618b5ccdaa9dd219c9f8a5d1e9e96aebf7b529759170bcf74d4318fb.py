code = """import json
import os

# File paths
all_tickers_path = globals()['var_functions.list_db:0']
nyse_records_path = globals()['var_functions.query_db:2']

# Load data
with open(all_tickers_path, "r") as f:
    all_tickers = json.load(f)

with open(nyse_records_path, "r") as f:
    nyse_records = json.load(f)

# Get valid NYSE non-ETF tickers
nyse_tickers = {rec['Symbol'] for rec in nyse_records}
valid_tickers = [t for t in all_tickers if t in nyse_tickers]

# Create a DuckDB query to process all tickers at once using UNION ALL
# This is more efficient than individual queries
queries = []
for i, ticker in enumerate(valid_tickers):
    # Escape ticker if it contains special characters
    safe_ticker = f"\"{ticker}\"" if not ticker.isalnum() else ticker
    query = f"""
    SELECT 
        '{ticker}' as symbol,
        COUNT(CASE WHEN Close > Open THEN 1 END) as up_days,
        COUNT(CASE WHEN Close < Open THEN 1 END) as down_days
    FROM {safe_ticker}
    WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'
    """
    queries.append(query)

# Combine all queries with UNION ALL
full_query = " UNION ALL ".join(queries)

print('__RESULT__:')
print(json.dumps(full_query[:500]))  # Print first part to verify"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': 'file_storage/functions.list_db:0.json', 'var_functions.execute_python:14': {'all_tickers_count': 2753, 'nyse_tickers_count': 234, 'valid_tickers_count': 234}, 'var_functions.execute_python:16': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}

exec(code, env_args)
