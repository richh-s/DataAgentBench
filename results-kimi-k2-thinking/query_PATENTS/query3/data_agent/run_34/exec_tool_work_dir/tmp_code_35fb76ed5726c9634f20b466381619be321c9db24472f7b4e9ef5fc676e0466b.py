code = """import json
import re

# Read UC patents data
uc_path = locals()['var_functions.query_db:16']
with open(uc_path, 'r') as f:
    uc_patents = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
uc_cpc_map = {}  # Map UC pub number to its CPC codes

for patent in uc_patents:
    # Extract publication number from Patents_info
    info = patent['Patents_info']
    pub_match = re.search(r'pub\. number\s+([A-Z]{2}-[^-]+-[A-Z][0-9])', info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.add(pub_num)
        
        # Extract CPC codes
        try:
            cpc_data = json.loads(patent['cpc'])
            cpc_codes = [cpc['code'] for cpc in cpc_data if 'code' in cpc]
            uc_cpc_map[pub_num] = cpc_codes
        except:
            uc_cpc_map[pub_num] = []

print('UC patents count: ' + str(len(uc_patents)))
print('UC publication numbers count: ' + str(len(uc_pub_numbers)))
print('Sample UC pub numbers: ' + str(list(uc_pub_numbers)[:5]))

result = {
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'uc_pub_numbers': list(uc_pub_numbers),
    'uc_cpc_sample': {k: uc_cpc_map[k] for k in list(uc_cpc_map)[:3]}
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'total': '169'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'status': 'success', 'count': 87}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
