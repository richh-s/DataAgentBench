code = """import json
import duckdb

# Read the ETF list from file
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_list = json.load(f)

# Get ETF symbols
etf_symbols = [etf['Symbol'] for etf in etf_list]

# Connect to DuckDB
conn = duckdb.connect('file_storage/stocktrade_database.db')

# List to store qualifying ETFs
qualifying_etfs = []

# Check each ETF symbol
for symbol in etf_symbols:
    try:
        # Query for max adjusted close in 2015
        query = 'SELECT MAX("Adj Close") FROM "{}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\''.format(symbol)
        result = conn.execute(query).fetchone()
        
        if result and result[0] is not None and result[0] > 200:
            qualifying_etfs.append({
                'symbol': symbol,
                'max_adj_close': float(result[0])
            })
    except:
        continue

conn.close()

# Sort by max price descending
qualifying_etfs.sort(key=lambda x: x['max_adj_close'], reverse=True)

# Prepare result
result = {
    'total_count': len(qualifying_etfs),
    'etfs': qualifying_etfs
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
