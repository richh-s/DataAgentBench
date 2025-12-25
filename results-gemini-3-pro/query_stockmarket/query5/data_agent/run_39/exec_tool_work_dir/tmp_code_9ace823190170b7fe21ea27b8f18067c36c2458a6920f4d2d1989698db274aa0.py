code = """import json
import pandas as pd

# Load stockinfo result
with open('var_function-call-4097608082559162712.json', 'r') as f:
    stockinfo_data = json.load(f)

stockinfo_df = pd.DataFrame(stockinfo_data)
# Filter just in case, though the query already did
target_symbols = stockinfo_df['Symbol'].tolist()
print(f"Found {len(target_symbols)} symbols in NASDAQ Capital Market.")

# Load stocktrade tables result
with open('var_function-call-14328794898966256946.json', 'r') as f:
    stocktrade_tables = json.load(f)

print(f"Found {len(stocktrade_tables)} tables in stocktrade_database.")

# Find intersection
# Note: table names in stocktrade might be case sensitive or not. Usually they match the symbol.
# The previous output shows uppercase symbols.
common_symbols = sorted(list(set(target_symbols) & set(stocktrade_tables)))
print(f"Found {len(common_symbols)} common symbols.")

# Generate the SQL query
# We want top 5.
# Query structure:
# SELECT Symbol, Count(*) as HighRangeDays FROM (
#   SELECT 'SYM' as Symbol, High, Low, Date FROM SYM WHERE STRFTIME('%Y', Date) = '2019'
#   UNION ALL ...
# ) WHERE (High - Low) > 0.2 * Low GROUP BY Symbol ORDER BY HighRangeDays DESC LIMIT 5

# However, constructing a massive UNION ALL might hit parser limits.
# Let's see how many symbols we have.
if len(common_symbols) > 0:
    print(f"Example symbols: {common_symbols[:5]}")
    
print("__RESULT__:")
print(json.dumps(common_symbols))"""

env_args = {'var_function-call-4097608082559162712': 'file_storage/function-call-4097608082559162712.json', 'var_function-call-14328794898966256946': 'file_storage/function-call-14328794898966256946.json'}

exec(code, env_args)
