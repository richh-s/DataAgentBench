code = """import json
file_path = locals()['var_functions.query_db:18']

with open(file_path, 'r') as f:
    data = json.load(f)

print('Records:', len(data))
first = data[0]
print('First patent info:', first['Patents_info'][:150])

citations = json.loads(first['citation'])
print('Citations:', len(citations))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
