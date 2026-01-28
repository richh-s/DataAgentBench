code = """import json
import re
from collections import defaultdict

# Load California patents data
file_path_cal = 'file_storage/functions.query_db:10.json'
with open(file_path_cal, 'r') as f:
    cal_pats = json.load(f)

# Load all patents with citations (large sample)
file_path_all = 'file_storage/functions.query_db:36.json'
with open(file_path_all, 'r') as f:
    all_pats = json.load(f)

# Extract California publication numbers
cal_pub_numbers = set()
for patent in cal_pats:
    info = patent.get('Patents_info', '')
    # Extract pub. number or publication number
    match = re.search(r'(?:pub\. number|publication number) ([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]?)', info)
    if match:
        cal_pub_numbers.add(match.group(1))

print(f'Found {len(cal_pub_numbers)} California publication numbers')
print(f'Sample: {list(cal_pub_numbers)[:5]}')

# Process citations more carefully - we'll parse the JSON citation field
citing_assignee_cpc = defaultdict(set)
total_checked = 0
potential_citations = 0

for patent in all_pats:
    citation_str = patent.get('citation', '')
    if not citation_str or citation_str.strip() == '[]':
        continue
    
    total_checked += 1
    citations_found = []
    
    # Try to parse the citation field as JSON
    try:
        # Clean up the string for JSON parsing
        if citation_str.startswith('[') and citation_str.endswith(']'):
            citations = json.loads(citation_str)
            for cite in citations:
                if isinstance(cite, dict):
                    pub_num = cite.get('publication_number')
                    if pub_num and pub_num in cal_pub_numbers:
                        citations_found.append(pub_num)
    except:
        # If JSON parsing fails, try simple string matching
        for cal_pub in cal_pub_numbers:
            if cal_pub in citation_str:
                citations_found.append(cal_pub)
    
    if citations_found:
        potential_citations += 1
        # Get assignee
        info = patent.get('Patents_info', '')
        assignee_match = re.search(r'^([A-Z][A-Z\s]+)', info)
        if assignee_match:
            assignee = assignee_match.group(1).strip()
            # Extract assignee name (before common keywords)
            for keyword in [' holds', ' is owned', ' is assigned', ' has', ' filed']:
                if keyword in assignee:
                    assignee = assignee.split(keyword)[0]
                    break
        elif 'PANASONIC' in info:
            assignee = 'PANASONIC IP MAN CO LTD'
        elif 'SAMSUNG' in info:
            assignee = 'SAMSUNG ELECTRONICS CO LTD'
        else:
            assignee = 'UNKNOWN'
        
        # Skip UNIV CALIFORNIA
        if 'UNIV CALIFORNIA' in assignee:
            continue
        
        # Get CPC codes
        cpc_codes = []
        cpc_str = patent.get('cpc', '')
        if cpc_str and cpc_str.strip() != '[]' and cpc_str != 'No CPC data':
            try:
                cpc_clean = cpc_str.replace("'", '"').replace('\n', '')
                cpc_list = json.loads(cpc_clean)
                for item in cpc_list:
                    if isinstance(item, dict) and 'code' in item:
                        code = item['code']
                        # Extract subclass like Y02B
                        m = re.match(r'([A-Z][0-9][A-Z0-9]{2})', code)
                        if m:
                            cpc_codes.append(m.group(1))
            except:
                pass
        
        # Add to our map
        for cpc in cpc_codes:
            citing_assignee_cpc[assignee].add(cpc)

print(f'Checked {total_checked} patents with citations')
print(f'Found {potential_citations} patents potentially citing California patents')
print(f'Found {len(citing_assignee_cpc)} non-UC assignees with CPC codes')

# Sort by number of CPC subclasses
sorted_assignees = sorted(citing_assignee_cpc.items(), key=lambda x: len(x[1]), reverse=True)

result = {
    'cal_pub_numbers': len(cal_pub_numbers),
    'patents_checked': total_checked,
    'potential_citations': potential_citations,
    'unique_assignees': len(citing_assignee_cpc),
    'top_assignees': [(assignee, sorted(list(cpcs))) for assignee, cpcs in sorted_assignees[:50]]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'type': "<class 'str'>", 'is_str': True, 'length': 39, 'preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'num_records': 169, 'sample_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.execute_python:20': {'num_cal_pats': 169, 'num_cited_pubs': 1112, 'sample_cited': ['US-6110908-A', 'US-2010047805-A1', 'US-2020194615-A1', 'US-4911920-A', 'US-2017026797-A1', 'US-2007005261-A1', 'US-5779924-A', 'US-2014179006-A1', 'WO-2012103519-A2', 'US-5763416-A']}, 'var_functions.query_db:22': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:26': [{'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.execute_python:28': {'num_cal_pats': 169, 'num_pub_numbers': 329, 'sample_pub_numbers': ['AU-2002254753-B2', 'JP-2009260386-A', 'US-6750960-B2', 'US-2017294981-A1', 'US-2019050475-W', 'US-11248107-B2', 'US-60880790-A', 'US-2023073050-W', 'AU-2005269556-A1', 'EP-19908337-A', 'US-201715625819-A', 'CN-103687626-A', 'US-2017145219-A1', 'CA-2562038-C', 'CA-2718348-C']}, 'var_functions.execute_python:30': {'num_cal_pats': 169, 'num_cited_pubs': 1112, 'sample_cited': ['US-2009312537-A1', 'WO-2014093712-A1', 'US-8932814-B2', 'US-6016220-A', 'US-10231998-B2', 'US-7190004-B2', 'US-2004039008-A1', 'US-2016038741-A1', 'US-2011002889-A1', 'US-8697359-B1']}, 'var_functions.query_db:32': [], 'var_functions.execute_python:34': {'num_cal_pats': 169, 'num_cal_pub_numbers': 329, 'cal_pub_numbers': ['US-201715646074-A', 'AU-2004253879-A', 'US-202117798325-A', 'WO-2024050335-A2', 'MX-2013002850-A', 'US-17323505-A', 'US-2017294981-A1', 'AU-2898989-A', 'US-11445941-B2', 'AP-2011005954-A', 'CN-200380105631-A', 'JP-2014180140-A', 'EP-0826155-A4', 'US-11546022-B2', 'CA-3027364-A1', 'AP-3334-A', 'KR-20167024476-A', 'US-11607427-B2', 'JP-S6163700-A', 'EP-00992018-A']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'total_patents_with_citations': 5000, 'cal_pub_numbers_count': 329, 'citing_patents_found': 0, 'citing_sample': []}, 'var_functions.execute_python:42': {'num_cal_pats': 169, 'num_cal_pub_numbers': 114, 'sample_pub_numbers': ['AU-2010214112-B2', 'RO-70061-A', 'EP-0826155-A4', 'US-7052856-B2', 'CN-102067370-B', 'KR-20050085437-A', 'US-12025581-B2', 'US-11072681-B2', 'US-6237292-B1', 'US-2004115131-A1']}, 'var_functions.execute_python:44': {'total_cal_pats': 169, 'valid_cal_pats': 128, 'sample_data': {'US-2022074631-A1': {'cpc_subclasses': [], 'assignee': 'UNIV CALIFORNIA'}, 'US-11421276-B2': {'cpc_subclasses': [], 'assignee': 'UNIV CALIFORNIA'}, 'JP-S6163700-A': {'cpc_subclasses': [], 'assignee': 'UNIV CALIFORNIA'}}}, 'var_functions.execute_python:46': {'total_cal_pats': 169, 'pats_with_cpc': 0, 'sample_cpc_data': {}}, 'var_functions.execute_python:48': {'sample_cpc_field': 'No CPC data', 'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.execute_python:52': {'cal_patents': 114, 'citing_patents': 0, 'unique_assignees': 0, 'top_assignees': []}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:58': {'cal_pats_count': 169, 'cal_pats_cpc_count': 10, 'sample_cal_pat': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}, 'sample_cal_pat_cpc': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)
