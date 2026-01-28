code = """import json
import pandas as pd

filepath = locals().get('var_functions.query_db:5');
print('filepath:', filepath)

data = json.load(open(filepath))
print('patent count:', len(data))

first = data[0]
print('keys:', list(first.keys()))
print('patents_info snippet:', first['Patents_info'][:150])
print('citation length:', len(str(first['citation'])))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
