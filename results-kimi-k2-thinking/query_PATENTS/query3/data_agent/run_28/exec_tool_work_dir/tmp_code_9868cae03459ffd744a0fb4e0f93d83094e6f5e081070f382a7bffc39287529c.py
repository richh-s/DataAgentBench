code = """import json
import re

# Get all patents data
all_patents_file = locals()['var_functions.query_db:28']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Get UC patents data
uc_patents_file = locals()['var_functions.query_db:20']
with open(uc_patents_file, 'r') as f:
    uc_patents = json.load(f)

# Build a set of UC publication numbers for quick lookup
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1))

print('UC publication numbers:', len(uc_pub_numbers))

# Find all patents that cite UC patents (excluding UC itself)
citing_patents = []
uc_citations = {}  # uc_patent -> list of citing patent info

for patent in all_patents:
    # Skip if this is a UC patent
    info = patent['Patents_info']
    if 'UNIV CALIFORNIA' in info:
        continue
    
    # Check if this patent cites any UC patents
    citations_str = patent.get('citation', '[]')
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for citation in citations:
                cited_pub = citation.get('publication_number')
                if cited_pub and cited_pub in uc_pub_numbers:
                    # Find assignee of citing patent
                    assignee_match = re.search(r'(?:owned by|assigned to|holds the|is owned by|is assigned to)\s+([^,]+)', info, re.IGNORECASE)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                    else:
                        assignee = 'Unknown'
                    
                    citing_patents.append({
                        'citing_assignee': assignee,
                        'citing_patent_info': info,
                        'cited_uc_patent': cited_pub,
                        'citing_cpc': patent.get('cpc', '[]')
                    })
                    
                    # Track which UC patent was cited
                    if cited_pub not in uc_citations:
                        uc_citations[cited_pub] = []
                    uc_citations[cited_pub].append({'assignee': assignee, 'info': info})
        except:
            continue

print('Total patents citing UC patents:', len(citing_patents))
print('Unique citing assignees:', len(set(p['citing_assignee'] for p in citing_patents)))

# Show top citing assignees
from collections import Counter
assignee_counts = Counter(p['citing_assignee'] for p in citing_patents)
print('Top 10 citing assignees:')
for assignee, count in assignee_counts.most_common(10):
    print(f'  {assignee}: {count} citations')

print('__RESULT__:')
print(json.dumps({
    'total_citing_patents': len(citing_patents),
    'unique_citing_assignees': len(set(p['citing_assignee'] for p in citing_patents)),
    'top_assignees': dict(assignee_counts.most_common(10))
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'sample_citation_type': "<class 'str'>", 'sample_citation_length': 653}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_uc_patents': 169, 'total_citations': 1308}, 'var_functions.execute_python:24': {'total_cited_pub_numbers': 1112, 'sample': ['US-2016010076-A1', 'US-4642569-A', 'US-5403841-A', 'EP-0474894-A1', 'US-2010305187-A1', 'US-2010197518-A1', 'US-7074888-B1', 'US-2014245496-A1', 'US-2020245905-A1', 'US-4940658-A']}, 'var_functions.execute_python:26': {'uc_pub_numbers_count': 114, 'citation_map_size': 1112, 'sample_cited': ['US-4599677-A', 'US-2015129765-A1', 'FR-3105380-A1', 'US-11466906-B2', 'US-2001053519-A1']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
