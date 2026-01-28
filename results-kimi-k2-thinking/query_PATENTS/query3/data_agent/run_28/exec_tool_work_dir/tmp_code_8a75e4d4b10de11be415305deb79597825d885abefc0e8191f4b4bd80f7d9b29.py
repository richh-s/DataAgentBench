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

# Find all patents that cite UC patents (excluding UC itself)
citing_patents = []

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
                    # Extract cleaner assignee name
                    assignee = 'Unknown'
                    info_lower = info.lower()
                    
                    # Multiple patterns to extract assignee
                    patterns = [
                        r'([A-Z][A-Z0-9\s\.-]+?(?:\s+(?:INC|LLC|CO|LTD|CORP|GMBH|AG|PLC|SA|SAS|BV|NV|KK)))[\s,]',
                        r'([A-Z][A-Z0-9\s\.-]+?(?:\s+(?:UNIVERSITY|INSTITUTE|RESEARCH))(?:\s+(?:OF|FOR|TECHNOLOGY))?[\s,])',
                        r'([A-Z][A-Z\s]+)\s+(?:holds|assigned|owned|is)\s+(?:the|a)\s+(?:patent|application)',
                        r'^([A-Z][A-Z\s]+?)\s+(?:holds|has|owns)'
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, info, re.IGNORECASE)
                        if match:
                            assignee = match.group(1).strip()
                            break
                    
                    citing_patents.append({
                        'citing_assignee': assignee,
                        'citing_patent_info': info,
                        'cited_uc_patent': cited_pub,
                        'citing_cpc': patent.get('cpc', '[]')
                    })
        except:
            continue

print('Total patents citing UC patents:', len(citing_patents))

# Clean up assignees further and count
from collections import Counter

# Clean assignee names (remove common suffixes/prefixes)
clean_assignees = []
for patent in citing_patents:
    assignee = patent['citing_assignee']
    # Remove trailing punctuation and common words
    assignee = re.sub(r'[,.;\']+$', '', assignee)
    assignee = re.sub(r'\s+(and)\s+.*$', '', assignee, flags=re.IGNORECASE)
    clean_assignees.append(assignee.strip())

assignee_counts = Counter(clean_assignees)
print('Unique clean citing assignees:', len(assignee_counts))
print('Clean assignees:', assignee_counts)

# Show detailed info for each citing patent
for i, patent in enumerate(citing_patents):
    clean_assignee = clean_assignees[i]
    print(f"\n{i+1}. Assignee: {clean_assignee}")
    print(f"   Cites: {patent['cited_uc_patent']}")
    print(f"   Info: {patent['citing_patent_info'][:100]}...")

print('__RESULT__:')
print(json.dumps({
    'total_citing_patents': len(citing_patents),
    'assignee_breakdown': dict(assignee_counts)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'sample_citation_type': "<class 'str'>", 'sample_citation_length': 653}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_uc_patents': 169, 'total_citations': 1308}, 'var_functions.execute_python:24': {'total_cited_pub_numbers': 1112, 'sample': ['US-2016010076-A1', 'US-4642569-A', 'US-5403841-A', 'EP-0474894-A1', 'US-2010305187-A1', 'US-2010197518-A1', 'US-7074888-B1', 'US-2014245496-A1', 'US-2020245905-A1', 'US-4940658-A']}, 'var_functions.execute_python:26': {'uc_pub_numbers_count': 114, 'citation_map_size': 1112, 'sample_cited': ['US-4599677-A', 'US-2015129765-A1', 'FR-3105380-A1', 'US-11466906-B2', 'US-2001053519-A1']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_citing_patents': 4, 'unique_citing_assignees': 4, 'top_assignees': {'CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.': 1, 'Unknown': 1, 'CRYSTAL IS INC and has publication no. US-9447521-B2.': 1, 'US application (number US-2000608-A)': 1}}}

exec(code, env_args)
