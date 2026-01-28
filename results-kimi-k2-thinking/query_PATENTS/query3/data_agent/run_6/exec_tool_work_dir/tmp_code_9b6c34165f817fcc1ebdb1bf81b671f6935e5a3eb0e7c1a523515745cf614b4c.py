code = """import json
import re
from collections import defaultdict

# Load all patent data
file_path = locals()['var_functions.query_db:28']
with open(file_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded:', len(all_patents))

# Build UNIV CALIFORNIA publication numbers set (normalize format)
univ_calif_pubs = set()
for rec in all_patents:
    patents_info = rec['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        # Extract publication numbers more carefully
        # Look for patterns and normalize
        patterns = [
            r'pub\. number\s+([A-Z]{2,3}-[^,\s\]]+)',
            r'publication number\s+([A-Z]{2,3}-[^,\s\]]+)',
            r'publication no\.\s+([A-Z]{2,3}-[^,\s\]]+)',
            r'pub\. no\.\s+([A-Z]{2,3}-[^,\s\]]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, patents_info, re.IGNORECASE)
            if match:
                pub_num = match.group(1).rstrip('.')
                # Normalize: remove trailing period if exists
                if pub_num.endswith('.'):
                    pub_num = pub_num[:-1]
                univ_calif_pubs.add(pub_num)
                break

print('UNIV CALIFORNIA publications found:', len(univ_calif_pubs))
print('Sample:', list(univ_calif_pubs)[:5])

# Now find ALL patents that cite these publications
citing_patents = []
county = 0

for rec in all_patents:
    county += 1
    if county % 50000 == 0:
        print(f'Checked {county}/{len(all_patents)} records...')
    
    # Skip UNIV CALIFORNIA patents
    patents_info = rec['Patents_info']
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    citations_str = rec['citation']
    if not citations_str or citations_str == '[]':
        continue
    
    try:
        citations = json.loads(citations_str)
        for cite in citations:
            pub_num = cite.get('publication_number', '')
            if pub_num:
                # Normalize cited publication number
                if pub_num.endswith('.'):
                    pub_num = pub_num[:-1]
                
                if pub_num in univ_calif_pubs:
                    # Found a patent that cites UNIV CALIFORNIA
                    
                    # Extract assignee
                    assignee = None
                    info = patents_info
                    
                    # More robust assignee extraction
                    patterns = [
                        r'is assigned to\s+([^,]+?)(?:\s+and\s+has|\s+with\s+pub|\s+with\s+publication|\s+and\s+pub|\.|$)',
                        r'is owned by\s+([^,]+?)(?:\s+and\s+has|\s+with\s+pub|\s+with\s+publication|\s+and\s+pub|\.|$)',
                        r'held by\s+([^,]+?)(?:\s+and\s+has|\s+with\s+pub|\s+with\s+publication|\s+and\s+pub|\.|$)',
                        r'belonging to\s+([^,]+?)(?:\s+and\s+has|\s+with\s+pub|\s+with\s+publication|\s+and\s+pub|\.|$)',
                        r'from\s+([^,]+?)(?:\s+and\s+has|\s+with\s+pub|\s+with\s+publication|\s+and\s+pub|\.|$)'
                    ]
                    
                    for pat in patterns:
                        match = re.search(pat, info)
                        if match:
                            assignee = match.group(1).strip()
                            # Remove trailing phrases
                            assignee = re.sub(r'\s+and\s+pub.*', '', assignee, flags=re.IGNORECASE)
                            assignee = re.sub(r'\s+with\s+pub.*', '', assignee, flags=re.IGNORECASE)
                            assignee = re.sub(r'\s+and\s+has.*', '', assignee, flags=re.IGNORECASE)
                            break
                    
                    # Extract CPC codes
                    cpc_codes = []
                    if rec['cpc'] and rec['cpc'] != '[]':
                        try:
                            cpc_list = json.loads(rec['cpc'])
                            cpc_codes = [item['code'] for item in cpc_list]
                        except:
                            pass
                    
                    citing_patents.append({
                        'assignee': assignee,
                        'cpc_codes': cpc_codes,
                        'cites': pub_num
                    })
                    break
    except:
        pass

print('Citing patents found:', len(citing_patents))

# Group by assignee (excluding UNIV CALIFORNIA)
assignee_info = defaultdict(lambda: {'cpc_codes': set(), 'cites_count': 0})

for data in citing_patents:
    assignee = data['assignee']
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    
    assignee_clean = assignee.strip()
    assignee_info[assignee_clean]['cites_count'] += 1
    for cpc in data['cpc_codes']:
        assignee_info[assignee_clean]['cpc_codes'].add(cpc)

print('Unique citing assignees:', len(assignee_info))
print('Sample assignees:', list(assignee_info.keys())[:10])

# Prepare for CPC lookup
all_cpc_codes = set()
for info in assignee_info.values():
    all_cpc_codes.update(info['cpc_codes'])

result = {
    'total_citing_assignees': len(assignee_info),
    'total_cpc_codes_to_lookup': len(all_cpc_codes),
    'assignees': list(assignee_info.keys()),
    'cpc_codes': list(all_cpc_codes)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}, 'var_functions.execute_python:36': {'total_univ_calif_patents': 169, 'unique_cited_publications': 1112, 'citations_with_pub_numbers': 1112}, 'var_functions.execute_python:38': {'total_cited_by_univ_calif': 1112, 'total_univ_calif_publications': 114, 'sample_univ_calif_pubs': ['US-11421276-B2.', 'EP-3668487-A4.', 'KR-20050085437-A.', 'US-2020283856-A1.', 'EP-0826155-A4.', 'WO-2021102420-A1.', 'US-2009031436-A1.', 'JP-2009260386-A.', 'US-11014955-B2.', 'PT-2970346-T.']}, 'var_functions.execute_python:42': {'total_patents': 277813, 'univ_calif_patents': 169, 'sample_pubs': ['US-2003112494-A1', 'KR-100228821-B1', 'IL-274176-A', 'US-2020025859-A1', 'US-2021000566-A1', 'US-6750960-B2', 'WO-2024112568-A1', 'AU-2015364602-B2', 'PE-20130764-A1', 'EP-3668487-A4']}, 'var_functions.execute_python:44': {'total_university_california_pubs': 114, 'citing_patents_found': 4, 'sample_citing_patent': {'patent_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'cites': 'US-6237292-B1', 'cpc': '[\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01M7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01V1/01",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:46': {'total_citing_patents': 1, 'unique_assignees': 1, 'sample_assignees': ['BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'cpc_codes_to_lookup': ['H01M2008/1293', 'H01M2004/8684', 'H01M8/2457', 'H01M8/1253', 'H01M4/8657', 'H01M4/8652', 'Y02E60/525', 'Y02E60/50', 'H01M4/8642', 'H01M4/8663', 'H01M4/861', 'H01M4/9066', 'H01M8/2425', 'H01M4/8885', 'H01M4/9016', 'Y02P70/56', 'Y02P70/50']}, 'var_functions.execute_python:48': {'total_citing_patents': 1, 'unique_assignees': 1, 'assignees': ['BLOOM ENERGY CORP']}}

exec(code, env_args)
