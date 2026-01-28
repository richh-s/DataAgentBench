code = """import json
import re
import os

# Load the file containing all patents with citations
citations_file = locals()['var_functions.query_db:24']

with open(citations_file, 'r') as f:
    all_patents = json.load(f)

# Load the file containing UNIV CALIFORNIA patents
uc_file = locals()['var_functions.query_db:22']

with open(uc_file, 'r') as f:
    uc_patents_data = json.load(f)

# Step 1: Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for record in uc_patents_data:
    patents_info = record.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        pub_num_match = re.search(r'(?:pub\. number|publication number|has pub\. number|pub\. number is)\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
        if pub_num_match:
            pub_num = pub_num_match.group(1)
            uc_pub_numbers.add(pub_num)

print(f"Step 1 - Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers:")
for pn in sorted(uc_pub_numbers):
    print(f"  - {pn}")

print("\n" + "="*60)

# Step 2: Find patents that cite UC patents and extract assignees
citing_assignees = {}
citation_count = 0

for record in all_patents:
    citations_str = record.get('citation', '[]')
    patents_info = record.get('Patents_info', '')
    
    # Skip if it's a UNIV CALIFORNIA patent
    if 'UNIV CALIFORNIA' in patents_info:
        continue
        
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for citation in citations:
                cited_pub_num = citation.get('publication_number')
                if cited_pub_num and cited_pub_num in uc_pub_numbers:
                    # Extract assignee from this citing patent
                    assignee_match = re.search(r'(?:owned by|assigned to|is owned by|is assigned to|holds the [A-Z]{2} patent)\s+([A-Z][^,\s\)]*(?:\s+[A-Z][^,\s\)]*)*)', patents_info)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                        if assignee and assignee != 'UNIV CALIFORNIA':
                            citation_count += 1
                            if assignee not in citing_assignees:
                                citing_assignees[assignee] = {
                                    'cited_uc_patents': set(),
                                    'count': 0
                                }
                            citing_assignees[assignee]['cited_uc_patents'].add(cited_pub_num)
                            citing_assignees[assignee]['count'] += 1
        except:
            continue

print(f"Step 2 - Found {len(citing_assignees)} unique assignees citing UC patents ({citation_count} total citations):")
for assignee in sorted(citing_assignees.keys()):
    count = citing_assignees[assignee]['count']
    uc_list = list(citing_assignees[assignee]['cited_uc_patents'])
    print(f"  - {assignee}: {count} citations (citing: {', '.join(uc_list[:3])}{'...' if len(uc_list) > 3 else ''})")

result = {
    'uc_patents_count': len(uc_pub_numbers),
    'citing_assignees_count': len(citing_assignees),
    'total_citations': citation_count,
    'uc_pub_numbers': list(uc_pub_numbers),
    'citing_assignees': list(citing_assignees.keys())
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'uc_patents_count': 8, 'citing_patents_count': 0, 'assignee_citations': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
