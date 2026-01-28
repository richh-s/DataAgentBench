code = """import json
import re

# Access the stored result
uc_patents_data = locals()['var_functions.query_db:8']

# If it's a file path, read it
if isinstance(uc_patents_data, str) and '.json' in uc_patents_data:
    with open(uc_patents_data, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = uc_patents_data

print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")

# Extract publication numbers from Patents_info field
pub_numbers = []
for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    match = re.search(r'(?:pub\.|publication|pub\s+no|publication\s+no)\s+(?:[A-Z]+-)?([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        pub_numbers.append(pub_num)

print(f"Extracted {len(pub_numbers)} publication numbers")
print("First few:", pub_numbers[:5])

# Create a set for faster lookup
uc_pub_numbers = set(pub_numbers)
print(f"Total unique UNIV CALIFORNIA publication numbers: {len(uc_pub_numbers)}")

# Export to JSON for next steps
result = list(uc_pub_numbers)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
