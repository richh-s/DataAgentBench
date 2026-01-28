code = """import json
import re

# Load UC patent data
uc_patents_path = locals()['var_functions.query_db:4']
with open(uc_patents_path, 'r') as f:
    uc_patents = json.load(f)

# Extract UC patent publication numbers
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.append(pub_num)

# Create a comma-separated list for SQL IN clause (just for checking count)
# We'll use this in multiple queries
uc_patents_list = "','".join(uc_pub_numbers[:100])  # Limit to avoid too long query

# We'll need to query in batches due to potential size
print('__RESULT__:')
print(json.dumps({
    'uc_patent_count': len(uc_pub_numbers),
    'sample_uc_patents': uc_pub_numbers[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': [], 'TW-201925402-A': []}}, 'var_functions.execute_python:12': {'uc_patent_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'sample_cpc_map': {'US-2022074631-A1': ['Y02B30', 'F25B21', 'F25B2321', 'F28D15'], 'TW-201925402-A': ['C09D11', 'B82Y30', 'C09J2463', 'C09J9', 'B82Y40', 'C08K7', 'C08K2201', 'C08K3', 'C09J11', 'C08K2003'], 'US-11421276-B2': ['C12Q1', 'Y02A50', 'C12Q2600']}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
