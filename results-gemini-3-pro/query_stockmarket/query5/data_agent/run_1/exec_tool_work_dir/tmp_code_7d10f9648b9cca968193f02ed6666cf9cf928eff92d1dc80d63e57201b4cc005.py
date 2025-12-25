code = """import json
import pandas as pd

# Load stock info
with open('var_function-call-9978005257229487382.json', 'r') as f:
    stock_info = json.load(f)

# Load table list
with open('var_function-call-9978005257229485951.json', 'r') as f:
    tables = json.load(f)

# Convert tables to set for fast lookup
table_set = set(tables)

# Filter Capital Market symbols that have tables
# The stock_info contains 'Symbol' and 'Company Description'
valid_symbols = []
for item in stock_info:
    sym = item['Symbol']
    if sym in table_set:
        valid_symbols.append(sym)

print(f"DEBUG: Found {len(valid_symbols)} valid symbols.")

# Construct SQL query
# SELECT 'SYM' AS Symbol, COUNT(*) AS Days FROM "SYM" WHERE Date LIKE '2019%' AND (High - Low) > 0.2 * Low
# UNION ALL ...
# ORDER BY Days DESC LIMIT 5

sqls = []
for sym in valid_symbols:
    # Ensure symbol is safely quoted if necessary, though typical tickers are fine.
    # Using double quotes for table name as per DuckDB/SQL standard for identifiers.
    sqls.append(f"SELECT '{sym}' AS Symbol, COUNT(*) AS Days FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")

full_query = " UNION ALL ".join(sqls) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-9978005257229487382': 'file_storage/function-call-9978005257229487382.json', 'var_function-call-9978005257229485951': 'file_storage/function-call-9978005257229485951.json'}

exec(code, env_args)
