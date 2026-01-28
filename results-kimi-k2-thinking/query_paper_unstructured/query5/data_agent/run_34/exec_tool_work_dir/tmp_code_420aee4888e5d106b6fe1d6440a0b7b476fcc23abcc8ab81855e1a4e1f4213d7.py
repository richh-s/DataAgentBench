code = """import json
import re

chi_papers_file = locals()['var_functions.query_db:2']
print("__RESULT__:")
print(json.dumps(chi_papers_file))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
