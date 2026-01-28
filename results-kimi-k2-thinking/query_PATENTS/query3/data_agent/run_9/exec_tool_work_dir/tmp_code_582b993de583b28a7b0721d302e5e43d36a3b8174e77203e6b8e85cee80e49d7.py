code = """import json
import re

# Load the UNIV CALIFORNIA patents data from the correct variable
uc_patents = var_functions.query_db:26

print(f"Loaded {len(uc_patents)} UNIV CALIFORNIA patents")

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for pub. number patterns like US-2022074631-A1
    pub_matches = re.findall(r'pub\. number\s+([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]*)', patents_info)
    if pub_matches:
        uc_pub_numbers.update(pub_matches)
    else:
        # Alternative patterns
        alt_matches = re.findall(r'([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]*)', patents_info)
        if alt_matches:
            uc_pub_numbers.update(alt_matches)

print(f"Found {len(uc_pub_numbers)} UC publication numbers")
print(f"Sample: {list(uc_pub_numbers)[:10]}")

# Save UC pub numbers for later use
with open('/tmp/uc_pub_numbers.json', 'w') as f:
    json.dump(list(uc_pub_numbers), f)

print("Done extracting UC publication numbers")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'total_patents': '169'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
