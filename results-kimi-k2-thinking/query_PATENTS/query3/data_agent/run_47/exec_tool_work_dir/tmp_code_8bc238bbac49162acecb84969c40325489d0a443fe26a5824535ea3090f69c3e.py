code = """import json
import re
import random
from collections import defaultdict

# Load California publication numbers
california_path = locals()['var_functions.query_db:14']
with open(california_path, 'r') as f:
    california_patents = json.load(f)

# Extract California publication numbers into a set for faster lookup
california_pub_nums = set()
for patent in california_patents:
    patents_info = patent['Patents_info']
    patterns = [
        r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'has publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'with publication number\s+([A-Z]{2}-[A-Z0-9-]+)',
        r'has pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)'
    ]
    for pattern in patterns:
        matches = re.findall(pattern, patents_info, re.IGNORECASE)
        if matches:
            california_pub_nums.update(matches)
            break

# Load patents with citations
citations_path = locals()['var_functions.query_db:44']
with open(citations_path, 'r') as f:
    patents_with_citations = json.load(f)

# Find patents that cite California patents with a better matching strategy
citing_patents = []
university_pattern = re.compile(r'UNIV CALIFORNIA|UNIVERSITY OF CALIFORNIA', re.IGNORECASE)

for i, patent in enumerate(patents_with_citations):
    if i >= 500:  # Limit to first 500 for testing
        break
        
    patent_info = patent['Patents_info']
    
    # Skip patents that are assigned to UNIV CALIFORNIA themselves
    if university_pattern.search(patent_info):
        continue
    
    # Parse citations
    try:
        if isinstance(patent['citation'], str):
            citations = json.loads(patent['citation'])
        else:
            citations = patent['citation']
    except:
        citations = []
    
    # Check each citation
    cited_ca_pubs = []
    for citation in citations:
        if isinstance(citation, dict) and 'publication_number' in citation:
            pub_num = citation['publication_number']
            if pub_num in california_pub_nums:
                cited_ca_pubs.append(pub_num)
    
    if cited_ca_pubs:
        citing_patents.append({
            'patent_info': patent_info,
            'cited_ca_pubs': cited_ca_pubs,
            'cpc': patent.get('cpc', [])
        })

# Now let's find some actual matches by checking more patents
print('__RESULT__:')
print(json.dumps({
    'citing_patents_found': len(citing_patents),
    'total_patents_searched': min(500, len(patents_with_citations)),
    'sample_citing': citing_patents[:3] if citing_patents else 'No matches found',
    'ca_pub_nums_count': len(california_pub_nums)
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_california_patents': 169, 'sample_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ', 'sample_cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "'}, 'var_functions.query_db:20': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.execute_python:22': {'total_california_patents': 169, 'extracted_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_california_patents': 169, 'extracted_publication_numbers_count': 114, 'sample_pub_nums': ['US-2017145219-A1', 'WO-2018026404-A3', 'US-11421276-B2', 'US-2019169580-A1', 'CN-101584047-A', 'US-2019328740-A1', 'CA-2283629-C', 'AU-2007297661-A1', 'US-2023279470-A1', 'WO-2023212447-A2']}, 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'patents_with_citations': 5, 'california_pub_nums': 114, 'sample_patent_citation': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, 'var_functions.query_db:34': [], 'var_functions.execute_python:36': {'sample_citation_full': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H0737617-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9744842-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H09330720-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H10294100-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H10302768-A",\n    "type": ""\n  },\n  {\n    "application_n'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'total_ca_patents': 169, 'unique_pub_nums': 114, 'sample_pub_nums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C']}, 'var_functions.execute_python:42': {'total_ca_patents': 169, 'total_unique_pub_nums': 114, 'sample_pub_nums': ['US-2020025859-A1', 'US-2021000566-A1', 'US-2021181673-A1', 'US-12025581-B2', 'WO-2024112568-A1', 'CA-3161617-A1', 'US-2019328740-A1', 'KR-20050085437-A', 'US-6750960-B2', 'US-11421276-B2'], 'total_to_search': 114}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'california_pub_nums_count': 114, 'sample_pub_nums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2'], 'message': 'Ready to search for citing patents'}, 'var_functions.execute_python:48': {'patents_with_citations_in_sample': 1000, 'citing_patents_count': 0, 'unique_citing_assignees': 0, 'sample_assignees': [], 'sample_citing_patent': 'None'}, 'var_functions.execute_python:50': {'total_citing_assignees': 0, 'total_ca_publications': 114, 'sample_assignees': [], 'sample_ca_cpc_mapping': {'US-2022074631-A1': ['F25B21/00', 'F25B21/00', 'F25B21/00'], 'TW-201925402-A': ['C09J9/02', 'C09J9/02', 'C09J9/02'], 'US-11421276-B2': ['C12Q1/6883', 'C12Q1/6883', 'C12Q1/6883'], 'AU-2019275518-B2': ['A61K31/34', 'A61K31/351', 'A61K31/351', 'A61K31/357', 'A61K31/025'], 'JP-S6163700-A': ['C07K16/34', 'C07K16/34']}}}

exec(code, env_args)
