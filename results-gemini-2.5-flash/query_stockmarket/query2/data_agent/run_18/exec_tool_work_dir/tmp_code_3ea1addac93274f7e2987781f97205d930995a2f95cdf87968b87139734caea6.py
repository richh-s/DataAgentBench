code = """import json

with open(locals()['var_function-call-16760421366032888909'], 'r') as f:
    etf_symbols_data = json.load(f)

symbols_list = [d['Symbol'] for d in etf_symbols_data]

print('__RESULT__:')
print(json.dumps(len(symbols_list)))"""

env_args = {'var_function-call-16760421366032888909': 'file_storage/function-call-16760421366032888909.json'}

exec(code, env_args)
