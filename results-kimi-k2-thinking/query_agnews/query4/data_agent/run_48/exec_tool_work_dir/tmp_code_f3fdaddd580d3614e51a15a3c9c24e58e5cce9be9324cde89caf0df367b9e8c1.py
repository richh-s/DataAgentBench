code = """import json

# Load the full metadata result from the file
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'record_count': len(metadata_2015),
    'first_five': metadata_2015[:5],
    'data_type': str(type(metadata_2015))
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
