code = """import json, pandas as pd
syms = pd.read_json(var_call_gVBDgqfFU3fmp05yZZylgnTV)
trade_tables = pd.read_json(var_call_sOxxqvjBZARcG1IuBxCd97c5)
common = sorted(set(syms['Symbol']).intersection(set(trade_tables)))
print('__RESULT__:')
print(json.dumps(common))"""

env_args = {'var_call_sOxxqvjBZARcG1IuBxCd97c5': 'file_storage/call_sOxxqvjBZARcG1IuBxCd97c5.json', 'var_call_gVBDgqfFU3fmp05yZZylgnTV': 'file_storage/call_gVBDgqfFU3fmp05yZZylgnTV.json'}

exec(code, env_args)
