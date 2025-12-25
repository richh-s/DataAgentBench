code = """import json, re, os
path = var_call_Pbyee6l3JZpWBR8HmnFCzn9d
with open(path) as f:
    data = json.load(f)
max_copies = -1
best = None
for row in data:
    m = re.search(r"(copied|appearing|repeated|duplicated) (\d+) times", row.get("repo_data_description",""))
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        best = row
result = {"repo_name": best["sample_repo_name"], "id": best["id"], "copies": max_copies}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Pbyee6l3JZpWBR8HmnFCzn9d': 'file_storage/call_Pbyee6l3JZpWBR8HmnFCzn9d.json'}

exec(code, env_args)
