code = """import json
import re
from collections import defaultdict

# Load the full list of citing patents
citing_patents_path = locals()['var_functions.query_db:26']
with open(citing_patents_path, 'r') as f:
    citing_patents_data = json.load(f)

# Process the citing patents to extract assignees and UC patents cited
citing_assignees = {}
uc_to_citing_map = defaultdict(list)  # maps UC patent to citing patents

for item in citing_patents_data['sample_citations']:
    patent_info = item['patent_info']
    cited_uc = item['cited_uc_patent']
    
    # Extract assignee name from Patents_info
    # Look for pattern like "assigned to ASSIGNEE_NAME" or "owned by ASSIGNEE_NAME"
    assignee_match = re.search(r'(?:assigned to|owned by|held by|is owned by)\s+([^\s][^.]+)', patent_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()
        # Exclude UNIV CALIFORNIA
        if 'UNIV CALIFORNIA' not in assignee:
            citing_assignees[assignee] = patent_info
    
    uc_to_citing_map[cited_uc].append(patent_info)

# Load UC CPC data to get subclass codes
uc_patents_path = locals()['var_functions.query_db:4']
with open(uc_patents_path, 'r') as f:
    uc_patents = json.load(f)

uc_cpc_map = {}  # maps UC patent pub number to CPC subclass codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc_data = patent['cpc']
    
    # Extract publication number 
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        
        # Parse CPC codes and extract subclasses 
        cpc_codes = set()
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract subclass group (e.g., Y02B30, F25B21)
                        # Take everything up to the first slash or space
                        clean_code = code.split('/')[0].split()[0]
                        cpc_codes.add(clean_code)
            except:
                pass
        
        uc_cpc_map[pub_num] = list(set(cpc_codes))

print('__RESULT__:')
print(json.dumps({
    'citing_assignees': list(citing_assignees.keys()),
    'uc_patents_cited': list(uc_to_citing_map.keys()),
    'assignee_count': len(citing_assignees),
    'sample_uc_cpc': {k: uc_cpc_map.get(k, []) for k in list(uc_to_citing_map.keys())}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': [], 'TW-201925402-A': []}}, 'var_functions.execute_python:12': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': ['Y02B30', 'F25B21', 'F25B2321', 'F28D15'], 'TW-201925402-A': ['C09D11', 'B82Y30', 'C09J2463', 'C09J9', 'B82Y40', 'C08K7', 'C08K2201', 'C08K3', 'C09J11', 'C08K2003'], 'US-11421276-B2': ['C12Q1', 'Y02A50', 'C12Q2600']}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'uc_patent_count': 114, 'sample_uc_patents': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.execute_python:18': {'uc_patent_count': 114, 'sample_uc_cpc': {'US-2022074631-A1': ['F25B21', 'F28D15', 'Y02B30', 'F25B2321'], 'TW-201925402-A': ['C08K2201', 'C09J2463', 'C08K2003', 'B82Y30', 'C08K7'], 'US-11421276-B2': ['C12Q2600', 'C12Q1', 'Y02A50']}}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'uc_patent_count': 114, 'sample_uc_patents': ['IL-274176-A', 'WO-2024044766-A3', 'US-2021002329-A1', 'EP-1212462-A1', 'US-2019169580-A1', 'US-2022018060-A1', 'WO-2020055916-A9', 'US-2018243924-A1', 'CN-101584047-A', 'US-5547866-A']}, 'var_functions.execute_python:24': {'uc_patent_count': 114, 'message': 'Ready to search for citations'}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json'}

exec(code, env_args)
