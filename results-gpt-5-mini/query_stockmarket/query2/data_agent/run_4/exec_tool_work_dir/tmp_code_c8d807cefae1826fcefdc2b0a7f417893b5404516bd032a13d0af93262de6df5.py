code = """import json
import pandas as pd
# Load variables from storage
rl1 = None
rl2 = None
try:
    rl1 = var_call_CkOett6RT3NpMdVOnQ5Rdezm
except Exception as e:
    pass
try:
    rl2 = var_call_DSMBYKQmd3iXKyKYg6Sw5gVC
except Exception as e:
    pass
# rl1: list of dicts from stockinfo query. Extract symbols
symbols_info = [r['Symbol'] for r in rl1]
# rl2: list of table names
tables = rl2
# intersect
symbols_to_check = sorted(list(set(symbols_info).intersection(set(tables))))
result = json.dumps(symbols_to_check)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_CkOett6RT3NpMdVOnQ5Rdezm': 'file_storage/call_CkOett6RT3NpMdVOnQ5Rdezm.json', 'var_call_DSMBYKQmd3iXKyKYg6Sw5gVC': 'file_storage/call_DSMBYKQmd3iXKyKYg6Sw5gVC.json'}

exec(code, env_args)
