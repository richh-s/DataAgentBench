code = """import json

print('__RESULT__:')
print(json.dumps({'count': int(var_call_aPDVTux9oknE8VfTjSjsf1Jj[0]['cnt'])}))"""

env_args = {'var_call_aPDVTux9oknE8VfTjSjsf1Jj': [{'cnt': '276'}], 'var_call_T4Ojw85gpLpoASrRx4vCTzoJ': 'file_storage/call_T4Ojw85gpLpoASrRx4vCTzoJ.json', 'var_call_XlaC5SXo3fAX4eJY28nmeBkQ': 'file_storage/call_XlaC5SXo3fAX4eJY28nmeBkQ.json'}

exec(code, env_args)
