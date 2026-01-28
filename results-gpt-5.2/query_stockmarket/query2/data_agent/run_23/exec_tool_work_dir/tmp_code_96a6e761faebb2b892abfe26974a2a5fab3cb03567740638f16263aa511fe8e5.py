code = """import json
print('__RESULT__:')
print(json.dumps({'ok': True}))"""

env_args = {'var_call_L7ddSgvG4pwxWupzI6Jilkxd': 'file_storage/call_L7ddSgvG4pwxWupzI6Jilkxd.json', 'var_call_h8spSELnHicwBjN3VuyEck6c': 'file_storage/call_h8spSELnHicwBjN3VuyEck6c.json'}

exec(code, env_args)
