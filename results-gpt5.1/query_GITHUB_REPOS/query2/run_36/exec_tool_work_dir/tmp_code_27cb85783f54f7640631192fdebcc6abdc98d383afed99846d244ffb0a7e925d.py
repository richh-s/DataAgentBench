code = """import json, re
from pathlib import Path

path = Path(var_call_4TjhrxC1Plavpr4wDgN86VFy)
rows = json.loads(path.read_text())

max_copies = -1
best = None
for r in rows:
    m = re.search(r"(copied|appearing|duplicated|seen|repeated) (\d+) times", r["repo_data_description"])
    if not m:
        continue
    copies = int(m.group(2))
    if copies > max_copies:
        max_copies = copies
        best = r

result = {"max_copies": max_copies, "id": best["id"], "sample_repo_name": best["sample_repo_name"], "repo_data_description": best["repo_data_description"]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4TjhrxC1Plavpr4wDgN86VFy': 'file_storage/call_4TjhrxC1Plavpr4wDgN86VFy.json'}

exec(code, env_args)
