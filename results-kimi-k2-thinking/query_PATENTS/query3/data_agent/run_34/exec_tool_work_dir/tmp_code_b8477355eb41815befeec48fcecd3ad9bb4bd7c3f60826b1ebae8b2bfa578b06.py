code = """import json
import re

print('Reading data...')

# Read UC patents data (citing patents assigned to UNIV CALIFORNIA)
uc_path = locals()['var_functions.query_db:16']
with open(uc_path, 'r') as f:
    uc_patents = json.load(f)

# Extract UC patent publication numbers and their CPC codes
uc_patents_dict = {}  # key: pub number, value: CPC codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    
    # Extract publication number using regex patterns
    pub_match = re.search(r'pub[^\w]*number[^\w]*([A-Z]{2}-[^-]+-[A-Z][0-9])', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        
        # Extract CPC codes
        try:
            cpc_data = json.loads(patent['cpc'])
            cpc_codes = [cpc['code'] for cpc in cpc_data if 'code' in cpc]
            uc_patents_dict[pub_num] = cpc_codes
        except:
            uc_patents_dict[pub_num] = []

print('UC patents extracted: ' + str(len(uc_patents_dict)))
print('Sample UC patents: ' + str(list(uc_patents_dict.keys())[:5]))

result = {
    'uc_patents_count': len(uc_patents_dict),
    'sample': {k: uc_patents_dict[k][:3] for k in list(uc_patents_dict)[:3]}
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'total': '169'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'status': 'success', 'count': 87}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'uc_patents_count': 87, 'uc_pub_numbers_count': 26, 'uc_pub_numbers': ['WO-2021102420-A1', 'US-11546022-B2', 'US-6767662-B2', 'US-6750960-B2', 'US-2006292670-A1', 'WO-2018026404-A3', 'AU-2019275518-B2', 'WO-2024112568-A1', 'US-2022074631-A1', 'WO-2012162563-A2', 'WO-2024044766-A3', 'WO-2023225482-A3', 'WO-2017214343-A1', 'US-2018243924-A1', 'US-2017145219-A1', 'US-11376346-B2', 'US-2017281687-A1', 'EP-0826155-A4', 'US-2006051790-A1', 'AU-2010214112-B2', 'EP-1212462-A1', 'US-9061071-B2', 'WO-2010045542-A3', 'US-11667770-B2', 'AU-2015364602-B2', 'US-2019328740-A1'], 'uc_cpc_sample': {'US-2022074631-A1': ['Y02B30/00', 'F25B2321/001', 'F25B21/00', 'F28D15/00', 'F25B21/00', 'F25B2321/001', 'F25B2321/001', 'F28D15/00', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/08', 'A61D7/04', 'A61K31/025', 'A61K31/357', 'A61P43/00', 'A61P25/20', 'A61K31/045', 'A61K31/02', 'A61P23/00', 'A61K9/007', 'A61K31/341', 'A61M16/01', 'A61D7/04', 'A61K31/351', 'A61K31/351', 'A61K31/34', 'A61K31/08', 'A61K31/025', 'A61P43/00', 'A61K31/02', 'A61K31/045', 'A61P11/00', 'A61K31/357', 'A61P23/00', 'A61P25/20', 'A61M16/01', 'A61K31/357', 'A61P11/00', 'A61K9/007', 'A61K31/025', 'A61K31/015', 'A61K31/341', 'A61K31/025', 'A61K31/045', 'A61K31/341', 'A61K31/351', 'A61K31/357', 'A61K31/08', 'A61K9/007', 'A61P23/00', 'A61K31/34', 'A61K31/015'], 'US-2017281687-A1': ['A61K31/52', 'A61K2035/124', 'A61K31/522', 'A61K35/28', 'A61K35/28', 'A61K31/522', 'C12N2510/00', 'A61K2035/124', 'A61K31/52', 'A61K2035/124', 'A61K35/28']}}, 'var_functions.query_db:34': [{'count': '277644'}]}

exec(code, env_args)
