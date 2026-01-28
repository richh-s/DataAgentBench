code = """import json

print('__RESULT__:')
print(json.dumps({'note':'debug'}))"""

env_args = {'var_call_q7oLujAQPcdluZq4wIf6UcE4': 'file_storage/call_q7oLujAQPcdluZq4wIf6UcE4.json', 'var_call_xKK2gQkeQKeKmrdma80MfrG0': 'file_storage/call_xKK2gQkeQKeKmrdma80MfrG0.json'}

exec(code, env_args)
