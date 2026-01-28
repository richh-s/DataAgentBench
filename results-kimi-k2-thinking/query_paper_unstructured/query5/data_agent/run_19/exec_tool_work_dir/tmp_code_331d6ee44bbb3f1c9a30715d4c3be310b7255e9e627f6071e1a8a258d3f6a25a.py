code = """import json

# Get the citations data from storage (handle the colon in the key name)
citations_data = globals().get('var_functions.query_db:2')

# If it's a string (file path), read the JSON file
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Debug info
print('__RESULT__:')
print(json.dumps({
    'type': str(type(citations_data)),
    'is_string': isinstance(citations_data, str),
    'is_list': isinstance(citations_data, list)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
