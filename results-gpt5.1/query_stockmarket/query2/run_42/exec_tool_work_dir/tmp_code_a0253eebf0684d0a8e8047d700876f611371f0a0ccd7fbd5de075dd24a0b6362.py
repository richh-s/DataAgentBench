code = """import json, pandas as pd
from datetime import datetime

# Load ETF symbols from file
with open(var_call_CreShPbUpMvyAIkwW0kctGDi, 'r') as f:
    etf_rows = json.load(f)

etf_symbols = [row['Symbol'] for row in etf_rows]

# We will build a DuckDB query that unions over all relevant symbol tables that exist in stocktrade_database.
# First, load all available tables from stocktrade_database list_db result
with open(var_call_3RXB6PeAK6rruYXHoJI1z6vB, 'r') as f:
    all_tables = json.load(f)

# Filter ETF symbols to those that actually have a table in stocktrade_database
etf_with_data = sorted(set(etf_symbols).intersection(set(all_tables)))

# For each symbol, create a SELECT checking 2015 dates with Adj Close > 200
selects = []
for sym in etf_with_data:
    # DuckDB: table name is the symbol; quote it to be safe
    selects.append(f"SELECT '{sym}' AS Symbol FROM '{sym}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200 GROUP BY Symbol")

if selects:
    union_query = " UNION ALL ".join(selects)
else:
    union_query = "SELECT NULL AS Symbol WHERE 1=0"

result = {
    "union_query": union_query,
    "symbol_count": len(etf_with_data)
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_CreShPbUpMvyAIkwW0kctGDi': 'file_storage/call_CreShPbUpMvyAIkwW0kctGDi.json', 'var_call_3RXB6PeAK6rruYXHoJI1z6vB': 'file_storage/call_3RXB6PeAK6rruYXHoJI1z6vB.json'}

exec(code, env_args)
