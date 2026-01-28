code = """import json

# Read the full civic docs data from the file stored by the previous query
with open('var_functions.query_db:0', 'r') as f:
    civic_docs_data = json.load(f)

print('__RESULT__:')
print(json.dumps(f'Number of civic docs: {len(civic_docs_data)}'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
