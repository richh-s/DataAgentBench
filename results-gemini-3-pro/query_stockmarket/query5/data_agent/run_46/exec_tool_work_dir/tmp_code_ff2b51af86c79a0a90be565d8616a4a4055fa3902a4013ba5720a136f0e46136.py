code = """import json
import pandas as pd

# Load the target symbols
with open('var_function-call-1914327577488087948.json', 'r') as f:
    target_data = json.load(f)
target_symbols = set([item['Symbol'] for item in target_data])

# Load the available tables
with open('var_function-call-546925876155124567.json', 'r') as f:
    all_tables = json.load(f)
available_tables = set(all_tables)

# Intersect
valid_symbols = list(target_symbols.intersection(available_tables))

print(f"Total target symbols: {len(target_symbols)}")
print(f"Total available tables: {len(available_tables)}")
print(f"Valid matching symbols: {len(valid_symbols)}")

# Generate SQL query
# We want to find top 5.
# SELECT 'SYMBOL' as symbol, SUM(CASE WHEN (High - Low) > 0.2 * Low THEN 1 ELSE 0 END) as cnt FROM SYMBOL WHERE Date LIKE '2019%'
# Using UNION ALL
# We should only query for 2019 to optimize.

queries = []
for sym in valid_symbols:
    # Use double quotes for table names just in case of reserved words or special chars
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as HighRangeDays FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY HighRangeDays DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "query": full_query}))"""

env_args = {'var_function-call-1914327577488087948': 'file_storage/function-call-1914327577488087948.json', 'var_function-call-546925876155124567': 'file_storage/function-call-546925876155124567.json'}

exec(code, env_args)
