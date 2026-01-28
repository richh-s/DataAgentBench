code = """import json
import pandas as pd
import re

# Load the data from the file
with open('var_functions.query_db:2.json', 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Extract UNIV CALIFORNIA patents and their publication numbers
uc_patents = []
for record in data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        # Extract publication number from Patents_info
        # Looking for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
        pub_num_match = re.search(r'(?:pub\. number|publication number|has pub\. number|pub\. number is)\s+([A-Z]{2}-[^\s,]+)', patents_info)
        if pub_num_match:
            pub_num = pub_num_match.group(1)
            uc_patents.append({
                'publication_number': pub_num,
                'patents_info': patents_info,
                'citation': record.get('citation', '[]')
            })

print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")

# Show first few to verify
for i, p in enumerate(uc_patents[:3]):
    print(f"{i+1}. Publication: {p['publication_number']}, Info: {p['patents_info'][:100]}...")

# Create a set of UC publication numbers for easy lookup
uc_pub_numbers = {p['publication_number'] for p in uc_patents}
print(f"UC publication numbers: {list(uc_pub_numbers)[:5]}...")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
