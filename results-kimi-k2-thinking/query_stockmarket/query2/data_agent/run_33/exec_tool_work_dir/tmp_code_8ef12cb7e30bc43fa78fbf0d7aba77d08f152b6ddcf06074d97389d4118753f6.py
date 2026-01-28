code = """import json
import sqlite3
import os

# Get the ETF symbols from previous result
etf_list = locals()['var_functions.query_db:0']
etf_symbols = [etf['Symbol'] for etf in etf_list]

# Connect to stocktrade_database and check which symbols have price data tables
# Since this is a DuckDB, we need to use duckdb connector
import duckdb

# We'll build a list to store successful ETFs
high_price_etfs = []

try:
    # Connect to DuckDB
    conn = duckdb.connect('file_storage/stocktrade_database.db')
    
    for symbol in etf_symbols:
        # Sanitize symbol to handle special characters that might affect table names
        # Table names are likely just the symbol
        try:
            # Check if table exists and get max adjusted close in 2015
            query = f'''
                SELECT MAX("Adj Close") as max_adj_close 
                FROM "{symbol}" 
                WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'
            '''
            result = conn.execute(query).fetchone()
            
            if result and result[0] is not None and result[0] > 200:
                high_price_etfs.append({
                    'symbol': symbol,
                    'max_adj_close_2015': result[0]
                })
                
        except Exception as e:
            # Table doesn't exist or other error, skip
            continue
    
    conn.close()
    
    print('__RESULT__:')
    print(json.dumps({
        'count': len(high_price_etfs),
        'etfs': high_price_etfs
    }))
    
except Exception as e:
    print('__RESULT__:')
    print(json.dumps({'error': str(e), 'count': 0, 'etfs': []}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'total_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
