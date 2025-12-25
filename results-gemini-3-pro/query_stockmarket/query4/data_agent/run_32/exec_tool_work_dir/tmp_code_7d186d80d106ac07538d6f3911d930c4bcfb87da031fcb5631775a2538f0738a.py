code = """import json

with open(locals()['var_function-call-16142873375800227589'], 'r') as f:
    valid_stocks = json.load(f)

print(f"Number of valid stocks: {len(valid_stocks)}")

# Let's create the query string to see how long it is
queries = []
for stock in valid_stocks:
    sym = stock['Symbol']
    # Escape double quotes in symbol if any (unlikely for tickers but good practice)
    # Wrap table name in double quotes
    table_name = f'"{sym}"' 
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM {table_name} WHERE Date LIKE '2017%'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
print(f"Query length: {len(full_query)}")

# If length is > 100,000, maybe we should split.
# Let's split into chunks of 500 stocks.
chunks = []
chunk_size = 500
current_chunk = []
for i, q in enumerate(queries):
    current_chunk.append(q)
    if (i + 1) % chunk_size == 0:
        chunks.append(" UNION ALL ".join(current_chunk))
        current_chunk = []
if current_chunk:
    chunks.append(" UNION ALL ".join(current_chunk))

print(f"Number of chunks: {len(chunks)}")
print("__RESULT__:")
print(json.dumps(chunks))"""

env_args = {'var_function-call-13183360315961424541': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-8321990054734025246': 'file_storage/function-call-8321990054734025246.json', 'var_function-call-10055054036662575247': 'file_storage/function-call-10055054036662575247.json', 'var_function-call-16142873375800227589': 'file_storage/function-call-16142873375800227589.json'}

exec(code, env_args)
