code = """import json
import pandas as pd

# Read the file paths from the variables
articles_path = 'var_functions.query_db:4'  
metadata_path = 'var_functions.query_db:6'

print('__RESULT__:')
print('Variables defined')"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
