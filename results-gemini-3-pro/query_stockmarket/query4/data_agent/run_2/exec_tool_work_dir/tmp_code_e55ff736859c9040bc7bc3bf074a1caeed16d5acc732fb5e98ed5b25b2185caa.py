code = """import json

# Load stockinfo results
with open(locals()['var_function-call-6223047370472614305'], 'r') as f:
    stock_info = json.load(f)

# Load list_db results
with open(locals()['var_function-call-14531105657415532109'], 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Filter symbols
valid_stocks = []
for item in stock_info:
    sym = item['Symbol']
    if sym in tables_set:
        valid_stocks.append(item)

print(f"DEBUG: Found {len(valid_stocks)} valid symbols.")

# Generate SQL
# To avoid too large query, let's limit or chunk if necessary.
# But 100-200 symbols is fine.
# Let's see the count first.
queries = []
for stock in valid_stocks:
    sym = stock['Symbol']
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

# Pass the query text and the mapping to the next step via print
# Note: full_query might be large.
print("__RESULT__:")
print(json.dumps({"query": full_query, "stocks": valid_stocks}))"""

env_args = {'var_function-call-5334989958488010331': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-6223047370472614305': 'file_storage/function-call-6223047370472614305.json', 'var_function-call-14531105657415532109': 'file_storage/function-call-14531105657415532109.json'}

exec(code, env_args)
