code = """import json
print('__RESULT__:')
print(json.dumps('ok'))"""

env_args = {'var_call_IGFXHUnqBZxLEESlaW1VjsQS': ['stockinfo'], 'var_call_HB4X7789w5RugKPxR8cyQbNE': 'file_storage/call_HB4X7789w5RugKPxR8cyQbNE.json', 'var_call_IxW6haiTFueyDjZZpfh1Pko3': 'file_storage/call_IxW6haiTFueyDjZZpfh1Pko3.json'}

exec(code, env_args)
