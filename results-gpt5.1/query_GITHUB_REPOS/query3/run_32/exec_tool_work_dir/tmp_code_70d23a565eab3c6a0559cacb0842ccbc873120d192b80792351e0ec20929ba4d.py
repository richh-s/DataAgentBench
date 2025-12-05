code = """import json, pathlib
from pathlib import Path

path = Path(var_call_t7xOSPWdmDU7Kfuu2E0Shawb)
with open(path) as f:
    queries = json.load(f)

batches = []
for i, q in enumerate(queries):
    batches.append({"id": i, "query": q})

print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_call_OTUOH9JSHbr0NQa3X0rbbdsJ': 'file_storage/call_OTUOH9JSHbr0NQa3X0rbbdsJ.json', 'var_call_RM4YWWPYtykZfJRoZa9J1Ufm': [{'cnt': '15016'}], 'var_call_t7xOSPWdmDU7Kfuu2E0Shawb': 'file_storage/call_t7xOSPWdmDU7Kfuu2E0Shawb.json'}

exec(code, env_args)
