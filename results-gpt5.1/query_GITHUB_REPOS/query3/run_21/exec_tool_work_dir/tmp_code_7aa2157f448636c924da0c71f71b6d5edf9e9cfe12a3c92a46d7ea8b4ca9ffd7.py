code = """import json

# var_call_G1kLGJbYGUhSMHeG8NPUH3Zr is a path to json file when large
import os, pandas as pd
path = var_call_G1kLGJbYGUhSMHeG8NPUH3Zr
with open(path, 'r') as f:
    data = json.load(f)
repos = [r['repo_name'] for r in data]
values_clause = ",".join(["('" + r.replace("'", "''") + "')" for r in repos])
query = "SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN (" + ",".join(["'"+r.replace("'","''")+"'" for r in repos]) + ") AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
result = json.dumps({"query": query})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_G1kLGJbYGUhSMHeG8NPUH3Zr': 'file_storage/call_G1kLGJbYGUhSMHeG8NPUH3Zr.json', 'var_call_PNdEVRPWylqYzQkyPy3PY7Sp': [{'cnt': '15016'}]}

exec(code, env_args)
