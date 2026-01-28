code = """import json
import re

# Get all patents data
with open('/tmp/tmp_result_l6k9k9.json', 'r') as f:
    all_patents = json.load(f)

print(f"Total patents loaded: {len(all_patents)}")

# Extract UNIV CALIFORNIA patents
uc_patents = []
for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        uc_patents.append(patent)

print(f"UNIV CALIFORNIA patents found: {len(uc_patents)}")

# Extract publication numbers for UNIV CALIFORNIA patents
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for publication number patterns like US-2022074631-A1
    pub_matches = re.findall(r'pub\. number\s+([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]*)', patents_info)
    if pub_matches:
        for pub in pub_matches:
            uc_pub_numbers.add(pub)
    else:
        # Alternative pattern
        alt_matches = re.findall(r'([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]*)', patents_info)
        if alt_matches:
            uc_pub_numbers.update(alt_matches)

print(f"UNIV CALIFORNIA publication numbers: {list(uc_pub_numbers)[:10]}...")
print(f"Total unique UC pub numbers: {len(uc_pub_numbers)}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'total_patents': '169'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
