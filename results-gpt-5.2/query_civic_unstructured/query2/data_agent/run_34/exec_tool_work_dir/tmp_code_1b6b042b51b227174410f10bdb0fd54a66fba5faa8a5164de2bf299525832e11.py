code = """import json
out={'note':'python run'}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KcYHlncOaFoH06aDA133uxk6': ['Funding'], 'var_call_vce97t2PfwFA5ltMgxq0udMD': ['civic_docs'], 'var_call_3K7hEc85tmIapV7kNVXe0blH': 'file_storage/call_3K7hEc85tmIapV7kNVXe0blH.json', 'var_call_u7VKhrByYEe1IOOvkFi0EPhw': 'file_storage/call_u7VKhrByYEe1IOOvkFi0EPhw.json'}

exec(code, env_args)
