code = """import json

# Get file paths from local variables
stock_info_path = locals()['var_function-call-392181113941230713']
table_list_path = locals()['var_function-call-4237662191302365216']

# Load data
with open(stock_info_path, 'r') as f:
    stock_info_list = json.load(f)

with open(table_list_path, 'r') as f:
    table_list = json.load(f)

tables_set = set(table_list)
valid_stocks = [s for s in stock_info_list if s['Symbol'] in tables_set]

batches = []
batch_size = 1000 # Try to fit all in one
current_batch = []

for stock in valid_stocks:
    sym = stock['Symbol']
    # Ensure quoting
    query_part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"" + sym + "\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'"
    current_batch.append(query_part)
    
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    batches.append(" UNION ALL ".join(current_batch))

print("__RESULT__:")
print(json.dumps(batches))"""

env_args = {'var_function-call-392181113941230713': 'file_storage/function-call-392181113941230713.json', 'var_function-call-4237662191302365216': 'file_storage/function-call-4237662191302365216.json', 'var_function-call-8581997054017550761': 'file_storage/function-call-8581997054017550761.json', 'var_function-call-8534971037616957309': 5}

exec(code, env_args)
