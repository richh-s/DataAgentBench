code = """import json
import os

# Check what we have in the variable
result_var = locals()['var_functions.query_db:0']
print(f"Type: {type(result_var)}")
print(f"Value: {repr(result_var)[:200]}")

# If it's a string path to a JSON file, read it
if isinstance(result_var, str) and result_var.endswith('.json'):
    with open(result_var, 'r') as f:
        companies = json.load(f)
    print(f"Loaded {len(companies)} companies from file")
else:
    # If it's already the data
    companies = result_var
    print(f"Already have {len(companies)} companies in memory")

# Show first few companies
print("\nFirst few companies:")
for i, company in enumerate(companies[:5]):
    print(f"  {company.get('Symbol', 'N/A')}: {company.get('Company Description', 'N/A')[:60]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
