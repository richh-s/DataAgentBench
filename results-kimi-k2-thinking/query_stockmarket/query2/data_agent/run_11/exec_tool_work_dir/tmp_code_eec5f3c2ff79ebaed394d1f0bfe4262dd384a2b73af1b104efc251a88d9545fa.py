code = """import json

# Check the full result from the previous query
result_path = var_functions.query_db:0
print(f"Result path: {result_path}")
# Read the full result from the JSON file
with open(result_path, 'r') as f:
    full_result = json.load(f)

# Show a preview
print(f"Number of NYSE Arca ETFs: {len(full_result)}")
print("First 10 ETFs:")
for etf in full_result[:10]:
    print(etf)

# Now let's check which of these ETFs had an adjusted closing price above $200 in 2015
# We'll need to look in the stocktrade_database, where each table is named after the ticker symbol
import sqlite3

# Get list of all ETF symbols from the result
nyse_arca_etfs = [etf['Symbol'] for etf in full_result]
print(f"\nTotal NYSE Arca ETFs found: {len(nyse_arca_etfs)}")
print(f"First 5 ETF symbols: {nyse_arca_etfs[:5]}")

# Print result structure
----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({"count": len(nyse_arca_etfs), "preview": nyse_arca_etfs[:10]}))
----END PRINT FORMAT----"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
