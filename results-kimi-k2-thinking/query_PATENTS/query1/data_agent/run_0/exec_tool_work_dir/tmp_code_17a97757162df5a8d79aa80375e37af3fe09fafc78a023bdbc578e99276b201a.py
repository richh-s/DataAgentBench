code = """import json
import os

# Get the file path for the results
storage_key = 'var_functions.execute_python:32'
file_path = locals().get(storage_key, None)

if file_path is None:
    result = {'error': 'File path not accessible'}
else:
    # Read the full results
    with open(file_path, 'r') as f:
        full_result = json.load(f)
    
    # Extract CPC codes that have their best year as 2022
    cpc_codes = full_result.get('cpc_codes_best_2022', [])
    
    result = {
        'count': len(cpc_codes),
        'sample_codes': cpc_codes[:20]  # First 20 codes
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'total': '277813'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': {'total_publications': 277813, 'extracted_pairs': 103409, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'H01M10/0566', 'year': 2021}, {'cpc_code': 'H01M10/052', 'year': 2021}, {'cpc_code': 'C01P2002/76', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}, {'cpc_code': 'Y02E60/10', 'year': 2021}]}, 'var_functions.query_db:26': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_functions.query_db:28': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01B1/022', 'level': '9.0'}, {'symbol': 'A01B1/024', 'level': '9.0'}, {'symbol': 'A01B1/026', 'level': '9.0'}, {'symbol': 'A01B1/028', 'level': '9.0'}, {'symbol': 'A01B1/04', 'level': '9.0'}, {'symbol': 'A01B1/06', 'level': '8.0'}, {'symbol': 'A01B1/065', 'level': '9.0'}, {'symbol': 'A01B1/08', 'level': '9.0'}], 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json'}

exec(code, env_args)
