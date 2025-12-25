code = """import json

# Load ETF list
with open(var_function_call_15483899617551082624, 'r') as f:
    etf_list = json.load(f)

# Extract symbols
etf_symbols = [item['Symbol'] for item in etf_list]

# Load table list
with open(var_function_call_17197364182680462886, 'r') as f:
    table_list = json.load(f)

# Find intersection (valid tables)
valid_etfs = sorted(list(set(etf_symbols).intersection(set(table_list))))

print(f"Total valid ETFs to check: {len(valid_etfs)}")

# Generate queries
# We want to check if any record in 2015 has Adj Close > 200
# Query: SELECT 'SYM' FROM SYM WHERE Date LIKE '2015%' AND "Adj Close" > 200 LIMIT 1
# We can combine these with UNION ALL

queries = []
batch_size = 50
current_batch = []

for i, sym in enumerate(valid_etfs):
    current_batch.append(sym)
    if len(current_batch) == batch_size or i == len(valid_etfs) - 1:
        # Construct query for the batch
        # SELECT 'SYM' as Symbol WHERE EXISTS (SELECT 1 FROM SYM WHERE Date LIKE '2015%' AND "Adj Close" > 200)
        # But DuckDB syntax might be simpler:
        # SELECT 'SYM' as Symbol FROM SYM WHERE Date LIKE '2015%' AND "Adj Close" > 200 LIMIT 1
        # Combined:
        # SELECT * FROM (
        #   SELECT 'SYM1' as Symbol FROM SYM1 WHERE Date LIKE '2015%' AND "Adj Close" > 200 LIMIT 1
        # ) UNION ALL SELECT * FROM (
        #   SELECT 'SYM2' as Symbol FROM SYM2 WHERE Date LIKE '2015%' AND "Adj Close" > 200 LIMIT 1
        # ) ...
        
        # More efficient:
        # SELECT 'SYM1' as Symbol WHERE (SELECT MAX("Adj Close") FROM SYM1 WHERE Date LIKE '2015%') > 200
        # Wait, if Date is string, LIKE '2015%' works.
        
        sub_queries = []
        for s in current_batch:
             sub_queries.append(f"SELECT '{s}' as Symbol FROM \"{s}\" WHERE Date LIKE '2015%' AND \"Adj Close\" > 200 LIMIT 1")
        
        full_query = " UNION ALL ".join(sub_queries)
        queries.append(full_query)
        current_batch = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json'}

exec(code, env_args)
