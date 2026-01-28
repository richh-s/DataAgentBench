code = """import json
import pandas as pd

# Read articles data from the file path stored in the variable
with open(var_functions.query_db_4, 'r') as f:
    articles_data = json.load(f)

# Read metadata data from the file path stored in the variable
with open(var_functions.query_db_6, 'r') as f:
    metadata_data = json.load(f)

# Basic overview
print('__RESULT__:')
print('Loaded ' + str(len(articles_data)) + ' articles and ' + str(len(metadata_data)) + ' metadata records')"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
