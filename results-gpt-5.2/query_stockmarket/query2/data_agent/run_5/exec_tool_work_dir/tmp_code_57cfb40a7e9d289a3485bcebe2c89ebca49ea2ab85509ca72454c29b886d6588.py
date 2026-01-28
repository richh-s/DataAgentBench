code = """import json
q = "SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym='SPY')
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json', 'var_call_Xrg9kOJDlc2kXxtL5GJXTznh': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}]}

exec(code, env_args)
