code = """import json
q = "MAX(\"Adj Close\")"
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json', 'var_call_Xrg9kOJDlc2kXxtL5GJXTznh': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}], 'var_call_Q8z2nea3JG18qa0BPuomzZln': 'ok', 'var_call_7BMhlXRncCAyexjmMVlRDx0L': 'a', 'var_call_RZJn9nNTovXDj4fNNdtACmQ3': "SELECT 'SPY' AS symbol"}

exec(code, env_args)
