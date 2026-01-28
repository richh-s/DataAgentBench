code = """import json
import os

# Read the full result from the file
with open('var_functions.query_db:0', 'r') as f:
    companies = json.load(f)

print(f"Found {len(companies)} companies on NASDAQ Capital Market")
print("First few companies:")
for i, company in enumerate(companies[:5]):
    print(f"  {company['Symbol']}: {company['Company Description']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
