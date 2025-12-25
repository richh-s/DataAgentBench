code = """import json

# Access the file paths from the storage variables
path1 = locals()['var_function-call-1914327577488087948']
path2 = locals()['var_function-call-546925876155124567']

with open(path1, 'r') as f:
    target_data = json.load(f)

with open(path2, 'r') as f:
    all_tables = json.load(f)

target_symbols = set([item['Symbol'] for item in target_data])
available_tables = set(all_tables)

valid_symbols = list(target_symbols.intersection(available_tables))

# Generate query
# Limit to 100 symbols per query to avoid length issues? 
# Or just try one big query. 
# There are about 300 NASDAQ Capital Market stocks usually?
# Let's check the length.

queries = []
for sym in valid_symbols:
    # Escape quotes just in case, though symbols are usually alphanumeric
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as HighRangeDays FROM \"{sym}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

full_query = ""
if queries:
    full_query = " UNION ALL ".join(queries) + " ORDER BY HighRangeDays DESC LIMIT 5"

result = {
    "count": len(valid_symbols),
    "query": full_query,
    "valid_symbols": valid_symbols
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1914327577488087948': 'file_storage/function-call-1914327577488087948.json', 'var_function-call-546925876155124567': 'file_storage/function-call-546925876155124567.json'}

exec(code, env_args)
