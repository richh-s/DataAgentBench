code = """import json
import os

path1 = locals().get('var_function-call-17503537162949357124')
path2 = locals().get('var_function-call-14793823752656914527')

# Load NASDAQ Capital Market companies
with open(path1, 'r') as f:
    nasdaq_companies = json.load(f)

# Load available tables
with open(path2, 'r') as f:
    tables = json.load(f)

# Create a set of table names for fast lookup
table_set = set(tables)

# Filter companies
valid_companies = []
for comp in nasdaq_companies:
    sym = comp['Symbol']
    if sym in table_set:
        valid_companies.append(comp)

# Prepare result to determine next step
result = {
    "total_nasdaq_cm": len(nasdaq_companies),
    "valid_companies_count": len(valid_companies),
    "sample_valid": valid_companies[:5],
    "all_valid_symbols": [c['Symbol'] for c in valid_companies]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17503537162949357124': 'file_storage/function-call-17503537162949357124.json', 'var_function-call-14793823752656914527': 'file_storage/function-call-14793823752656914527.json'}

exec(code, env_args)
