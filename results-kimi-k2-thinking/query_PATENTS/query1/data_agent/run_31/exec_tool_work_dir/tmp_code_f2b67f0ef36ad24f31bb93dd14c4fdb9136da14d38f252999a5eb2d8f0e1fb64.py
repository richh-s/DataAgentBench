code = """import pandas as pd
import numpy as np
import json
import re
from collections import defaultdict

# Get result from storage
stored_file = locals()['var_functions.query_db:10']
print(f'Stored result type: {type(stored_file)}')
print(f'Stored result: {stored_file}')

# Find CPC groups at level 5 with best EMA in 2022
cpc_groups = []
print('Found CPC groups with best year 2022:')
print(json.dumps(cpc_groups))

print('__RESULT__:')
print(json.dumps(cpc_groups))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'count': '277813'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
