code = """import json, pandas as pd

# Load full repo list from file
path = var_call_vJBLmxJKSPkjp0uqlsBQCoa4
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Create an IN clause chunked to avoid overly long queries
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    # Escape single quotes
    vals = ",".join(["'" + r.replace("'", "''") + "'" for r in chunk])
    chunks.append(f"repo_name IN ({vals})")

where_clause = " OR ".join(chunks) if chunks else '1=0'

query = "SELECT COUNT(*) AS cnt FROM commits WHERE (" + where_clause + ") AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"

result = query

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vJBLmxJKSPkjp0uqlsBQCoa4': 'file_storage/call_vJBLmxJKSPkjp0uqlsBQCoa4.json', 'var_call_be6nYBBjSHIDM5KM4r0PcnO3': [{'cnt': '15016'}]}

exec(code, env_args)
