code = """import json
print('__RESULT__:')
print(json.dumps('ok'))"""

env_args = {'var_call_gYJbskZiMLDqMqhJmUIqMw5P': 'file_storage/call_gYJbskZiMLDqMqhJmUIqMw5P.json', 'var_call_yC5xzU04KLrHiVtr69INvnjw': 'file_storage/call_yC5xzU04KLrHiVtr69INvnjw.json', 'var_call_QMPBqXPWLwySAtjtee9Dfswo': [{'ok': '1'}]}

exec(code, env_args)
