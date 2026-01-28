code = """import json
print('__RESULT__:')
print(json.dumps({'ok': True}))"""

env_args = {'var_call_XrHlNWKzMrgiQtx7cnfZcCrW': 'file_storage/call_XrHlNWKzMrgiQtx7cnfZcCrW.json', 'var_call_jWPZt9UPzSeXm5a2fEJh4H2f': 'file_storage/call_jWPZt9UPzSeXm5a2fEJh4H2f.json'}

exec(code, env_args)
