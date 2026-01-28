code = """import json
import re
import os

# Load patent data
uc_file = locals()['var_functions.query_db:22']
citations_file = locals()['var_functions.query_db:24']

with open(uc_file, 'r') as f:
    uc_data = json.load(f)

with open(citations_file, 'r') as f:
    citation_data = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
for record in uc_data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        match = re.search(r'pub\. number\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
        if match:
            uc_pub_numbers.add(match.group(1))

print("UNIV CALIFORNIA patents found:", len(uc_pub_numbers))
print("UC publication numbers:", list(uc_pub_numbers))

# Search for citations systematically
citing_assignees = {}
total_matches = 0

for record in citation_data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    citations_str = record.get('citation', '[]')
    if citations_str and citations_str != '[]':
        for uc_pub in uc_pub_numbers:
            if uc_pub in citations_str:
                total_matches += 1
                assignee_match = re.search(r'([A-Z][^,\s\)]*(?:\s+[A-Z][^,\s\)]*)*)\s+(?:holds|owns|is assigned|assigned to)', patents_info)
                if assignee_match:
                    assignee = assignee_match.group(1).strip()
                    if assignee not in citing_assignees:
                        citing_assignees[assignee] = []
                    citing_assignees[assignee].append(uc_pub)

print(f"\nFound {len(citing_assignees)} assignees citing UC patents:")
for assignee in sorted(citing_assignees.keys()):
    print(f"  {assignee}: {citing_assignees[assignee]}")

result = {
    'uc_patents': list(uc_pub_numbers),
    'citing_assignees': citing_assignees,
    'total_citations': total_matches
}

print("\n__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'uc_patents_count': 8, 'citing_patents_count': 0, 'assignee_citations': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': []}

exec(code, env_args)
