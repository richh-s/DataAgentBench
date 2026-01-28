code = """import json
import pandas as pd
import os

# Get the file path from the stored variable
result_filepath = locals()['var_functions.query_db:2']
print('__RESULT__:')
print("File path:", str(result_filepath))
print("File exists:", os.path.exists(result_filepath))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
