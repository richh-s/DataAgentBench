code = """import json
import pandas as pd

# var_call_l4mGwoA9VE0pZo0i7k2073ZS is a path to a JSON file with repo_name records
with open(var_call_l4mGwoA9VE0pZo0i7k2073ZS, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build a SQL IN clause in chunks to avoid too-long queries
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join(["'" + name.replace("'", "''") + "'" for name in chunk])
    chunks.append(f"repo_name IN ({in_list})")

where_clause = " OR ".join(chunks) if chunks else "1=0"

result = json.dumps({"where_clause": where_clause})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_l4mGwoA9VE0pZo0i7k2073ZS': 'file_storage/call_l4mGwoA9VE0pZo0i7k2073ZS.json', 'var_call_ORXsSp6ga1HLOLovfr8LwBrk': [{'cnt': '15016'}]}

exec(code, env_args)
