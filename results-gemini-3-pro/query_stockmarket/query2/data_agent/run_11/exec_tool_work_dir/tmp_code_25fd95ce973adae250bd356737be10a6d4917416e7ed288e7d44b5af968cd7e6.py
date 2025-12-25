code = """import json

# Access variables using locals() because of hyphens in names
path_etfs = locals()['var_function-call-15483899617551082624']
path_tables = locals()['var_function-call-17197364182680462886']

# Load ETF list
with open(path_etfs, 'r') as f:
    etf_list = json.load(f)

# Extract symbols
etf_symbols = [item['Symbol'] for item in etf_list]

# Load table list
with open(path_tables, 'r') as f:
    table_list = json.load(f)

# Find intersection (valid tables)
valid_etfs = sorted(list(set(etf_symbols).intersection(set(table_list))))

# Generate queries
# We split into batches to avoid too long queries
queries = []
batch_size = 50
current_batch = []

for i, sym in enumerate(valid_etfs):
    current_batch.append(sym)
    if len(current_batch) == batch_size or i == len(valid_etfs) - 1:
        sub_queries = []
        for s in current_batch:
             # Use double quotes for table names to handle case sensitivity or special chars if any
             sub_queries.append(f"SELECT '{s}' as Symbol FROM \"{s}\" WHERE Date LIKE '2015%' AND \"Adj Close\" > 200 LIMIT 1")
        
        full_query = " UNION ALL ".join(sub_queries)
        queries.append(full_query)
        current_batch = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json'}

exec(code, env_args)
