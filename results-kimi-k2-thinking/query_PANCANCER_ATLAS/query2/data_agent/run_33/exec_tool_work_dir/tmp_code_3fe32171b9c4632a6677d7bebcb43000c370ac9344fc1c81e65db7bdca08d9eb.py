code = """import json
import re

file_path = var_functions.query_db:22
with open(file_path, 'r') as f:
    clinical_data = json.load(f)

brca_alive = []
total_alive = 0

for record in clinical_data:
    desc = record.get('Patient_description', '')
    hist = record.get('histological_type', '')  
    death = record.get('days_to_death')
    
    alive = death in [None, 'None', '[Not Applicable]', 'nan', '']
    if alive:
        total_alive += 1
    
    brca = False
    if 'BRCA' in desc:
        brca = True
    if 'breast' in desc.lower():
        brca = True
    if 'breast' in hist.lower():
        brca = True
    
    if brca and alive:
        brca_alive.append({'desc': desc, 'hist': hist})

result = {
    'brca_alive_count': len(brca_alive),
    'total_alive': total_alive,
    'first_few': brca_alive[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:8': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': 'test', 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5', 'var_functions.query_db:8', 'var_functions.query_db:11', 'var_functions.execute_python:18'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
