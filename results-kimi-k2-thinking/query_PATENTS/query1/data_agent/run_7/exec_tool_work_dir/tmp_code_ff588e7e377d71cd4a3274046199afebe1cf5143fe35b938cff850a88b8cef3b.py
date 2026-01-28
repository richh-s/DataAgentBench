code = """import json

# Read the query result file
with open(var_functions.query_db:2, 'r') as f:
    records = json.load(f)

print(f"Loaded {len(records)} records")
print("Sample record:")
print(json.dumps(records[0], indent=2)[:500] + "...")

# Let's check the structure
sample_cpc = records[0]['cpc']
print(f"\nSample CPC data type: {type(sample_cpc)}")
print(f"Sample CPC content: {sample_cpc[:200]}...")

# Parse the first record to understand structure
try:
    cpc_list = json.loads(records[0]['cpc'])
    print(f"\nParsed CPC list length: {len(cpc_list)}")
    print(f"First CPC entry: {cpc_list[0]}")
except Exception as e:
    print(f"Error parsing CPC JSON: {e}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
