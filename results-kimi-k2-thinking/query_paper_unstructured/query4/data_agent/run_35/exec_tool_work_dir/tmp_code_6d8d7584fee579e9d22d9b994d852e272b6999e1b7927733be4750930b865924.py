code = """import json, os, glob

# Look for the actual file in the file_storage directory
files = []
if os.path.exists('file_storage'):
    files = os.listdir('file_storage')
else:
    # Try to find JSON files anywhere
    files = glob.glob('**/*.json', recursive=True)

print('__RESULT__:')
print(json.dumps(files))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
