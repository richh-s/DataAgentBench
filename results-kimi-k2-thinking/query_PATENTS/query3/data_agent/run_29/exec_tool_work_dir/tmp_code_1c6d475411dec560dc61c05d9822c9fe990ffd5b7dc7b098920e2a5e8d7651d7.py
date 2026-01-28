code = """import json
import re
from collections import defaultdict

# Load UC patent publication numbers
uc_patents_path = locals()['var_functions.query_db:4']
with open(uc_patents_path, 'r') as f:
    uc_patents = json.load(f)

uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.add(pub_num)

# Load non-UC patents (patents that might cite UC patents)
non_uc_patents_path = locals()['var_functions.query_db:20']
with open(non_uc_patents_path, 'r') as f:
    non_uc_patents = json.load(f)

# Find patents that cite UC patents
citing_patents = []
uc_citations_map = defaultdict(set)  # maps UC patent to list of citing patents

for patent in non_uc_patents:
    patents_info = patent['Patents_info']
    citation_data = patent['citation']
    
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data)
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                if cited_pub and cited_pub in uc_pub_numbers:
                    # This patent cites a UC patent
                    citing_patents.append({
                        'patent_info': patents_info,
                        'citation': citation_data,
                        'cited_uc_patent': cited_pub
                    })
                    uc_citations_map[cited_pub].add(patents_info)
        except:
            continue

print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_pub_numbers),
    'citing_patents_found': len(citing_patents),
    'uc_patents_cited': len(uc_citations_map),
    'sample_citations': citing_patents[:5] if citing_patents else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': [], 'TW-201925402-A': []}}, 'var_functions.execute_python:12': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': ['Y02B30', 'F25B21', 'F25B2321', 'F28D15'], 'TW-201925402-A': ['C09D11', 'B82Y30', 'C09J2463', 'C09J9', 'B82Y40', 'C08K7', 'C08K2201', 'C08K3', 'C09J11', 'C08K2003'], 'US-11421276-B2': ['C12Q1', 'Y02A50', 'C12Q2600']}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'uc_patent_count': 114, 'sample_uc_patents': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.execute_python:18': {'uc_patent_count': 114, 'sample_uc_cpc': {'US-2022074631-A1': ['F25B21', 'F28D15', 'Y02B30', 'F25B2321'], 'TW-201925402-A': ['C08K2201', 'C09J2463', 'C08K2003', 'B82Y30', 'C08K7'], 'US-11421276-B2': ['C12Q2600', 'C12Q1', 'Y02A50']}}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'uc_patent_count': 114, 'sample_uc_patents': ['IL-274176-A', 'WO-2024044766-A3', 'US-2021002329-A1', 'EP-1212462-A1', 'US-2019169580-A1', 'US-2022018060-A1', 'WO-2020055916-A9', 'US-2018243924-A1', 'CN-101584047-A', 'US-5547866-A']}, 'var_functions.execute_python:24': {'uc_patent_count': 114, 'message': 'Ready to search for citations'}}

exec(code, env_args)
