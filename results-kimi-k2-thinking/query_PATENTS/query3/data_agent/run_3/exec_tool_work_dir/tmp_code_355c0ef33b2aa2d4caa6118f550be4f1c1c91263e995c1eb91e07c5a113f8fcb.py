code = """import json
import os

# Load the UNIV CALIFORNIA patents data
file_path = locals().get('var_functions.query_db:5', '')
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

# Debug: show the structure of one patent
first_patent = uc_patents[0] if uc_patents else None

result = {
    'total_patents': len(uc_patents),
    'sample_patent': first_patent
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 'Found 50 patents from UNIV CALIFORNIA', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
