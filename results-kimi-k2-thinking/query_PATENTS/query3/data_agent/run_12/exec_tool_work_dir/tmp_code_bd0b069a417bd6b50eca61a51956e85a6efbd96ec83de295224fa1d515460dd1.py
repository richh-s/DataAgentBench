code = """import json
import re

# Total database size: 277,813 records
# Let's load a larger sample to find UC citations
all_patents_file = 'file_storage/functions.query_db:54.json'
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Load UC publication numbers
uc_file = 'file_storage/functions.query_db:36.json'
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

# Create set of UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'(?:pub|publication)(?:\s+number)?\s+([A-Z]{2}-[\dA-Z-]+)', patents_info)
    if pub_match:
        uc_pub_numbers.add(pub_match.group(1))

# Find patents that cite UC patents
citing_patents = []
for patent in all_patents:
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        continue
    
    if not patent['citation'] or patent['citation'] == '[]':
        continue
    
    try:
        citations = json.loads(patent['citation'])
        for citation in citations:
            pub_num = citation.get('publication_number', '')
            if pub_num in uc_pub_numbers:
                citing_patents.append({
                    'patents_info': patent['Patents_info'],
                    'cpc_codes': json.loads(patent['cpc']) if patent['cpc'] else [],
                    'uc_patent_cited': pub_num
                })
                break
    except:
        continue

result = {
    'all_patents_checked': len(all_patents),
    'uc_pub_numbers': len(uc_pub_numbers),
    'citing_patents_found': len(citing_patents),
    'sample_citing': citing_patents[:3] if citing_patents else []
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'name': 'publicationinfo'}], 'var_functions.execute_python:10': 'File path: file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': [{'index': 0, 'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ...', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "...'}, {'index': 1, 'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation': '[]...', 'cpc': '[\n  {\n    "code": "C09J11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08K3/08",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"...'}, {'index': 2, 'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2001053519-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",...', 'cpc': '[\n  {\n    "code": "Y02A50/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code...'}, {'index': 3, 'patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "ABU-AWWAD, F. M. \\"A QSAR STUDY of the Activity of Some Fluorinated Anesthetics\\" Der Pharma Chemica (...', 'cpc': '[\n  {\n    "code": "A61K31/357",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K31/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"...'}, {'index': 4, 'patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'citation': '[]...', 'cpc': '[\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "cod...'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': 'Total UC patents: 169', 'var_functions.execute_python:20': {'total_uc_patents': 169, 'extracted_pub_numbers': 55, 'sample_pub_numbers': ['US-11421276-B2', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'US-2019169580-A1', 'US-2020283856-A1'], 'sample_records': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   ', 'cpc_codes': [{'code': 'Y02B30/00', 'first': False, 'inventive': False, 'tree': []}, {'code': 'F25B2321/001', 'first': False, 'inventive': False, 'tree': []}]}, {'patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_preview': '[]', 'cpc_codes': [{'code': 'C09J11/04', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C08K3/08', 'first': False, 'inventive': False, 'tree': []}]}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2001053519-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",', 'cpc_codes': [{'code': 'Y02A50/30', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C12Q1/6883', 'first': True, 'inventive': True, 'tree': []}]}]}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 55, 'sample_uc_pub_numbers': ['US-2020283856-A1', 'CN-101584047-A', 'US-2021002329-A1', 'AU-2005269556-A1', 'US-2017087258-A1', 'US-2021181673-A1', 'AU-2898989-A', 'US-2003112494-A1', 'AU-2004253879-A1', 'KR-20050085437-A']}, 'var_functions.query_db:26': [{'total': '277813'}], 'var_functions.execute_python:30': {'uc_patents_count': 169, 'uc_pub_numbers_count': 55, 'first_few_pub_numbers': ['AU-2017356943-A1', 'AU-2898989-A', 'EP-2210307-A4', 'WO-2014152660-A1', 'WO-2018067976-A1', 'US-11421276-B2', 'PE-20130764-A1', 'EP-3668487-A4', 'PT-2970346-T', 'US-2020283856-A1']}, 'var_functions.query_db:32': [], 'var_functions.execute_python:34': {'uc_pub_numbers_count': 55, 'sample_numbers': ['CN-101584047-A', 'EP-3668487-A4', 'AU-5938296-A', 'US-11421276-B2', 'US-7052856-B2']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents_loaded': 169, 'unique_uc_pub_numbers': 55, 'sample_uc_pub_numbers': ['WO-2019173834-A1', 'US-2017087258-A1', 'US-2003112494-A1', 'US-6237292-B1', 'EP-3668487-A4', 'KR-20050085437-A', 'AU-2409401-A', 'US-2004115131-A1', 'JP-2009260386-A', 'US-11421276-B2']}, 'var_functions.query_db:40': [], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 169, 'uc_pub_numbers': 55, 'sample_numbers': ['US-2003112494-A1', 'AU-2005269556-A1', 'AU-3353000-A', 'AU-2898989-A', 'US-2021181673-A1']}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patents_count': 169, 'uc_pub_numbers_count': 55, 'sample_mapping': {'US-11421276-B2': ['Y02A50/30', 'C12Q1/6883', 'C12Q1/6883', 'C12Q2600/136', 'C12Q2600/158', 'C12Q2600/112', 'C12Q2600/158', 'C12Q2600/112', 'C12Q2600/118', 'C12Q2600/136', 'C12Q1/6883', 'C12Q2600/136', 'C12Q2600/112', 'C12Q2600/158', 'C12Q2600/118'], 'AU-2003247814-A1': ['A61H2205/106', 'A61H2205/10', 'A61H9/005', 'A61H2205/106', 'A61H2205/10', 'A61H9/005'], 'AU-2017356943-A1': ['C07C253/34', 'C07C253/30', 'C07C253/30', 'C07B59/001', 'C07C255/34', 'C07B59/001', 'C07B2200/05', 'C07C253/34']}}, 'var_functions.execute_python:52': {'total_patents_checked': 500, 'uc_citations_found': 0, 'uc_pub_numbers_being_cited': 55, 'sample_citations': []}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:58': {'total_uc_patents': 169, 'uc_pub_numbers_found': 55, 'sample_pub_numbers': ['US-11421276-B2', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'US-2019169580-A1', 'US-2020283856-A1'], 'sample_citations': [{'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US', 'citation_sample': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}, {'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publica', 'citation_sample': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2001053519-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}]}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': [{'total': '277813'}]}

exec(code, env_args)
