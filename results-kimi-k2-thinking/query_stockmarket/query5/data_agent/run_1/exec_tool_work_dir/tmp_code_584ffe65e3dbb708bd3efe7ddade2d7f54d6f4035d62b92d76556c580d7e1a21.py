code = """import json

# Load the result from the previous query
rl = locals()['var_functions.query_db:0']

# If rl is a string (file path), read the JSON file
if isinstance(rl, str):
    with open(rl, 'r') as f:
        rl = json.load(f)

# Count total number of companies
num_companies = len(rl)
print(f"Total number of NASDAQ Capital Market companies: {num_companies}")

# Show first 10 companies for debugging
print("\nFirst 10 companies:")
for i, company in enumerate(rl[:10]):
    print(f"{i+1}. Symbol: {company['Symbol']}, Company: {company['Company Description'][:60]}...")

# Check if we need to process further
print(f"\nReady to analyze {num_companies} companies")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
