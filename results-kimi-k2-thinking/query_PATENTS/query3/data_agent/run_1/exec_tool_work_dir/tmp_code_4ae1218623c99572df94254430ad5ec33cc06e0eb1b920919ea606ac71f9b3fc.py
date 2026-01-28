code = """import json
import re

# Load the UNIV CALIFORNIA patents
uc_path = locals()['var_functions.query_db:6']
with open(uc_path, 'r') as f:
    uc_patents = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'sample_patent': uc_patents[0] if uc_patents else None
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_patents': 5, 'uc_patents': 10, 'sample_structure': ['Patents_info', 'cpc', 'citation'], 'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}}

exec(code, env_args)
