code = """import json
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    papers = json.load(f)
print('__RESULT__:')
print(json.dumps(len(papers)))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
