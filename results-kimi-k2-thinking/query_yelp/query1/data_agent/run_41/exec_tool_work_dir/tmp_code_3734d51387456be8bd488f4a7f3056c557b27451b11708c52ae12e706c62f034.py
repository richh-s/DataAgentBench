code = """import json

# Read the result file from the previous query
result_file = locals()['var_functions.query_db:2']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        all_businesses = json.load(f)
else:
    all_businesses = locals()['var_functions.query_db:2']

# Debug: print the type and length
print(f"Type: {type(all_businesses)}")
print(f"Length: {len(all_businesses) if hasattr(all_businesses, '__len__') else 'N/A'}")

# Extract Indianapolis businesses
indianapolis_business_ids = []
for business in all_businesses:
    description = business.get('description', '')
    if 'Indianapolis, IN' in description:
        business_id = business.get('business_id')
        if business_id:
            indianapolis_business_ids.append(business_id)

print(f"Found {len(indianapolis_business_ids)} Indianapolis businesses")
print(f"First few: {indianapolis_business_ids[:5] if indianapolis_business_ids else 'None'}")

# Prepare result
result = json.dumps(indianapolis_business_ids)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
