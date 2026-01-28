code = """import json
import re

# First, let's get EXACT UNIV CALIFORNIA publication numbers from the patents_info field
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract all UNIV CALIFORNIA publication numbers exactly as they appear
uc_pub_numbers = set()
uc_cpc_mapping = {}

for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Extract the exact publication number
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.add(pub_num)
        
        # Store CPC codes
        cpc = patent.get('cpc', '[]')
        try:
            cpc_codes = json.loads(cpc)
            cpc_list = [code['code'] for code in cpc_codes]
            uc_cpc_mapping[pub_num] = cpc_list
        except:
            uc_cpc_mapping[pub_num] = []

print('UNIV CALIFORNIA publication numbers:')
print('Total:', len(uc_pub_numbers))
print('Sample:', list(uc_pub_numbers)[:20])

# Now let's check citation format in a few patents
all_patents_file = locals()['var_functions.query_db:24']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Check if any patent cites any UC publication number
citation_pub_numbers = set()
for patent in all_patents:
    citation = patent.get('citation', '[]')
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            pub_num = cite.get('publication_number', '')
            if pub_num:
                citation_pub_numbers.add(pub_num)
    except:
        continue

print('\\nTotal unique publication numbers in citations:', len(citation_pub_numbers))

# Check for any overlap
overlap = uc_pub_numbers.intersection(citation_pub_numbers)
print('\\nOverlapping publication numbers (UC patents cited by others):', len(overlap))
print('Overlapping:', list(overlap)[:20])

# If no overlap, check a few citation examples that look similar to UC format
candidate_cites = []
for pub_num in uc_pub_numbers:
    # Find citations with similar format
    for cit_num in citation_pub_numbers:
        if pub_num.split('-')[0] == cit_num.split('-')[0]:  # Same country code
            candidate_cites.append((pub_num, cit_num))
print('\\nCandidate similar patterns:', candidate_cites[:20])

print('__RESULT__:')
print(json.dumps({
    'uc_pub_count': len(uc_pub_numbers),
    'citation_pub_count': len(citation_pub_numbers),
    'overlap_count': len(overlap),
    'sample_uc_pub': list(uc_pub_numbers)[:20],
    'sample_citation_pub': list(citation_pub_numbers)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'uc_publication_numbers_count': 114, 'sample_uc_pub_numbers': ['US-6980295-B2', 'US-9061071-B2', 'AU-2008349842-A1', 'CN-102584712-A', 'AU-2007297661-A1', 'US-7052856-B2', 'EP-4284234-A1', 'WO-2018067976-A1', 'KR-20160119166-A', 'IL-274176-A']}, 'var_functions.execute_python:20': {'uc_pub_count': 114, 'sample_pub_numbers': ['WO-2017214343-A1', 'US-2004115131-A1', 'AU-2409401-A', 'US-2021039104-A1', 'CA-2562038-C', 'KR-20050085437-A', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'US-2017281687-A1', 'CA-2718348-C', 'WO-2012158833-A3', 'US-2019209590-A1', 'CA-3161617-A1', 'JP-S6163700-A', 'US-6980295-B2', 'US-11376346-B2', 'WO-2010045542-A3', 'AU-5938296-A', 'WO-2020055916-A9']}, 'var_functions.execute_python:22': {'checking': 'test'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_citing_patents_found': 0, 'unique_citing_assignees': 0, 'top_citing_assignees': []}, 'var_functions.execute_python:28': {'total_citations_found': 0, 'unique_citing_assignees': 0, 'citing_assignees': [], 'sample_cpc_codes': []}}

exec(code, env_args)
