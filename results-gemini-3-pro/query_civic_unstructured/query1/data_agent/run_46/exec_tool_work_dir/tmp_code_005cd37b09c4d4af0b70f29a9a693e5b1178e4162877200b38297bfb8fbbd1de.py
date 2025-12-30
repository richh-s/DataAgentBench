code = """import json
k1 = 'var_function-call-13970698935459151877'
k2 = 'var_function-call-13579203068557831030'
with open(locals()[k1], 'r') as f: funding = json.load(f)

c_fund = 0
for x in funding:
    if float(x['Amount']) > 50000: c_fund += 1

print('__RESULT__:')
print(c_fund)"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)
