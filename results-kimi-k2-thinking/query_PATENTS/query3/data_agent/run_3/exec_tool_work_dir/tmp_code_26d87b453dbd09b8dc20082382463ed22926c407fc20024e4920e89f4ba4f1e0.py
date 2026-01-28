code = """import json
import re

# Load all patents that are NOT assigned to UNIV CALIFORNIA
other_file = locals().get('var_functions.query_db:32', '')
with open(other_file, 'r') as f:
    other_patents = json.load(f)

# Load all UNIV CALIFORNIA patents
uc_file = locals().get('var_functions.query_db:5', '')
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

# Extract UC publication numbers from their patents
uc_pub_numbers = set()
uc_cpc_map = {}  # Map UC patent number to its CPC codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    
    # Extract UC publication numbers
    pattern = r'([A-Z]{2}-\d+[A-Z]?-\d+[A-Z]\d*)\.?\b'
    matches = re.findall(pattern, patents_info)
    uc_pub_numbers.update(matches)
    
    # Store CPC codes for each UC patent
    for match in matches:
        uc_cpc_map[match.rstrip('.')] = patent.get('cpc', '')

# Now find patents that cite UC patents and are not assigned to UC
citing_pairs = []

for patent in other_patents:
    patents_info = patent['Patents_info']
    citation = patent.get('citation', '')
    cpc = patent.get('cpc', '')
    
    if citation and citation != '[]':
        try:
            # Clean and parse citations
            citations = json.loads(citation.replace("'", '"').replace('\n', ''))
            
            for cite in citations:
                pub_number = cite.get('publication_number', '')
                if pub_number:
                    # Check if cited patent is a UC patent
                    if pub_number in uc_pub_numbers:
                        # Extract assignee - look at the beginning before verbs
                        assignee_match = re.search(r'^(.+?)\s+(holds|is owned by|holds the|is assigned to|owns)', patents_info)
                        if assignee_match:
                            assignee = assignee_match.group(1).strip()
                            # Exclude UNIV CALIFORNIA itself
                            if 'UNIV CALIFORNIA' not in assignee:
                                citing_pairs.append({
                                    'citing_assignee': assignee,
                                    'cited_uc_patent': pub_number,
                                    'uc_cpc_codes': uc_cpc_map.get(pub_number, ''),
                                    'citing_cpc_codes': cpc
                                })
        except Exception as e:
            # Skip parsing errors
            continue

print('__RESULT__:')
print(json.dumps({
    'uc_patents_found': len(uc_pub_numbers),
    'citing_assignees_found': len(citing_pairs),
    'sample_citations': citing_pairs[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 'Found 50 patents from UNIV CALIFORNIA', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_patents': 50, 'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:16': {'total_uc_patents': 50, 'uc_publication_numbers': ['AU-2005269556-A1.', 'US-2020283856-A1.', 'US-2017281687-A1.', 'KR-20050085437-A.', 'EP-0826155-A4.', 'CN-103189548-A.', 'US-2021002329-A1.', 'WO-2017136335-A1.', 'AU-2019275518-B2.', 'US-2022074631-A1.', 'PT-2970346-T.', 'KR-20160119166-A.', 'US-7745569-B2.', 'AU-2898989-A.', 'KR-20200041324-A.', 'US-2006051790-A1.', 'US-2017145219-A1.', 'US-6237292-B1.', 'WO-2012162563-A2.', 'US-9061071-B2.'], 'total_unique_pub_numbers': 36}, 'var_functions.list_db:18': ['cpc_definition'], 'var_functions.execute_python:20': 'Preparing to search for citing patents...', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_uc_patents': 50, 'uc_publication_numbers': [], 'count': 0}, 'var_functions.execute_python:26': {'total_uc_patents': 50, 'sample_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'extracted_pub_numbers': [], 'total_extracted': 0}, 'var_functions.execute_python:28': {'uc_publication_numbers': [], 'uc_count': 0, 'citing_pairs_found': 0, 'sample_pairs': []}, 'var_functions.execute_python:30': {'uc_patents_count': 50, 'uc_publication_numbers': ['AU-2001296493-A', 'AU-2001296493-B2', 'AU-2002254753-A', 'AU-2002254753-B2', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2008329628-A', 'AU-2008329628-B2', 'AU-2017356943-A', 'AU-2017356943-A1', 'AU-2019275518-A', 'AU-2019275518-B2', 'AU-2898989-A', 'CA-2298540-A', 'CA-2298540-A1', 'CN-100339724-C', 'CN-103189548-A', 'CN-200380105631-A', 'CN-201180052574-A', 'EP-00992018-A', 'EP-0826155-A4', 'EP-1224461-B1', 'EP-96907882-A', 'IL-140140-A0', 'IL-14014099-A', 'JP-13313985-A', 'JP-2004321293-A', 'JP-2005104983-A', 'KR-20050085437-A', 'KR-20057010360-A', 'KR-20160119166-A', 'KR-20167024476-A', 'KR-20180041236-A', 'KR-20187008669-A', 'KR-20200041324-A', 'KR-20200084864-A', 'KR-20207004898-A', 'KR-20207010098-A', 'PT-14764430-T', 'PT-2970346-T', 'RO-70061-A', 'RO-7944874-A', 'TW-107142982-A', 'TW-201925402-A', 'US-10765865-B2', 'US-10900049-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-17323505-A', 'US-2006051790-A1', 'US-2009031436-A1', 'US-2012039471-W', 'US-201313787160-A', 'US-201515313510-A', 'US-201515329526-A', 'US-2017015812-W', 'US-2017145219-A1', 'US-201715422925-A', 'US-201715625819-A', 'US-201715646074-A', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017369950-A1', 'US-201815950106-A', 'US-201816612511-A', 'US-2018304537-A1', 'US-2019021660-W', 'US-2019059638-W', 'US-201916277921-A', 'US-201916362297-A', 'US-201916401060-A', 'US-201916454755-A', 'US-201916537416-A', 'US-2019169580-A1', 'US-2020061827-W', 'US-202016878973-A', 'US-202016883515-A', 'US-202017021925-A', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-202117472182-A', 'US-2022074631-A1', 'US-39548599-A', 'US-55161904-A', 'US-6237292-B1', 'US-7745569-B2', 'US-8864206-A', 'US-9061071-B2', 'WO-2012162563-A2', 'WO-2017136335-A1', 'WO-2019173834-A1', 'WO-2020096950-A1', 'WO-2021102420-A1'], 'count': 98, 'sample_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
