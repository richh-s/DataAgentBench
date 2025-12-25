code = """import json
import pandas as pd

with open(locals()['var_function-call-12425289590227642337'], 'r') as f:
    symbols_data = json.load(f)

symbols = [item['Symbol'] for item in symbols_data]


print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_function-call-12425289590227642337': 'file_storage/function-call-12425289590227642337.json'}

exec(code, env_args)
