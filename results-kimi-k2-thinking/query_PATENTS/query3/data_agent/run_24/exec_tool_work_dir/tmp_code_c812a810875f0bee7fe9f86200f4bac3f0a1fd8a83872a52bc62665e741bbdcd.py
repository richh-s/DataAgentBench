code = """import json

# The result is stored in a file, let's read it
with open('var_functions.query_db:2.json', 'r') as f:
    sample_data = json.load(f)

# Print the required format
print('__RESULT__:')
print(json.dumps({
    'total_records': len(sample_data),
    'first_record_keys': list(sample_data[0].keys()) if sample_data else [],
    'first_record_patents_info': sample_data[0].get('Patents_info', '') if sample_data else '',
    'has_uc_records': any('UNIV CALIFORNIA' in r.get('Patents_info', '') for r in sample_data[:100])
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)
