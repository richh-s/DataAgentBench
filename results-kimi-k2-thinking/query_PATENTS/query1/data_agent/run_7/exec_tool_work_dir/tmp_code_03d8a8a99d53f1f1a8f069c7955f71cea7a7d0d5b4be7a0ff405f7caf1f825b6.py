code = """import json

# The storage key contains a file path
file_path = var_functions.query_db:2
print(f"File path: {file_path}")

# Read the query result file
with open(file_path, 'r') as f:
    records = json.load(f)

print(f"Loaded {len(records)} records")
print("Sample record publication date:", records[0]['publication_date'])

# Check CPC data
sample_cpc = records[0]['cpc']
print(f"Sample CPC data type: {type(sample_cpc)}")
print(f"Sample CPC (first 300 chars): {sample_cpc[:300]}")

# Try to parse it (it looks like a JSON string)
import ast
try:
    cpc_list = ast.literal_eval(sample_cpc)
    print(f"\nParsed CPC list length: {len(cpc_list)}")
    if cpc_list:
        print(f"First CPC entry: {cpc_list[0]}")
except Exception as e:
    print(f"Error evaluating CPC string: {e}")
    
# Also try json.loads
try:
    cpc_list = json.loads(sample_cpc)
    print(f"\nJSON parsed CPC list length: {len(cpc_list)}")
    if cpc_list:
        print(f"First CPC entry: {cpc_list[0]}")
except Exception as e:
    print(f"JSON parsing error: {e}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
