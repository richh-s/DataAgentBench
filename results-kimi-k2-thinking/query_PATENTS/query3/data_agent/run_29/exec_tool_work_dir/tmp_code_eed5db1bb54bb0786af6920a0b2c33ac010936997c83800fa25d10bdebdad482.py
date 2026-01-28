code = """import json
import re

# Get all UC patent publication numbers and their CPC codes
uc_patents_path = locals()['var_functions.query_db:4']
with open(uc_patents_path, 'r') as f:
    uc_patents = json.load(f)

uc_pub_numbers = []
uc_cpc_map = {}  # maps UC pub number to CPC subclass codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc_data = patent['cpc']
    
    # Extract publication number from Patents_info
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.append(pub_num)
        
        # Parse CPC codes and extract subclasses (e.g., Y02B30, F25B21)
        cpc_codes = []
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract up to the slash (e.g., Y02B30/00 -> Y02B30)
                        slash_pos = code.find('/')
                        if slash_pos > 0:
                            cpc_codes.append(code[:slash_pos])
                        else:
                            cpc_codes.append(code)
            except:
                pass
        
        uc_cpc_map[pub_num] = list(set(cpc_codes))

print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_pub_numbers),
    'sample_pub_numbers': uc_pub_numbers[:10],
    'sample_cpc_map': {k: uc_cpc_map[k] for k in list(uc_cpc_map.keys())[:3]}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': [], 'TW-201925402-A': []}}}

exec(code, env_args)
