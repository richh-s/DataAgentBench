code = """import json
p = var_call_v8UAmsuj3jIxT9Csk8ySlzip
print('__RESULT__:')
print(json.dumps({'path': p}))"""

env_args = {'var_call_v8UAmsuj3jIxT9Csk8ySlzip': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json', 'var_call_7cQ5gSCfYebF9BuEJ5E83c8m': 'file_storage/call_7cQ5gSCfYebF9BuEJ5E83c8m.json', 'var_call_iqqiSjgzDqx5k2lcbtWs0Kwd': {'a': 1}}

exec(code, env_args)
