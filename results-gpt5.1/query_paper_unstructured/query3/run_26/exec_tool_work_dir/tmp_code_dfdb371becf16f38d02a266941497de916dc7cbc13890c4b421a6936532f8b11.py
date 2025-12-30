code = """import json, pandas as pd

with open(var_call_9cKZRhGI6XXizXbWJB5czsqU, 'r') as f:
    citations_records = json.load(f)

# Inspect keys
first = citations_records[0]
result = list(first.keys())

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uzjJKQEGOkxiNnYlwMAOuxIe': 'file_storage/call_uzjJKQEGOkxiNnYlwMAOuxIe.json', 'var_call_9cKZRhGI6XXizXbWJB5czsqU': 'file_storage/call_9cKZRhGI6XXizXbWJB5czsqU.json'}

exec(code, env_args)
