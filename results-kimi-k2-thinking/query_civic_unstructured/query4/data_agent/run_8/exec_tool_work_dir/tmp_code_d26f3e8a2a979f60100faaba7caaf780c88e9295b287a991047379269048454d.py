code = """import json
import os

# Get the file path from the storage variable
file_path_variable = 'var_functions.query_db:6'
mongo_results_file = locals().get(file_path_variable, '')

print(f"File path from variable: {mongo_results_file}")
print(f"Type: {type(mongo_results_file)}")

# Read the actual file
if os.path.exists(mongo_results_file):
    with open(mongo_results_file, 'r') as f:
        mongo_results = json.load(f)
    print(f"Successfully loaded {len(mongo_results)} records")
else:
    print(f"File not found: {mongo_results_file}")
    mongo_results = []

result = {
    'file_path': mongo_results_file,
    'file_exists': os.path.exists(mongo_results_file) if mongo_results_file else False,
    'record_count': len(mongo_results)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
