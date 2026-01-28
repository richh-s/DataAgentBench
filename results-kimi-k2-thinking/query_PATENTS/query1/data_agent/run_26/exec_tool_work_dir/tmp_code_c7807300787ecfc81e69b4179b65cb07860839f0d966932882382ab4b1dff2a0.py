code = """import json
import pandas as pd
import numpy as np

# Read the publication data
pub_data_path = locals().get('var_functions.query_db:5')
if pub_data_path:
    with open(pub_data_path, 'r') as f:
        pub_data = json.load(f)
else:
    pub_data = locals().get('var_functions.query_db:5', [])

# Read the CPC level 5 data
cpc_data_path = locals().get('var_functions.query_db:14')
if cpc_data_path:
    with open(cpc_data_path, 'r') as f:
        cpc_level5_data = json.load(f)
else:
    cpc_level5_data = locals().get('var_functions.query_db:14', [])

# Get all level 5 CPC groups
cpc_level5_groups = set()
for item in cpc_level5_data:
    symbol = item.get('symbol', '')
    if len(symbol) == 4:  # CPC groups at level 5 have 4 characters
        cpc_level5_groups.add(symbol)

# Parse CPC codes and extract year from publication_date
cpc_year_counts = {}

for record in pub_data:
    cpc_json = record.get('cpc', '[]')
    pub_date = record.get('publication_date', '')
    
    try:
        cpc_list = json.loads(cpc_json) if isinstance(cpc_json, str) else cpc_json
    except:
        continue
    
    # Extract year from publication date
    if pub_date:
        parts = pub_date.split()[-1]
        try:
            year = int(parts)
        except:
            continue
        
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                full_cpc_code = cpc_item['code']
                # Extract level 5 group code (first 4 characters)
                if len(full_cpc_code) >= 4:
                    group_code = full_cpc_code[:4]
                    # Only count if it's a valid level 5 CPC group
                    if group_code in cpc_level5_groups:
                        key = (group_code, year)
                        cpc_year_counts[key] = cpc_year_counts.get(key, 0) + 1

print('__RESULT__:')
print(json.dumps({
    'total_cpc_level5_groups': len(cpc_level5_groups),
    'sample_level5_groups': list(cpc_level5_groups)[:10],
    'total_records': len(cpc_year_counts),
    'sample_counts': dict(list(cpc_year_counts.items())[:10])
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:6': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'H01M10/0566', 'year': 2021}, {'cpc_code': 'H01M10/052', 'year': 2021}, {'cpc_code': 'C01P2002/76', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'Y02E60/10', 'year': 2021}, {'cpc_code': 'C01P2002/76', 'year': 2021}, {'cpc_code': 'H01M10/0525', 'year': 2021}, {'cpc_code': 'H01M2004/028', 'year': 2021}, {'cpc_code': 'H01M4/1315', 'year': 2021}, {'cpc_code': 'H01M2004/021', 'year': 2021}, {'cpc_code': 'H01M4/525', 'year': 2021}, {'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'H01M4/1315', 'year': 2021}, {'cpc_code': 'H01M4/525', 'year': 2021}, {'cpc_code': 'H01M4/505', 'year': 2021}, {'cpc_code': 'H01M4/505', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0525', 'year': 2021}, {'cpc_code': 'H01M4/582', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M4/525', 'year': 2021}, {'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01P2002/76', 'year': 2021}, {'cpc_code': 'H01M4/1315', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'H01M2004/028', 'year': 2021}, {'cpc_code': 'H01M4/505', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M2004/021', 'year': 2021}, {'cpc_code': 'H01M10/0525', 'year': 2021}, {'cpc_code': 'H01M10/0566', 'year': 2021}, {'cpc_code': 'H01M10/052', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'F16H47/04', 'year': 2020}, {'cpc_code': 'F16H37/08', 'year': 2020}, {'cpc_code': 'F16H47/04', 'year': 2020}, {'cpc_code': 'F16H47/04', 'year': 2020}, {'cpc_code': 'F16H2037/0893', 'year': 2020}, {'cpc_code': 'F16H2200/2007', 'year': 2020}, {'cpc_code': 'F16H37/084', 'year': 2020}, {'cpc_code': 'F16H2200/0043', 'year': 2020}, {'cpc_code': 'F16H2037/0873', 'year': 2020}, {'cpc_code': 'F16H2200/2041', 'year': 2020}, {'cpc_code': 'F16H2037/0886', 'year': 2020}, {'cpc_code': 'F16H3/62', 'year': 2020}, {'cpc_code': 'F16H37/084', 'year': 2020}, {'cpc_code': 'F16H3/76', 'year': 2020}, {'cpc_code': 'F16H2037/0873', 'year': 2020}, {'cpc_code': 'F16H2037/0873', 'year': 2020}, {'cpc_code': 'F16H2200/2007', 'year': 2020}, {'cpc_code': 'F16H3/62', 'year': 2020}, {'cpc_code': 'F16H47/04', 'year': 2020}, {'cpc_code': 'F16H37/084', 'year': 2020}, {'cpc_code': 'F16H2200/0043', 'year': 2020}, {'cpc_code': 'F16H2200/2041', 'year': 2020}, {'cpc_code': 'B29C70/48', 'year': 2021}, {'cpc_code': 'C08J5/246', 'year': 2021}, {'cpc_code': 'C08J5/244', 'year': 2021}, {'cpc_code': 'C08J5/246', 'year': 2021}, {'cpc_code': 'C08J5/244', 'year': 2021}, {'cpc_code': 'B32B15/14', 'year': 2021}, {'cpc_code': 'B32B2262/101', 'year': 2021}, {'cpc_code': 'C09D175/08', 'year': 2021}, {'cpc_code': 'B29L2031/3017', 'year': 2021}, {'cpc_code': 'B32B27/08', 'year': 2021}, {'cpc_code': 'C08G18/3206', 'year': 2021}, {'cpc_code': 'B32B27/34', 'year': 2021}, {'cpc_code': 'B29C70/86', 'year': 2021}, {'cpc_code': 'B32B2260/021', 'year': 2021}, {'cpc_code': 'B32B29/002', 'year': 2021}, {'cpc_code': 'B29K2075/00', 'year': 2021}, {'cpc_code': 'B32B2605/08', 'year': 2021}, {'cpc_code': 'B32B2260/046', 'year': 2021}, {'cpc_code': 'B32B2255/02', 'year': 2021}, {'cpc_code': 'B32B2255/26', 'year': 2021}, {'cpc_code': 'B32B27/10', 'year': 2021}, {'cpc_code': 'B32B15/20', 'year': 2021}, {'cpc_code': 'B32B15/095', 'year': 2021}, {'cpc_code': 'B32B27/32', 'year': 2021}, {'cpc_code': 'B32B2605/003', 'year': 2021}, {'cpc_code': 'B32B5/022', 'year': 2021}, {'cpc_code': 'B32B2255/10', 'year': 2021}, {'cpc_code': 'B32B2262/065', 'year': 2021}, {'cpc_code': 'C08J2375/04', 'year': 2021}, {'cpc_code': 'B32B2307/50', 'year': 2021}, {'cpc_code': 'B32B15/08', 'year': 2021}, {'cpc_code': 'B32B5/026', 'year': 2021}, {'cpc_code': 'C08G18/4829', 'year': 2021}, {'cpc_code': 'B32B3/12', 'year': 2021}, {'cpc_code': 'B32B2262/106', 'year': 2021}, {'cpc_code': 'B32B29/08', 'year': 2021}, {'cpc_code': 'B32B29/02', 'year': 2021}, {'cpc_code': 'B32B2262/0269', 'year': 2021}, {'cpc_code': 'B32B2262/101', 'year': 2021}, {'cpc_code': 'C08G18/7671', 'year': 2021}], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:10': {'total_records': 2141569, 'sample_data': [{'cpc_group': 'C01B', 'year': 2021}, {'cpc_group': 'C01B', 'year': 2021}, {'cpc_group': 'H01M', 'year': 2021}, {'cpc_group': 'H01M', 'year': 2021}, {'cpc_group': 'C01G', 'year': 2021}, {'cpc_group': 'H01M', 'year': 2021}, {'cpc_group': 'H01M', 'year': 2021}, {'cpc_group': 'C01P', 'year': 2021}, {'cpc_group': 'C01G', 'year': 2021}, {'cpc_group': 'Y02E', 'year': 2021}], 'year_range': {'min': 1837, 'max': 2024}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
