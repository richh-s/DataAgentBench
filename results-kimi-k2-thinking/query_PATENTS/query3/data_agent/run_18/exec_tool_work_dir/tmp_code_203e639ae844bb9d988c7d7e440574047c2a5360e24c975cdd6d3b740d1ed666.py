code = """import json
import re
from collections import defaultdict

# Load California patents data
file_path_cal = 'file_storage/functions.query_db:10.json'
with open(file_path_cal, 'r') as f:
    cal_pats = json.load(f)

# Load all patents with citations (larger dataset)
file_path_all = 'file_storage/functions.query_db:36.json'
with open(file_path_all, 'r') as f:
    all_pats = json.load(f)

# Extract California publication numbers
cal_pub_numbers = set()
for patent in cal_pats:
    patents_info = patent.get('Patents_info', '')
    pub_match = re.search(r'(?:pub\. number |publication number )([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]?)', patents_info)
    if pub_match:
        cal_pub_numbers.add(pub_match.group(1))

print(f'California publications: {len(cal_pub_numbers)}')
print(f'First few: {list(cal_pub_numbers)[:5]}')

# Find all patents that cite California patents (citing patents)
# And collect their CPC codes and assignees
citing_patent_data = []  # List of (citing_patent_info, cited_cal_pub, cpc_codes, assignee)

for patent in all_pats:
    citation_str = patent.get('citation', '')
    if not citation_str or citation_str == '[]':
        continue
    
    # Check each California publication to see if it's cited
    cited_cal_pubs = []
    for cal_pub in cal_pub_numbers:
        if cal_pub in citation_str:
            cited_cal_pubs.append(cal_pub)
    
    if cited_cal_pubs:
        # This patent cites at least one California patent
        patents_info = patent.get('Patents_info', '')
        cpc_str = patent.get('cpc', '')
        
        # Extract assignee
        assignee_match = re.search(r'(?:owned by|assigned to|holds?) (?:the )?([A-Z][A-Z\s]+)', patents_info)
        assignee = assignee_match.group(1).strip() if assignee_match else 'UNKNOWN'
        
        # Get CPC codes
        cpc_codes = []
        if cpc_str and cpc_str.strip() != '[]' and cpc_str != 'No CPC data':
            try:
                cpc_str_clean = cpc_str.replace("'", '"')
                cpc_list = json.loads(cpc_str_clean)
                for cpc_item in cpc_list:
                    if isinstance(cpc_item, dict) and 'code' in cpc_item:
                        code = cpc_item['code']
                        # Extract subclass like Y02B
                        subclass_match = re.match(r'([A-Z][0-9][A-Z0-9]{2})', code)
                        if subclass_match:
                            cpc_codes.append(subclass_match.group(1))
            except:
                pass
        
        citing_patent_data.append({
            'citing_patent_info': patents_info,
            'cited_cal_pubs': cited_cal_pubs,
            'cpc_subclasses': list(set(cpc_codes)),
            'assignee': assignee
        })

# Filter out UNIV CALIFORNIA assignees (excluding self-citations)
non_cal_citing = [p for p in citing_patent_data if 'UNIV CALIFORNIA' not in p['assignee']]

print(f'Total citing patents found: {len(citing_patent_data)}')
print(f'Non-UNIV CALIFORNIA citing patents: {len(non_cal_citing)}')

# Group by assignee and collect CPC subclasses
assignee_cpc_map = defaultdict(set)
for patent in non_cal_citing:
    assignee = patent['assignee']
    for cpc_subclass in patent['cpc_subclasses']:
        assignee_cpc_map[assignee].add(cpc_subclass)

print(f'Number of unique assignees citing California patents: {len(assignee_cpc_map)}')

# Prepare summary
top_assignees = []
for assignee, cpc_set in assignee_cpc_map.items():
    top_assignees.append({
        'assignee': assignee,
        'cpc_subclasses': sorted(list(cpc_set))[:10]  # Limit to first 10
    })

# Sort by number of CPC subclasses
top_assignees.sort(key=lambda x: len(x['cpc_subclasses']), reverse=True)

print('\n__RESULT__:')
print(json.dumps({
    'citing_assignees_count': len(assignee_cpc_map),
    'top_assignees': top_assignees[:15],  # Show top 15
    'total_citing_patents': len(non_cal_citing)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'type': "<class 'str'>", 'is_str': True, 'length': 39, 'preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'num_records': 169, 'sample_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.execute_python:20': {'num_cal_pats': 169, 'num_cited_pubs': 1112, 'sample_cited': ['US-6110908-A', 'US-2010047805-A1', 'US-2020194615-A1', 'US-4911920-A', 'US-2017026797-A1', 'US-2007005261-A1', 'US-5779924-A', 'US-2014179006-A1', 'WO-2012103519-A2', 'US-5763416-A']}, 'var_functions.query_db:22': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:26': [{'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.execute_python:28': {'num_cal_pats': 169, 'num_pub_numbers': 329, 'sample_pub_numbers': ['AU-2002254753-B2', 'JP-2009260386-A', 'US-6750960-B2', 'US-2017294981-A1', 'US-2019050475-W', 'US-11248107-B2', 'US-60880790-A', 'US-2023073050-W', 'AU-2005269556-A1', 'EP-19908337-A', 'US-201715625819-A', 'CN-103687626-A', 'US-2017145219-A1', 'CA-2562038-C', 'CA-2718348-C']}, 'var_functions.execute_python:30': {'num_cal_pats': 169, 'num_cited_pubs': 1112, 'sample_cited': ['US-2009312537-A1', 'WO-2014093712-A1', 'US-8932814-B2', 'US-6016220-A', 'US-10231998-B2', 'US-7190004-B2', 'US-2004039008-A1', 'US-2016038741-A1', 'US-2011002889-A1', 'US-8697359-B1']}, 'var_functions.query_db:32': [], 'var_functions.execute_python:34': {'num_cal_pats': 169, 'num_cal_pub_numbers': 329, 'cal_pub_numbers': ['US-201715646074-A', 'AU-2004253879-A', 'US-202117798325-A', 'WO-2024050335-A2', 'MX-2013002850-A', 'US-17323505-A', 'US-2017294981-A1', 'AU-2898989-A', 'US-11445941-B2', 'AP-2011005954-A', 'CN-200380105631-A', 'JP-2014180140-A', 'EP-0826155-A4', 'US-11546022-B2', 'CA-3027364-A1', 'AP-3334-A', 'KR-20167024476-A', 'US-11607427-B2', 'JP-S6163700-A', 'EP-00992018-A']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'total_patents_with_citations': 5000, 'cal_pub_numbers_count': 329, 'citing_patents_found': 0, 'citing_sample': []}, 'var_functions.execute_python:42': {'num_cal_pats': 169, 'num_cal_pub_numbers': 114, 'sample_pub_numbers': ['AU-2010214112-B2', 'RO-70061-A', 'EP-0826155-A4', 'US-7052856-B2', 'CN-102067370-B', 'KR-20050085437-A', 'US-12025581-B2', 'US-11072681-B2', 'US-6237292-B1', 'US-2004115131-A1']}, 'var_functions.execute_python:44': {'total_cal_pats': 169, 'valid_cal_pats': 128, 'sample_data': {'US-2022074631-A1': {'cpc_subclasses': [], 'assignee': 'UNIV CALIFORNIA'}, 'US-11421276-B2': {'cpc_subclasses': [], 'assignee': 'UNIV CALIFORNIA'}, 'JP-S6163700-A': {'cpc_subclasses': [], 'assignee': 'UNIV CALIFORNIA'}}}, 'var_functions.execute_python:46': {'total_cal_pats': 169, 'pats_with_cpc': 0, 'sample_cpc_data': {}}, 'var_functions.execute_python:48': {'sample_cpc_field': 'No CPC data', 'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}}

exec(code, env_args)
