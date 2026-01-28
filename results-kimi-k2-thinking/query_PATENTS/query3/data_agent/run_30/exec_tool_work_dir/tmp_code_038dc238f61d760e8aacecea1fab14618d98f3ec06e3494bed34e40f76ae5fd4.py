code = """import json, re
print('__RESULT__:')

# Load all data
all_data = globals()['var_functions.query_db:28']
if isinstance(all_data, str):
    with open(all_data, 'r') as f:
        all_data = json.load(f)

univ_data = globals()['var_functions.query_db:12']
if isinstance(univ_data, str):
    with open(univ_data, 'r') as f:
        univ_data = json.load(f)

# Get UNIV CALIFORNIA publication numbers
univ_pub_numbers = set()
for record in univ_data:
    patents_info = record.get('Patents_info', '')
    # More flexible regex to capture various formats
    pub_match = re.search(r'pub\. (?:number|no\.) ([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]+)', patents_info)
    if pub_match:
        univ_pub_numbers.add(pub_match.group(1))

# Find citing patents and their CPCs
citations_info = []
for record in all_data:
    patents_info = record.get('Patents_info', '')
    citation_str = record.get('citation', '')
    cpc_str = record.get('cpc', '')
    
    if not citation_str or citation_str == '[]':
        continue
    
    # Get assignee of current record
    assignee = 'Unknown'
    # Try different patterns
    patterns = [
        r'^([A-Z\s&\-0-9]+?)\s+(holds|is (owned by|assigned to|belonging to))',
        r'^The ([A-Z\s&\-0-9]+?) patent',
        r'^In [A-Z]{2}, the patent.*? (?:owned by|assigned to|belonging to) ([A-Z\s&\-0-9]+?) and'
    ]
    
    for pattern in patterns:
        assignee_match = re.search(pattern, patents_info, re.IGNORECASE)
        if assignee_match:
            assignee = assignee_match.group(1).strip()
            break
    
    # Skip UNIV CALIFORNIA itself
    if 'UNIV CALIFORNIA' in assignee:
        continue
    
    # Parse citations
    try:
        citations = json.loads(citation_str)
        cites_california = False
        for citation in citations:
            cited_pub = citation.get('publication_number', '')
            if cited_pub in univ_pub_numbers:
                cites_california = True
                break
        
        if cites_california:
            # Get CPC codes (primary inventive ones)
            cpc_codes = []
            if cpc_str and cpc_str != '[]':
                try:
                    cpc_entries = json.loads(cpc_str)
                    for entry in cpc_entries:
                        if entry.get('inventive') and entry.get('first'):
                            code = entry.get('code', '')
                            # Extract subclass (first 4 characters + first letter after slash)
                            if len(code) >= 4:
                                subclass = code[:4]
                                cpc_codes.append(subclass)
                except:
                    pass
            
            if assignee != 'Unknown':
                citations_info.append({
                    'assignee': assignee,
                    'cpc_subclasses': list(set(cpc_codes)) if cpc_codes else []
                })
                
    except Exception as e:
        continue

result = {
    'total_citing_patents': len(citations_info),
    'sample_patents': citations_info[:10]
}
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': 'Test output', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:34': {'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:12', 'var_functions.execute_python:26', 'var_functions.query_db:28', '__builtins__', 'json']}, 'var_functions.execute_python:36': {'univ_records': 169, 'all_records': 277813, 'sample_univ': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'sample_all': {'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}}, 'var_functions.list_db:38': ['cpc_definition'], 'var_functions.execute_python:42': {'message': 'Found 43 UNIV CALIFORNIA publication numbers', 'sample_pubs': ['AU-2008349842-A1', 'US-2018243924-A1', 'US-2020025859-A1', 'WO-2024112568-A1', 'US-2021000566-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'CA-2550552-A1', 'IL-244029-A0', 'US-2006051790-A1']}, 'var_functions.execute_python:44': {'citing_assignees_count': 0, 'sample_citing_assignees': [], 'total_citing_records': 0}, 'var_functions.execute_python:46': {'sample_citations': [], 'total_records': 277813}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'Y02B30/00', 'titleFull': 'Energy efficient heating, ventilation or air conditioning [HVAC]'}]}

exec(code, env_args)
