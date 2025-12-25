code = """import json

# Load NASDAQ Capital Market symbols
with open('var_function-call-17503537162949357124.json', 'r') as f:
    nasdaq_companies = json.load(f)

# Load available tables
with open('var_function-call-14793823752656914527.json', 'r') as f:
    tables = json.load(f)

# Create a set of table names for fast lookup
table_set = set(tables)

# Filter companies
valid_companies = []
for comp in nasdaq_companies:
    sym = comp['Symbol']
    if sym in table_set:
        valid_companies.append(comp)

print(f"Total NASDAQ Capital Market companies: {len(nasdaq_companies)}")
print(f"Companies with data: {len(valid_companies)}")
print("__RESULT__:")
print(json.dumps(valid_companies[:5])) # Print a few to check structure"""

env_args = {'var_function-call-17503537162949357124': 'file_storage/function-call-17503537162949357124.json', 'var_function-call-14793823752656914527': 'file_storage/function-call-14793823752656914527.json'}

exec(code, env_args)
