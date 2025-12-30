code = """import json, pandas as pd
from pathlib import Path

with open(var_call_nOqzOufOsztauC4aXgX8PTr5, 'r') as f:
    cits = json.load(f)

# Inspect keys
keys = sorted({k for row in cits for k in row.keys()})

out = json.dumps(keys)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EULIMl6zDz8YLz2d1z4pg5Sa': 'file_storage/call_EULIMl6zDz8YLz2d1z4pg5Sa.json', 'var_call_nOqzOufOsztauC4aXgX8PTr5': 'file_storage/call_nOqzOufOsztauC4aXgX8PTr5.json'}

exec(code, env_args)
