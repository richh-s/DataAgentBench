code = """import json
import re

# Load UNIV CALIFORNIA publication numbers from the previous query
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract all publication numbers for UNIV CALIFORNIA
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        uc_pub_numbers.add(pub_match.group(1))

# Load the large dataset from all patents
all_patents_file = locals()['var_functions.query_db:24']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Find patents that cite UNIV CALIFORNIA patents
citing_mappings = []

for patent in all_patents:
    patents_info = patent['Patents_info']
    citation = patent['citation']
    
    # Skip UNIV CALIFORNIA patents themselves
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Extract the assignee
    assignee_match = re.search(r'^([A-Z][A-Z0-9\s&.-]+)\s+(holds|hold|is|assigned)', patents_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()
    else:
        # Try alternative pattern
        assignee_match = re.search(r'^(In [A-Z]{2},\s+)?([A-Z][A-Z0-9\s&.-]+)\s+(holds|hold|is owned by|is assigned to)', patents_info)
        if assignee_match:
            assignee = assignee_match.group(2).strip()
        else:
            assignee = "UNKNOWN"
    
    # Remove location prefixes
    assignee = re.sub(r'^In [A-Z]{2},\s*', '', assignee)
    
    # Parse citation list to see if it cites any UNIV CALIFORNIA patents
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            pub_num = cite.get('publication_number', '')
            if pub_num in uc_pub_numbers:
                citing_mappings.append({
                    'citing_assignee': assignee,
                    'cited_pub_number': pub_num,
                    'citing_patent_info': patents_info
                })
    except:
        continue

# Group by assignee
assignee_citations = {}
for mapping in citing_mappings:
    assignee = mapping['citing_assignee']
    if assignee not in assignee_citations:
        assignee_citations[assignee] = set()
    assignee_citations[assignee].add(mapping['cited_pub_number'])

# Convert to list for easier handling
assignee_citations_list = []
for assignee, cited_nums in assignee_citations.items():
    if 'UNIV CALIFORNIA' not in assignee:  # Exclude UNIV CALIFORNIA itself
        assignee_citations_list.append({
            'assignee': assignee,
            'cited_count': len(cited_nums)
        })

# Sort by count descending
assignee_citations_list.sort(key=lambda x: x['cited_count'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_citing_patents_found': len(citing_mappings),
    'unique_citing_assignees': len(assignee_citations_list),
    'top_citing_assignees': assignee_citations_list[:20]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'uc_publication_numbers_count': 114, 'sample_uc_pub_numbers': ['US-6980295-B2', 'US-9061071-B2', 'AU-2008349842-A1', 'CN-102584712-A', 'AU-2007297661-A1', 'US-7052856-B2', 'EP-4284234-A1', 'WO-2018067976-A1', 'KR-20160119166-A', 'IL-274176-A']}, 'var_functions.execute_python:20': {'uc_pub_count': 114, 'sample_pub_numbers': ['WO-2017214343-A1', 'US-2004115131-A1', 'AU-2409401-A', 'US-2021039104-A1', 'CA-2562038-C', 'KR-20050085437-A', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'US-2017281687-A1', 'CA-2718348-C', 'WO-2012158833-A3', 'US-2019209590-A1', 'CA-3161617-A1', 'JP-S6163700-A', 'US-6980295-B2', 'US-11376346-B2', 'WO-2010045542-A3', 'AU-5938296-A', 'WO-2020055916-A9']}, 'var_functions.execute_python:22': {'checking': 'test'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
