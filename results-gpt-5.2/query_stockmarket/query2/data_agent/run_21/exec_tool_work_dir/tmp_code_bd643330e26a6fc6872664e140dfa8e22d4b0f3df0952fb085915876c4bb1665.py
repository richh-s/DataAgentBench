code = """import json

t = ['AAAU','AADR','ABEQ']
q = "SELECT '{}' AS symbol".format(t[0])
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json', 'var_call_U9EfGLpOkTlayKj1ozkxcQcY': {'n_tickers': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_eXF2jCX9vVN63ZeYWX46HRZb': 'file_storage/call_eXF2jCX9vVN63ZeYWX46HRZb.json', 'var_call_idLqIfVWfUT0SaiEtbRhgVzc': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_call_7b54IpID7GntJHh06TKnktb1': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}]}

exec(code, env_args)
