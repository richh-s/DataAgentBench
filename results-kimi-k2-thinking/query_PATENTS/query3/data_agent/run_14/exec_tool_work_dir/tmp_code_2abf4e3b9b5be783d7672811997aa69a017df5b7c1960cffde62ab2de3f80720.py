code = """import json
import os

# Load all UNIV CALIFORNIA patents
with open(locals()['var_functions.query_db:24'], 'r') as f:
    univ_california_patents = json.load(f)

print('UNIV CALIFORNIA patents found:', len(univ_california_patents))

# Extract publication numbers from these patents
univ_calif_pub_numbers = []
for patent in univ_california_patents:
    patents_info = patent.get('Patents_info', '')
    # Extract publication number from Patents_info
    if 'pub. number' in patents_info:
        # Look for pattern like "pub. number US-2022074631-A1"
        import re
        match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
        if match:
            pub_num = match.group(1)
            univ_calif_pub_numbers.append(pub_num)
            print(f"Found patent: {pub_num}")

print('\nTotal UNIV CALIFORNIA publication numbers extracted:', len(univ_calif_pub_numbers))
print('Sample:', univ_calif_pub_numbers[:5] if univ_calif_pub_numbers else 'None')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:22': [{'total_rows': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
