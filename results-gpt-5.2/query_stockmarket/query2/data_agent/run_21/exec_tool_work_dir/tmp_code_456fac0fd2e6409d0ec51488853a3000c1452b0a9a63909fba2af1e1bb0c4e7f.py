code = """import json
q = 'SELECT \'AAAU\' AS symbol, MAX("Adj Close") AS m FROM "AAAU"'
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_NZ0JfUmxkUXZtZhMlGbm0tDu': 'file_storage/call_NZ0JfUmxkUXZtZhMlGbm0tDu.json', 'var_call_aTsh1In8HMrOaUxRKitJk4wo': 'file_storage/call_aTsh1In8HMrOaUxRKitJk4wo.json', 'var_call_U9EfGLpOkTlayKj1ozkxcQcY': {'n_tickers': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_eXF2jCX9vVN63ZeYWX46HRZb': 'file_storage/call_eXF2jCX9vVN63ZeYWX46HRZb.json', 'var_call_idLqIfVWfUT0SaiEtbRhgVzc': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_call_7b54IpID7GntJHh06TKnktb1': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_sQVD6FKG4ELMbhSXVMWrgtPO': "SELECT 'AAAU' AS symbol", 'var_call_DU7qi2lOvmjq70kT21Gv6GLm': "SELECT 'AAAU' AS symbol, MAX('x') AS m", 'var_call_fqoW3iUFP5BUE6wkKAkaRu3q': [{'symbol': 'AADR', 'max_adj_close_2015': '39.58057403564453'}], 'var_call_ZrL7MmPrCSAeMZ2pMbzwB1yY': 'MAX("Adj Close")'}

exec(code, env_args)
