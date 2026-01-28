code = """import json
result_path = var_functions.query_db:6
with open(result_path, 'r') as f:
    clinical_data = json.load(f)
print('Total records:', len(clinical_data))
if clinical_data:
    print('First record keys:', list(clinical_data[0].keys()))
    print('Sample Patient_description:', clinical_data[0]['Patient_description'])
    print('Sample histological_type:', clinical_data[0]['histological_type'])

lgg_count = sum(1 for p in clinical_data if 'LGG' in p.get('Patient_description', ''))
print('LGG mentioned in Patient_description:', lgg_count)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
