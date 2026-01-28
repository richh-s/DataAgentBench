code = """import json
import re
from collections import defaultdict

# Direct access to variables - no file reading needed
uc_patents = var_functions.query_db:44
all_patents = var_functions.query_db:36

# If loading fails, try alternative variable names
if not uc_patents or len(uc_patents) == 0:
    uc_patents = locals().get('var_functions.query_db:8', [])
if not all_patents or len(all_patents) == 0:
    all_patents = locals().get('var_functions.query_db:34', [])

print(f"UC patents type: {type(uc_patents)}, count: {len(uc_patents) if hasattr(uc_patents, '__len__') else 0}")
print(f"All patents type: {type(all_patents)}, count: {len(all_patents) if hasattr(all_patents, '__len__') else 0}")

# Ensure we have data
if not uc_patents or not all_patents:
    # Try to get them as direct variables
    for key, value in locals().items():
        if 'query_db' in key and '44' in key:
            uc_patents = value
        if 'query_db' in key and ('36' in key or '34' in key):
            all_patents = value

print(f"After check - UC: {len(uc_patents) if uc_patents else 0}, All: {len(all_patents) if all_patents else 0}")

print('__RESULT__:')
print(json.dumps('Data access check completed'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}]}

exec(code, env_args)
