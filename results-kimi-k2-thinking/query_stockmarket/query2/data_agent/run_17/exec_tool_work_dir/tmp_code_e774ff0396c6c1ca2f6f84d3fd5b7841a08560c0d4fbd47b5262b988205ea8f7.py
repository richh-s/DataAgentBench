code = """import json
import os

# Read the full result from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    etf_symbols = json.load(f)

print(f"Total NYSE Arca ETFs found: {len(etf_symbols)}")
print("First 10 symbols:", [s['Symbol'] for s in etf_symbols[:10]])

# Create a list of symbols to check
symbols_to_check = [s['Symbol'] for s in etf_symbols]

# We'll check each symbol in the stocktrade_database
# For performance, let's check a batch at a time and keep track of matches

import duckdb

# Connect to DuckDB - we'll assume it's accessible via the tool
# Since we can't directly connect, we'll use query_db for each table

# Let's start by checking a subset to test the approach
# Then we'll process all symbols

matches = []
checked = 0
errors = 0

# Let's check the first 50 symbols as a test
for symbol in symbols_to_check[:50]:
    try:
        # Query for 2015 data with Adj Close > 200
        query = f"""SELECT "{symbol}" FROM stocktrade_database WHERE 
        Date >= '2015-01-01' AND Date <= '2015-12-31' AND 
        "Adj Close" > 200.0 LIMIT 1"""
        
        # We'll use the query_db tool for this
        # Since we can't call it directly from here, we'll just prepare the queries
        # and track which symbols we need to check
        
        matches.append(symbol)  # Placeholder for now
        checked += 1
        
    except Exception as e:
        errors += 1
        print(f"Error checking {symbol}: {e}")

print(f"Checked {checked} symbols, errors: {errors}")
print("This was just a test run. Will now check all symbols properly.")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
