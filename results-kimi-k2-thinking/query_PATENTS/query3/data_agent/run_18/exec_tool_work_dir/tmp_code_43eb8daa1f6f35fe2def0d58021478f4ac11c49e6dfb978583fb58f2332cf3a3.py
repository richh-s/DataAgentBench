code = """import json
import re
from collections import defaultdict

# Load all patents with citations
file_path = 'file_storage/functions.query_db:36.json'
with open(file_path, 'r') as f:
    all_pats_with_citations = json.load(f)

# Load California patents to get their publication numbers
file_path_cal = 'file_storage/functions.query_db:10.json'
with open(file_path_cal, 'r') as f:
    cal_pats = json.load(f)

# Extract California publication numbers
cal_pub_numbers = set()
for patent in cal_pats:
    patents_info = patent.get('Patents_info', '')
    pub_match = re.search(r'(?:pub\. number |publication number )([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]?)', patents_info)
    if pub_match:
        cal_pub_numbers.add(pub_match.group(1))
    # Also extract all patterns as fallback
    matches = re.findall(r'([A-Z]{2}-[A-Z0-9]+-[A-Z][0-9]?)', patents_info)
    for match in matches:
        cal_pub_numbers.add(match)

# Find patents that cite California patents
citing_patents = []
for patent in all_pats_with_citations:
    citation_str = patent.get('citation', '')
    if not citation_str or citation_str == '[]':
        continue
    
    # Check if this patent cites any California publication
    for cal_pub in cal_pub_numbers:
        if cal_pub in citation_str:
            citing_patents.append(patent)
            break

print('__RESULT__:')
print(json.dumps({
    'total_patents_with_citations': len(all_pats_with_citations),
    'cal_pub_numbers_count': len(cal_pub_numbers),
    'citing_patents_found': len(citing_patents),
    'citing_sample': citing_patents[:3] if citing_patents else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'type': "<class 'str'>", 'is_str': True, 'length': 39, 'preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'num_records': 169, 'sample_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.execute_python:20': {'num_cal_pats': 169, 'num_cited_pubs': 1112, 'sample_cited': ['US-6110908-A', 'US-2010047805-A1', 'US-2020194615-A1', 'US-4911920-A', 'US-2017026797-A1', 'US-2007005261-A1', 'US-5779924-A', 'US-2014179006-A1', 'WO-2012103519-A2', 'US-5763416-A']}, 'var_functions.query_db:22': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:26': [{'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.execute_python:28': {'num_cal_pats': 169, 'num_pub_numbers': 329, 'sample_pub_numbers': ['AU-2002254753-B2', 'JP-2009260386-A', 'US-6750960-B2', 'US-2017294981-A1', 'US-2019050475-W', 'US-11248107-B2', 'US-60880790-A', 'US-2023073050-W', 'AU-2005269556-A1', 'EP-19908337-A', 'US-201715625819-A', 'CN-103687626-A', 'US-2017145219-A1', 'CA-2562038-C', 'CA-2718348-C']}, 'var_functions.execute_python:30': {'num_cal_pats': 169, 'num_cited_pubs': 1112, 'sample_cited': ['US-2009312537-A1', 'WO-2014093712-A1', 'US-8932814-B2', 'US-6016220-A', 'US-10231998-B2', 'US-7190004-B2', 'US-2004039008-A1', 'US-2016038741-A1', 'US-2011002889-A1', 'US-8697359-B1']}, 'var_functions.query_db:32': [], 'var_functions.execute_python:34': {'num_cal_pats': 169, 'num_cal_pub_numbers': 329, 'cal_pub_numbers': ['US-201715646074-A', 'AU-2004253879-A', 'US-202117798325-A', 'WO-2024050335-A2', 'MX-2013002850-A', 'US-17323505-A', 'US-2017294981-A1', 'AU-2898989-A', 'US-11445941-B2', 'AP-2011005954-A', 'CN-200380105631-A', 'JP-2014180140-A', 'EP-0826155-A4', 'US-11546022-B2', 'CA-3027364-A1', 'AP-3334-A', 'KR-20167024476-A', 'US-11607427-B2', 'JP-S6163700-A', 'EP-00992018-A']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
