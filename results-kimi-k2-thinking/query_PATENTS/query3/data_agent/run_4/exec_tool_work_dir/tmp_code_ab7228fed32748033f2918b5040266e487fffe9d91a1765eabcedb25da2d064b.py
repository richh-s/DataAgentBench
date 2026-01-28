code = """import json
import pandas as pd

result_file = var_functions.query_db:2

with open(result_file, 'r') as f:
    data = json.load(f)

count = sum(1 for record in data if 'UNIV CALIFORNIA' in record['Patents_info'])

result_dict = {'total': len(data), 'uni_california': count}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
