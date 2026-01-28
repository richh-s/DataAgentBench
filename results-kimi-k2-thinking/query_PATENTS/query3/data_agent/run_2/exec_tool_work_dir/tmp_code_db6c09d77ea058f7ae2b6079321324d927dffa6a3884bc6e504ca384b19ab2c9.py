code = """import json
import re
import os

# Load the data file
data_file = locals()['var_functions.query_db:32']

with open(data_file, 'r') as f:
    patents_with_citations = json.load(f)

print(f"Loaded {len(patents_with_citations)} patents that have citations")

# Extract UC publication numbers first
uc_file = locals()['var_functions.query_db:22']
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

uc_pub_numbers = set()
for record in uc_data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        match = re.search(r'pub\. number\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
        if match:
            uc_pub_numbers.add(match.group(1))

print(f"UC publication numbers: {list(uc_pub_numbers)}")
print()

# Now analyze which patents cite UC patents
citing_assignees = {}
uc_citation_count = 0

for record in patents_with_citations:
    patents_info = record.get('Patents_info', '')
    
    # Skip if it's UC patent
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    citations_str = record.get('citation', '[]')
    
    # Check if it cites any UC patent
    for uc_pub in uc_pub_numbers:
        if uc_pub in citations_str:
            uc_citation_count += 1
            
            # Extract assignee
            assignee_match = re.search(r'([A-Z][^,\s\)]+(?:\s+[A-Z][^,\s\)]+)*)\s+(?:holds|owns|is assigned|assigned to|belonging to|from US, (\w+(?:\s+\w+)*)[,\s])', patents_info)
            if assignee_match:
                if assignee_match.group(1):
                    assignee = assignee_match.group(1).strip()
                else:
                    assignee = assignee_match.group(2).strip()
                
                if assignee and assignee != 'UNIV CALIFORNIA':
                    if assignee not in citing_assignees:
                        citing_assignees[assignee] = set()
                    citing_assignees[assignee].add(uc_pub)

print(f"Found {len(citing_assignees)} assignees citing UC patents ({uc_citation_count} citations total):")
for assignee in sorted(citing_assignees.keys()):
    uc_list = list(citing_assignees[assignee])
    print(f"  {assignee}: {uc_list}")

print("\n" + "="*60)
print("RESULT SUMMARY:")
print(f"UC Patents: {len(uc_pub_numbers)}")
print(f"Citing Assignees: {len(citing_assignees)}")
print(f"Total Citations: {uc_citation_count}")
print("="*60)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'uc_patents_count': 8, 'citing_patents_count': 0, 'assignee_citations': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
