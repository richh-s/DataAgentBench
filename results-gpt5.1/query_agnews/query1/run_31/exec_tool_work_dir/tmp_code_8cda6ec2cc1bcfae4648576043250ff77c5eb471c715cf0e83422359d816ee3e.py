code = """import json
import pandas as pd

path = var_call_wDlXiKgFmCYp580cmBRPaSck
with open(path, 'r') as f:
    data = json.load(f)

max_item = max(data, key=lambda x: len(x.get('description', '') or ''))
result = max_item.get('title', '')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wDlXiKgFmCYp580cmBRPaSck': 'file_storage/call_wDlXiKgFmCYp580cmBRPaSck.json'}

exec(code, env_args)
