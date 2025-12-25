code = """import json

# Load previous results
stock_info_list = json.load(open('var_function-call-392181113941230713.json'))
table_list = json.load(open('var_function-call-4237662191302365216.json'))

# Create a set of available tables
tables_set = set(table_list)

# Filter stocks that have tables
valid_stocks = []
for s in stock_info_list:
    sym = s['Symbol']
    if sym in tables_set:
        valid_stocks.append(s)

print(f"Total valid stocks: {len(valid_stocks)}")

# Create batches of queries if needed
# A safe batch size for DuckDB via this interface might be 50-100 tables per query to avoid huge SQL strings.
# Let's target 50 tables per batch.

batches = []
batch_size = 50
current_batch = []

for stock in valid_stocks:
    sym = stock['Symbol']
    # Select needed columns and calculate up/down immediately to save data transfer?
    # Or just select raw data. Calculating in SQL is cleaner.
    # SQL: SELECT 'SYM' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM SYM WHERE Date LIKE '2017%'
    
    # Check if we can do this. The Date format is usually YYYY-MM-DD.
    
    query_part = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'"
    current_batch.append(query_part)
    
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    batches.append(" UNION ALL ".join(current_batch))

print(f"Number of batches: {len(batches)}")

# Pass the batches to the next step via print or just print them to a variable I can use?
# I can't pass variables to the next tool call directly except via 'result'.
# So I will print the batches as a JSON list.

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-392181113941230713': 'file_storage/function-call-392181113941230713.json', 'var_function-call-4237662191302365216': 'file_storage/function-call-4237662191302365216.json'}

exec(code, env_args)
