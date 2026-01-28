code = """import json
import re

# Query a few sample records to understand the structure
sample_query = """
SELECT Patents_info, citation 
FROM publicationinfo 
LIMIT 3
"""

# Load sample data to understand structure
sample_file = locals()['var_functions.query_db:18']

with open(sample_file, 'r') as f:
    sample_data = json.load(f)

print("Sample records:")
for i, record in enumerate(sample_data[:2]):
    print(f"\nRecord {i+1}:")
    print(f"Patents_info: {record['Patents_info'][:150]}...")
    print(f"Citation preview: {record['citation'][:200] if record['citation'] else 'No citations'}...")

print("\n" + "="*50)

# Now let's identify all UNIV CALIFORNIA patents
uc_file = locals()['var_functions.query_db:14']

with open(uc_file, 'r') as f:
    uc_data = json.load(f)

uc_pub_numbers = set()
uc_patents = []

for record in uc_data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        pub_num_match = re.search(r'(?:pub\. number|publication number|has pub\. number|pub\. number is)\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
        if pub_num_match:
            pub_num = pub_num_match.group(1)
            uc_pub_numbers.add(pub_num)
            uc_patents.append({
                'publication_number': pub_num,
                'info': patents_info
            })

print(f"\nFound {len(uc_patents)} UNIV CALIFORNIA patents")
for p in uc_patents:
    print(f"  - {p['publication_number']}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'uc_patents_count': 8, 'citing_patents_count': 0, 'assignee_citations': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
