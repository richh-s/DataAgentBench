code = """import json
import re

# Load the UNIV CALIFORNIA patents
result_file = locals()['var_functions.query_db:20']
with open(result_file, 'r') as f:
    ucs_patents = json.load(f)

# Extract UNIV CALIFORNIA publication numbers and their CPC codes
uc_pub_numbers = []
uc_cpc_map = {}  # publication_number -> list of CPC codes

for patent in ucs_patents:
    patents_info = patent.get('Patents_info', '')
    
    if 'UNIV CALIFORNIA' in patents_info.upper():
        # Extract publication number
        pub_match = re.search(r'(?:pub\. number|publication number|number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
        if pub_match:
            pub_num = pub_match.group(1)
            uc_pub_numbers.append(pub_num)
            
            # Extract CPC codes for this patent
            cpc_codes = []
            cpc_data = patent.get('cpc', '[]')
            if cpc_data:
                try:
                    cpc_list = json.loads(cpc_data)
                    for cpc_item in cpc_list:
                        if 'code' in cpc_item:
                            cpc_codes.append(cpc_item['code'])
                except:
                    pass
            
            uc_cpc_map[pub_num] = cpc_codes

print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA patents")
print(f"Sample UC patents: {uc_pub_numbers[:5]}")

result_summary = {
    'total_uc_patents': len(uc_pub_numbers),
    'uc_pub_numbers': uc_pub_numbers,
    'sample_cpc_map': {k: uc_cpc_map[k] for k in list(uc_cpc_map.keys())[:3]}
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_uc_patents': 8, 'sample_pub_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'patents_with_citations': 5}, 'var_functions.execute_python:16': {'/tmp': [], '/tmp/patent_dbs': 'access error', '/': ['root', 'tmp', 'lib', 'run', 'srv', 'lib64', 'usr', 'sys', 'sbin', 'opt']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
