code = """import json
import pandas as pd
from pathlib import Path

symbols = json.load(open(var_call_bJICUAbpJUwglQ5xaYtXCzka))
# we'll filter later by intersection; for now just pass through
result = json.dumps(symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_bJICUAbpJUwglQ5xaYtXCzka': 'file_storage/call_bJICUAbpJUwglQ5xaYtXCzka.json', 'var_call_zRgyKPBN7HPsNtEzD5tmKyk7': 'file_storage/call_zRgyKPBN7HPsNtEzD5tmKyk7.json'}

exec(code, env_args)
