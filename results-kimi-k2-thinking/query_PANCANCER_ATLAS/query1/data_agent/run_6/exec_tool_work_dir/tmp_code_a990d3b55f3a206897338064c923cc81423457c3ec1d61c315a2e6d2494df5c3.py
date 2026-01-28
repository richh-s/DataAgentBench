code = """import json
# Access the clinical data from storage using locals()
clinical_data_path = locals()['var_functions.query_db:2']

with open(clinical_data_path, 'r') as f:
    clinical_data = json.load(f)

# Check structure of clinical data
if clinical_data:
    columns = list(clinical_data[0].keys())
    print('__RESULT__:')
    print(json.dumps({
        'total_records': len(clinical_data),
        'columns': sorted(columns)[:20],  # First 20 columns
        'sample_record': clinical_data[0]
    }, indent=2))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
