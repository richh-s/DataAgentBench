code = """import json
import re
from collections import defaultdict

# Load the UNIV CALIFORNIA patent data
file_path = locals()['var_functions.query_db:30']

with open(file_path, 'r') as f:
    univ_calif_data = json.load(f)

print('Total UNIV CALIFORNIA patents:', len(univ_calif_data))

# Extract publication numbers for UNIV CALIFORNIA patents
univ_calif_pubs = set()
for rec in univ_calif_data:
    patents_info = rec['Patents_info']
    # Look for pub. number patterns like: US-2022074631-A1
    match = re.search(r'pub\. number\s+([A-Z]{2}-[^,\s]+)', patents_info)
    if match:
        pub_num = match.group(1)
        univ_calif_pubs.add(pub_num)
    else:
        # Alternative patterns
        match2 = re.search(r'publication number\s+([A-Z]{2}-[^,\s]+)', patents_info, re.IGNORECASE)
        if match2:
            pub_num = match2.group(1)
            univ_calif_pubs.add(pub_num)

print('Extracted publication numbers (sample):', list(univ_calif_pubs)[:10])
print('Total extracted:', len(univ_calif_pubs))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
