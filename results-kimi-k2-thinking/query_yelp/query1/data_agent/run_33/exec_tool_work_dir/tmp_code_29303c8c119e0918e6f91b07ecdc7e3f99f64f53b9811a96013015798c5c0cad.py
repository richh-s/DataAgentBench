code = """import json

# Read the full result from file
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    businesses = json.load(f)

# Filter for Indianapolis, IN businesses
indianapolis_businesses = []
for business in businesses:
    description = business.get('description', '').lower()
    if 'indianapolis' in description and 'in' in description:
        # Check if it's the state abbreviation
        if ', in' in description or 'in,' in description:
            indianapolis_businesses.append(business)

print('__RESULT__:')
print(json.dumps(indianapolis_businesses))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
