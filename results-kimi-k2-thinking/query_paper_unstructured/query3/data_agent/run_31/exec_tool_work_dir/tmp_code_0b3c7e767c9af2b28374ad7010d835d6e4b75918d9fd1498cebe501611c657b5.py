code = """import json

# Check what the variable contains
papers_data = locals()['var_functions.query_db:4']
print('__RESULT__:')
print(json.dumps(str(type(papers_data))))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
