code = """import json
import pandas as pd

# Debug - print the variable types first  
print('citations_2018 type:', type(var_functions.query_db:7))
print('paper_docs type:', type(var_functions.query_db:3))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
