code = """import json

# Get the file path from the stored result
result_file = locals()['var_functions.query_db:2']
print(f"Result file path: {result_file}")

# Read the JSON file
with open(result_file, 'r') as f:
    reviews_data = json.load(f)

print(f"Total reviews in the file: {len(reviews_data)}")

# Print first few records to verify structure
for i in range(min(3, len(reviews_data))):
    print(f"Review {i+1}: {reviews_data[i]}")

# Calculate business_id from business_ref by removing prefix and adding business_ prefix
business_ref_to_id = {}
for review in reviews_data:
    if 'business_ref' in review:
        ref = review['business_ref']
        # Convert businessref_X to businessid_X
        if ref.startswith('businessref_'):
            business_id = 'businessid_' + ref.split('_', 1)[1]
            business_ref_to_id[ref] = business_id

print(f"\nSample business ID mapping: {list(business_ref_to_id.items())[:3]}")"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
