code = """import json, pandas as pd

path = var_call_5UTLYr6CjRTZ3IeIVAZpQMJA
with open(path, 'r') as f:
    cites = json.load(f)

print('__RESULT__:')
print(json.dumps({'columns': list(pd.DataFrame(cites).columns)}))"""

env_args = {'var_call_QVVMdIHmtyFsuI5sqTG3yzN5': 'file_storage/call_QVVMdIHmtyFsuI5sqTG3yzN5.json', 'var_call_5UTLYr6CjRTZ3IeIVAZpQMJA': 'file_storage/call_5UTLYr6CjRTZ3IeIVAZpQMJA.json'}

exec(code, env_args)
