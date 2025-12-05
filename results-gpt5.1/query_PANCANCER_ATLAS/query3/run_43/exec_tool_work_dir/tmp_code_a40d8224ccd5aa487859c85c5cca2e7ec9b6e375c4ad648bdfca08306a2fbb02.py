code = """import json, re, pandas as pd

sample = var_call_kFdtIxdw17Uuf9hYNi6CocaY
cols = list(sample[0].keys())

result = json.dumps(cols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_sk1CdOkFtNMBWzsiQ5Kx4Ajt': 'file_storage/call_sk1CdOkFtNMBWzsiQ5Kx4Ajt.json', 'var_call_LqJsTSDxhZBl9m4Ay3avMuyZ': ['clinical_info'], 'var_call_kFdtIxdw17Uuf9hYNi6CocaY': 'file_storage/call_kFdtIxdw17Uuf9hYNi6CocaY.json'}

exec(code, env_args)
