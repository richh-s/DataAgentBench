code = """import json
# var_call_s0SMA8mwCgYpSST807JOmhU0 is provided in storage (path to JSON file)
path = var_call_s0SMA8mwCgYpSST807JOmhU0
with open(path, 'r') as f:
    data = json.load(f)
purchase_ids = sorted({r['purchase_id'] for r in data})
import json
print("__RESULT__:")
print(json.dumps(purchase_ids))"""

env_args = {'var_call_mnbPILAIpkDaj9iYNGPwjVOp': ['review'], 'var_call_M2rFox5fpysDiznYKTSJfXOB': ['books_info'], 'var_call_s0SMA8mwCgYpSST807JOmhU0': 'file_storage/call_s0SMA8mwCgYpSST807JOmhU0.json'}

exec(code, env_args)
