code = """import os
import json
import re
from collections import defaultdict

# Read UC patents data
uc_patents_file = 'var_functions.query_db:8'
if os.path.exists(uc_patents_file):
    with open(uc_patents_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = []

# Read all patents data  
all_patents_file = 'var_functions.query_db:36'
if os.path.exists(all_patents_file):
    with open(all_patents_file, 'r') as f:
        all_patents = json.load(f)
else:
    # Try the other file
    all_patents_file = 'var_functions.query_db:34'
    if os.path.exists(all_patents_file):
        with open(all_patents_file, 'r') as f:
            all_patents = json.load(f)
    else:
        all_patents = []

print(f"Loaded {len(uc_patents)} UNIV CALIFORNIA patents")
print(f"Loaded {len(all_patents)} other patents for citation analysis")

# Extract UC publication numbers
uc_pub_numbers = set()
uc_patent_lookup = {}  # Map pub number to patent data

for patent in uc_patents:
    info = patent.get('Patents_info', '')
    # More flexible pattern matching for pub numbers
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.add(pub_num)
        uc_patent_lookup[pub_num] = patent

print(f"Extracted {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")

# Find patents that cite UNIV CALIFORNIA patents
citing_patents = []
for patent in all_patents:
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            for cite in citations:
                cited_pub = cite.get('publication_number')
                if cited_pub and cited_pub in uc_pub_numbers:
                    # Extract assignee from the citing patent
                    info = patent.get('Patents_info', '')
                    assignee_match = re.search(r'^(.+?)\s+(holds|assigned to|owned by|is the applicant)', info)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                        # Exclude UNIV CALIFORNIA self-citations
                        if 'UNIV CALIFORNIA' not in assignee.upper():
                            citing_patents.append({
                                'citing_assignee': assignee,
                                'cited_uc_patent': cited_pub,
                                'citing_patent_info': info,
                                'cpc_data': patent.get('cpc', '[]')
                            })
        except:
            continue

print(f"Found {len(citing_patents)} citations from non-UC assignees")

# Analyze unique assignees and their citations
assignee_citations = defaultdict(list)
uc_citations_by_assignee = defaultdict(set)  # Which UC patents each assignee cites

for citation in citing_patents:
    assignee = citation['citing_assignee']
    uc_patent = citation['cited_uc_patent']
    assignee_citations[assignee].append(citation)
    uc_citations_by_assignee[assignee].add(uc_patent)

print(f"Found {len(assignee_citations)} unique non-UC assignees that cite UC patents")
print("Top assignees:")
for assignee in list(assignee_citations.keys())[:10]:
    print(f"  {assignee}: {len(assignee_citations[assignee])} citations")

print('__RESULT__:')
result = {
    'uc_patents': len(uc_patents),
    'uc_pub_numbers': len(uc_pub_numbers),
    'total_citations': len(citing_patents),
    'unique_assignees': len(assignee_citations),
    'sample_assignees': list(assignee_citations.keys())[:10]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
