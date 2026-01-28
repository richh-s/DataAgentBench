code = """import json
import re

# Load UNIV CALIFORNIA publication numbers
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract all UNIV CALIFORNIA publication numbers as a set
uc_pub_numbers = set()
uc_cpc_mapping = {}  # Map UC pub number to its CPC codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc = patent.get('cpc', '[]')
    
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.add(pub_num)
        
        # Store CPC codes for this UC patent
        try:
            cpc_codes = json.loads(cpc)
            cpc_list = list(set([code['code'] for code in cpc_codes]))
            uc_cpc_mapping[pub_num] = cpc_list
        except:
            uc_cpc_mapping[pub_num] = []

# Load all patents from the sample
all_patents_file = locals()['var_functions.query_db:24']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Find patents that cite UNIV CALIFORNIA patents
citation_mappings = []  # List of {citing_assignee, uc_pub_number, citing_cpc}

for patent in all_patents:
    patents_info = patent['Patents_info']
    citation = patent.get('citation', '[]')
    patent_cpc = patent.get('cpc', '[]')
    
    # Extract citing assignee
    if 'UNIV CALIFORNIA' in patents_info:
        continue  # Skip UNIV CALIFORNIA itself
    
    # Get assignee name
    assignee_match = re.search(r'^([A-Z][A-Z0-9\s&.,-]+?)\s+(holds|hold|is|assigned)', patents_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()
    else:
        assignee_match = re.search(r'^(In [A-Z]{2},\s+)?([A-Z][A-Z0-9\s&.,-]+?)\s+(holds|hold|is owned by|is assigned to)', patents_info)
        if assignee_match:
            assignee = assignee_match.group(2).strip()
        else:
            continue
    
    # Clean assignee name
    assignee = re.sub(r'^In [A-Z]{2},\s*', '', assignee)
    
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            cited_pub = cite.get('publication_number', '')
            if cited_pub in uc_pub_numbers:
                # This patent cites a UC patent, get its CPC codes
                try:
                    citing_cpc_codes = json.loads(patent_cpc)
                    citing_cpc_list = list(set([code['code'] for code in citing_cpc_codes]))
                except:
                    citing_cpc_list = []
                
                citation_mappings.append({
                    'citing_assignee': assignee,
                    'cited_uc_pub': cited_pub,
                    'cited_cpc_codes': uc_cpc_mapping.get(cited_pub, []),
                    'citing_cpc_codes': citing_cpc_list
                })
    except:
        continue

# Group by assignee to get unique assignees
assignee_data = {}
for mapping in citation_mappings:
    assignee = mapping['citing_assignee']
    if assignee not in assignee_data:
        assignee_data[assignee] = {
            'cited_uc_pubs': set(),
            'all_cpc_codes': set()
        }
    assignee_data[assignee]['cited_uc_pubs'].add(mapping['cited_uc_pub'])
    assignee_data[assignee]['all_cpc_codes'].update(mapping['cited_cpc_codes'])
    assignee_data[assignee]['all_cpc_codes'].update(mapping['citing_cpc_codes'])

# Convert to list and sort by number of cited UC patents
assignee_list = [{'assignee': k, 'cited_uc_count': len(v['cited_uc_pubs']), 'cpc_codes': list(v['all_cpc_codes'])} 
                 for k, v in assignee_data.items()]
assignee_list.sort(key=lambda x: x['cited_uc_count'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_citations_found': len(citation_mappings),
    'unique_citing_assignees': len(assignee_list),
    'citing_assignees': assignee_list[:20],  # Top 20
    'sample_cpc_codes': list(set([code for assignee in assignee_list[:5] for code in assignee['cpc_codes']]))[:20]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'uc_publication_numbers_count': 114, 'sample_uc_pub_numbers': ['US-6980295-B2', 'US-9061071-B2', 'AU-2008349842-A1', 'CN-102584712-A', 'AU-2007297661-A1', 'US-7052856-B2', 'EP-4284234-A1', 'WO-2018067976-A1', 'KR-20160119166-A', 'IL-274176-A']}, 'var_functions.execute_python:20': {'uc_pub_count': 114, 'sample_pub_numbers': ['WO-2017214343-A1', 'US-2004115131-A1', 'AU-2409401-A', 'US-2021039104-A1', 'CA-2562038-C', 'KR-20050085437-A', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'US-2017281687-A1', 'CA-2718348-C', 'WO-2012158833-A3', 'US-2019209590-A1', 'CA-3161617-A1', 'JP-S6163700-A', 'US-6980295-B2', 'US-11376346-B2', 'WO-2010045542-A3', 'AU-5938296-A', 'WO-2020055916-A9']}, 'var_functions.execute_python:22': {'checking': 'test'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_citing_patents_found': 0, 'unique_citing_assignees': 0, 'top_citing_assignees': []}}

exec(code, env_args)
