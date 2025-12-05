code = """import json, pandas as pd
from pathlib import Path

symbols_file = var_call_AcKDswczsOcXnXZEVKxFjaXp
symbols = pd.read_json(symbols_file)

symbols_list = symbols['Symbol'].tolist()

result = json.dumps(symbols_list)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_B2M7G0jKhwkzf7Yh3TG2wneV': 'file_storage/call_B2M7G0jKhwkzf7Yh3TG2wneV.json', 'var_call_AcKDswczsOcXnXZEVKxFjaXp': 'file_storage/call_AcKDswczsOcXnXZEVKxFjaXp.json'}

exec(code, env_args)
