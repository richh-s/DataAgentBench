code = """import json
print('__RESULT__:')
print(json.dumps({'a':1}))"""

env_args = {'var_call_W9DknPtITkO5E8fVFyGGCP1i': 'file_storage/call_W9DknPtITkO5E8fVFyGGCP1i.json', 'var_call_IkdZGIDgN5BwsY28UnCmseZJ': 'file_storage/call_IkdZGIDgN5BwsY28UnCmseZJ.json'}

exec(code, env_args)
