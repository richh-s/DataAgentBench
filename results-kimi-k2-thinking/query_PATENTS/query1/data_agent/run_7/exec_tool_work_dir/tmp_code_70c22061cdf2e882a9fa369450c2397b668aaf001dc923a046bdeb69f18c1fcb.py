code = """import json
import ast

# Read the CPC codes with best year 2022
file_path = locals()['var_functions.execute_python:21']
with open(file_path, 'r') as f:
    cpc_best_2022 = json.load(f)

print('Total CPC codes with best year 2022:', len(cpc_best_2022))
print('Sample codes:', cpc_best_2022[:10])

# Filter for level 5 CPC codes (format XXXXXX/XXXX where subgroup has 2+ digits)
level5_cpc_codes = []
for cpc in cpc_best_2022:
    if '/' in cpc:
        parts = cpc.split('/')
        main_group = parts[0]
        subgroup = parts[1] if len(parts) > 1 else ''
        
        # Level 5: subgroup should have at least 2 digits
        # and main_group should end with digits
        if (len(subgroup) >= 2 and 
            subgroup.isdigit() and 
            any(c.isdigit() for c in main_group)):
            level5_cpc_codes.append(cpc)

print('Level 5 CPC codes with best year 2022:', len(level5_cpc_codes))
print('Sample level 5 codes:', level5_cpc_codes[:20])

# Return the filtered list
print('__RESULT__:')
print(json.dumps(level5_cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_cpc_codes': 143452, 'cpc_best_year_2022_count': 12036, 'level5_cpc_best_year_2022_count': 12036, 'sample_level5_cpc_2022': ['C01P2002/76', 'H01M10/0525', 'F16H2200/2007', 'F16H2200/2041', 'B29C70/48', 'C09D175/08', 'B32B27/34', 'B32B2260/021', 'B32B2307/50', 'B32B27/302']}, 'var_functions.execute_python:21': 'file_storage/functions.execute_python:21.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': [{'symbol': 'H01M10/0525', 'level': '10.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': []}

exec(code, env_args)
