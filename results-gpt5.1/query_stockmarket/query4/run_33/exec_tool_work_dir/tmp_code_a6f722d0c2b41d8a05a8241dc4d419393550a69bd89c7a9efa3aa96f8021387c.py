code = """import json, pandas as pd, os
symbols = json.load(open(var_call_Q6E3M2xorFhQ3T4kqPpifgXe))
# filter plausible stock symbols: drop those containing non-alphanumeric except '.' or '-' and too long
filtered = [s for s in symbols if all(c.isalnum() or c in '.-' for c in s) and len(s)<=5]
result = json.dumps(filtered)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Q6E3M2xorFhQ3T4kqPpifgXe': 'file_storage/call_Q6E3M2xorFhQ3T4kqPpifgXe.json', 'var_call_v14b2ximDhbtElGaNzZdoYOU': 'file_storage/call_v14b2ximDhbtElGaNzZdoYOU.json'}

exec(code, env_args)
