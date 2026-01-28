code = """import json
import duckdb

# Read the ETF list from the file
with open('file_storage/stocktrade_database.json', 'r') as f:
    etf_list = json.load(f)

# Get ETF symbols from NYSE Arca (listing exchange 'P')
etf_symbols = [etf['Symbol'] for etf in etf_list]

# Connect to DuckDB
conn = duckdb.connect('file_storage/stocktrade_database.db')

# Find ETFs with adjusted closing price > $200 in 2015
high_price_etfs = []

for symbol in etf_symbols:
    try:
        # Check if table exists and get max adjusted close price in 2015
        query = f"""
            SELECT MAX("Adj Close") as max_adj_close 
            FROM "{symbol}" 
            WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'
        """
        result = conn.execute(query).fetchone()
        
        if result and result[0] is not None and result[0] > 200:
            high_price_etfs.append({
                'symbol': symbol,
                'max_adj_close_2015': float(result[0])
            })
    except:
        # Skip if table doesn't exist or other errors
        continue

conn.close()

# Sort by max price descending
high_price_etfs.sort(key=lambda x: x['max_adj_close_2015'], reverse=True)

result_data = {
    'total_etfs_found': len(high_price_etfs),
    'etfs': high_price_etfs
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
