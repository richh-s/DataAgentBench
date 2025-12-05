code = """import json
import pandas as pd

# var_call_G1kLGJbYGUhSMHeG8NPUH3Zr contains list of repos using Shell and Apache-2.0
repos = [r['repo_name'] for r in var_call_G1kLGJbYGUhSMHeG8NPUH3Zr]

# Convert to SQL IN list safely by quoting repo names
# Chunk into groups to avoid very large IN clause; but we really only need the count over all.
# We'll just create a temp table list as a VALUES clause.
values_clause = ",".join(["('" + r.replace("'", "''") + "')" for r in repos])
query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN (SELECT column1 FROM (VALUES {values_clause})) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"

result = json.dumps({"query": query})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_G1kLGJbYGUhSMHeG8NPUH3Zr': 'file_storage/call_G1kLGJbYGUhSMHeG8NPUH3Zr.json', 'var_call_PNdEVRPWylqYzQkyPy3PY7Sp': [{'cnt': '15016'}]}

exec(code, env_args)
