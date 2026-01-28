code = """import json
import pandas as pd
from datetime import datetime
import re
import os

# Read the file directly since we know the pattern
file_pattern = 'tmp_'
files = [f for f in os.listdir('/tmp') if f.startswith(file_pattern)]
print('__RESULT__:')
print(json.dumps({'files_in_tmp': files}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
