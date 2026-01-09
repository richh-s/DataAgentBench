code = """import json

# quick sanity
print('__RESULT__:')
print(json.dumps('ok'))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json'}

exec(code, env_args)
