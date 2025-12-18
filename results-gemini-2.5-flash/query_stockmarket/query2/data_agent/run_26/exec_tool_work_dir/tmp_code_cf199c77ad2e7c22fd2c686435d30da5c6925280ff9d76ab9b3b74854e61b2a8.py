code = """import json

# The result from the previous query_db call is stored in a file.
# We need to open and load the JSON content from this file.
with open(locals()['var_function-call-12451871195317439682'], 'r') as f:
    raw_data = json.load(f)

# The structure of the loaded JSON is {"query_db_response": {"results": [...]}}
# So, we need to access the 'results' key within 'query_db_response'.
etf_symbols_list_of_dicts = raw_data['query_db_response']['results']

# Extract just the 'Symbol' strings into a list
etf_symbols = [d['Symbol'] for d in etf_symbols_list_of_dicts]

# Construct the UNION ALL query
union_queries = []
for symbol in etf_symbols:
    # Each sub-query should select the symbol and the max adjusted close price for 2015
    # Double quotes are used for column names with spaces or special characters, and for table names (which are symbols here)
    # Single quotes are for string literals (the symbol itself).
    union_queries.append(f"SELECT '{symbol}' AS Symbol, MAX(\"Adj Close\") AS MaxAdjClose FROM \"{symbol}\" WHERE Date LIKE '2015-%'")

# Join all the sub-queries with UNION ALL
full_query = " UNION ALL ".join(union_queries)

print("__RESULT__:")
print(json.dumps({"db_name": "stocktrade_database", "query": full_query}))"""

env_args = {'var_function-call-12451871195317439682': 'file_storage/function-call-12451871195317439682.json'}

exec(code, env_args)
