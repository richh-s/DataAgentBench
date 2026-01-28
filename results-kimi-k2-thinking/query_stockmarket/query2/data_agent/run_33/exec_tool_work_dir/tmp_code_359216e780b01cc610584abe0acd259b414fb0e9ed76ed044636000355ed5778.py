code = """import json
import duckdb

# Read the ETF list from NYSE Arca
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_list = json.load(f)

# Get the symbols as a set for fast lookup
nyse_arca_etf_symbols = {etf['Symbol'] for etf in etf_list}

# Read the list of all tables in stocktrade_database
with open('file_storage/functions.query_db:26.json', 'r') as f:
    all_tables_data = json.load(f)

# Get all table names that are in our NYSE Arca ETF list
all_table_names = {row['name'] for row in all_tables_data}
etf_tables = nyse_arca_etf_symbols.intersection(all_table_names)

# Connect to DuckDB
conn = duckdb.connect('file_storage/stocktrade_database.db')

# Find ETFs with adjusted closing price > $200 in 2015
qualifying_etfs = []

for symbol in sorted(etf_tables):
    try:
        # Query for max adjusted close in 2015
        query = f"""SELECT MAX("Adj Close") as max_adj_close 
                     FROM "{symbol}" 
                     WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"""
        result = conn.execute(query).fetchone()
        
        if result and result[0] is not None and float(result[0]) > 200:
            qualifying_etfs.append({
                'symbol': symbol,
                'max_adj_close': float(result[0])
            })
    except Exception as e:
        # Skip if table doesn't exist or other errors
        continue

conn.close()

# Sort by max price descending
qualifying_etfs.sort(key=lambda x: x['max_adj_close'], reverse=True)

# Prepare final result
result = {
    'total_count': len(qualifying_etfs),
    'etfs': qualifying_etfs
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:16': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
