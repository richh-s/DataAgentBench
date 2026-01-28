code = """import json
papers = locals()['var_functions.query_db:0']
print('__RESULT__:')
print(json.dumps({'count': len(papers)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs']}

exec(code, env_args)
