code = """import json
import re

# Access the data from previous queries
# We need to load the actual files since they were stored as file paths

# First, let's get all patents assigned to UNIV CALIFORNIA
# We already have a file with UC patents from var_functions.query_db:14
uc_file_path = var_functions.query_db:14

with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

print(f'Number of patents assigned to UNIV CALIFORNIA: {len(uc_patents)}')
print('Sample UC patent info:')
print(uc_patents[0]['Patents_info'])

# Extract publication numbers for UC patents
uc_pub_numbers = []
for patent in uc_patents:
    # Try to extract publication number from Patents_info
    info = patent['Patents_info']
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', info)
    if match:
        uc_pub_numbers.append(match.group(1))

print(f'\nExtracted {len(uc_pub_numbers)} UC publication numbers')
print('Sample:', uc_pub_numbers[:5])

# Save results for next step
result = {
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers': uc_pub_numbers
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
