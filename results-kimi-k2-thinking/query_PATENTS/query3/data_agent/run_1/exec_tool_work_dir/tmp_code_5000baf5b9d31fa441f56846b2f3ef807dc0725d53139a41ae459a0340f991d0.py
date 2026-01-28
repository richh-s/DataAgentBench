code = """import json
import re
from collections import defaultdict

# Load the full publication database
full_db_path = locals()['var_functions.query_db:30']

with open(full_db_path, 'r') as f:
    patents_data = json.load(f)

print(f'Total patents in database: {len(patents_data)}')

# Extract UC patents and their publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info:
        uc_patents.append(patent)
        # Try different patterns to extract publication numbers
        patterns = [
            r'pub[\.\s]*number[\s:]+([A-Z0-9-]+)',  # pub. number
            r'publication number[\s:]+([A-Z0-9-]+)',  # publication number
            r'with\s+[A-Z0-9-]+[,-]\s*([A-Z0-9-]+)',  # ...with US-12345-B2
            r'([A-Z0-9-]{10,})',  # Any long alphanumeric pattern
        ]
        
        for pattern in patterns:
            pub_match = re.search(pattern, patents_info)
            if pub_match:
                pub_num = pub_match.group(1)
                if len(pub_num) > 8:  # Filter out short matches
                    uc_pub_numbers.add(pub_num)
                    break

print(f'Found {len(uc_patents)} UNIV CALIFORNIA patents')
print(f'Distinct UC publication numbers: {len(uc_pub_numbers)}')

# Find all patents that cite these UC patents
citing_assignees = defaultdict(set)
citing_patents = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    
    # Skip if this is a UNIV CALIFORNIA patent
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Extract assignee using multiple patterns
    assignee = None
    assignee_patterns = [
        r'^([A-Z][A-Z\s&\-\.\d]+)\s+(holds|is|owns)',  # starts with company name
        r'is assigned to\s+([A-Z][A-Z\s&\-\.\d]+)',  # assigned to ...
        r'is owned by\s+([A-Z][A-Z\s&\-\.\d]+)',  # owned by ...
    ]
    
    for pattern in assignee_patterns:
        assignee_match = re.search(pattern, patents_info)
        if assignee_match:
            assignee = (assignee_match.group(1) or '').strip()
            if len(assignee) > 3:  # Ensure it's a reasonable length
                break
    
    # Check citations
    citation_text = patent.get('citation', '')
    if citation_text and citation_text != '[]':
        try:
            citations = json.loads(citation_text)
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                if cited_pub in uc_pub_numbers:
                    citing_patents.append(patent)
                    if assignee:
                        citing_assignees[assignee].add(cited_pub)
        except:
            continue

print(f'Found {len(citing_patents)} patents that cite UNIV CALIFORNIA patents')
print(f'Found {len(citing_assignees)} unique citing assignees')

# Now extract CPC subclasses for citing patents
all_cpc_codes = set()
for patent in citing_patents:
    cpc_text = patent.get('cpc', '')
    if cpc_text and cpc_text != '[]':
        try:
            cpc_entries = json.loads(cpc_text)
            for entry in cpc_entries:
                code = entry.get('code', '')
                if code:
                    # Extract primary subclass (first 4 characters after letter)
                    subclass_match = re.match(r'([A-Z][0-9]{2}[A-Z])', code)
                    if subclass_match:
                        all_cpc_codes.add(subclass_match.group(1))
        except:
            continue

print(f'Found {len(all_cpc_codes)} unique CPC subclasses in citing patents')

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'citing_patents_count': len(citing_patents),
    'citing_assignees_count': len(citing_assignees),
    'cpc_subclasses_count': len(all_cpc_codes),
    'top_citing_assignees': [[k, list(v)] for k, v in list(citing_assignees.items())[:10]],
    'cpc_subclasses_sample': list(all_cpc_codes)[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_patents': 5, 'uc_patents': 10, 'sample_structure': ['Patents_info', 'cpc', 'citation'], 'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.execute_python:12': {'uc_patents_count': 10, 'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.execute_python:16': {'uc_patents_analyzed': 10, 'uc_pub_numbers_found': 5, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1']}, 'var_functions.execute_python:20': {'uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1'], 'count': 5}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': {'uc_pub_numbers': ['TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2022074631-A1', 'US-2017281687-A1'], 'count': 5}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'uc_patents_count': 169, 'uc_pub_numbers': ['CN-100339724-C', 'US-2017145219-A1', 'CA-2298540-A1', 'KR-20200041324-A', 'CN-103189548-A', 'US-11376346-B2', 'IL-244029-A0', 'RO-70061-A', 'US-2020025859-A1', 'WO-2020055916-A9', 'IL-274176-A', 'US-2006292670-A1', 'US-11667770-B2', 'US-2023321419-A1', 'WO-2023225482-A3', 'US-9061071-B2', 'US-2022074631-A1', 'HK-1250569-A1', 'US-6767662-B2', 'US-2017281687-A1', 'US-2021000566-A1', 'EP-1212462-A1', 'WO-2024044766-A3', 'JP-S6163700-A', 'AU-2010214112-B2', 'CA-2562038-C', 'WO-2010045542-A3', 'CN-102584712-A', 'AU-2019275518-B2', 'EP-4284234-A1', 'AU-6535890-A', 'US-2019328740-A1', 'AU-2008349842-A1', 'WO-2021102420-A1', 'US-6750960-B2', 'ID-23426-A', 'WO-2018026404-A3', 'US-2023171142-A1', 'US-5304932-A', 'WO-2012162563-A2', 'US-2022018060-A1', 'TW-201925402-A', 'EP-0826155-A4', 'US-2021101879-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'MX-2013002850-A', 'US-2006051790-A1', 'AU-2007297661-A1', 'WO-2024112568-A1', 'US-11546022-B2', 'US-2023155090-A1', 'JP-2014224156-A', 'US-5547866-A', 'CA-2550552-A1', 'CN-102067370-B', 'AU-2015364602-B2', 'US-2018243924-A1', 'US-2023279470-A1'], 'citing_patents_count': 1, 'citing_assignees_count': 0, 'top_citing_assignees': []}}

exec(code, env_args)
