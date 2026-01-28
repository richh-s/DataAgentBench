code = """import json
etf_var = var_call_ASxqUidKouxirPTsX6kyMaGX
print('__RESULT__:')
print(json.dumps({'type': str(type(etf_var)), 'is_str': isinstance(etf_var, str)}))"""

env_args = {'var_call_ASxqUidKouxirPTsX6kyMaGX': 'file_storage/call_ASxqUidKouxirPTsX6kyMaGX.json', 'var_call_qDAxo3HVUHPjQPFy7oZgucv5': 'file_storage/call_qDAxo3HVUHPjQPFy7oZgucv5.json', 'var_call_tVCECwffNXINpFAgd099c7UH': [{'x': 'DUMMY'}], 'var_call_91jccmvZMcEWEuAJAsaVFqm0': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}], 'var_call_fPP4wsWWGtNhqAp74CX0913q': {'ok': True}}

exec(code, env_args)
