code = """import json
fp = var_call_7RDsQJ4weAgqRJhZMU3kruDs
print('__RESULT__:')
print(json.dumps({'path': fp}))"""

env_args = {'var_call_woj4tIn0U10exCkWbYaBd5Yf': ['checkin', 'business'], 'var_call_ijrp6giWNGCVcjhdTof3zBx6': ['review', 'tip', 'user'], 'var_call_qAmoAqh3sTe1FeETR7N45GKP': 'file_storage/call_qAmoAqh3sTe1FeETR7N45GKP.json', 'var_call_7RDsQJ4weAgqRJhZMU3kruDs': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json'}

exec(code, env_args)
