code = """# Let's check what variables are available
import json
available_vars = list(locals().keys())
print("__RESULT__:")
print(json.dumps(available_vars))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
