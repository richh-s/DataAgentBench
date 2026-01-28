code = """import json
from pathlib import Path

# Load the query results from the stored JSON files
contents_path = Path(var_call_jQQSgzJH4LwIFK5GGYOlnsgn)
languages_path = Path(var_call_0Egm93ckdSYZQKPTuYeDx3Ry)

with open(contents_path, 'r', encoding='utf-8') as f:
    contents = json.load(f)
with open(languages_path, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Build set of repositories declared Swift
swift_repo_set = set()
for r in languages:
    name = r.get('repo_name')
    if name:
        swift_repo_set.add(name)

# Filter non-binary .swift entries and count occurrences by id
counts = {}
id_to_repos = {}
for rec in contents:
    path = rec.get('sample_path','') or ''
    desc = rec.get('repo_data_description','') or ''
    if not path.lower().endswith('.swift'):
        continue
    if 'binary' in desc.lower():
        continue
    rid = rec.get('id')
    if not rid:
        continue
    counts[rid] = counts.get(rid, 0) + 1
    id_to_repos.setdefault(rid, set()).add(rec.get('sample_repo_name'))

if not counts:
    result = {"error": "no non-binary swift files found"}
else:
    max_count = max(counts.values())
    max_ids = [rid for rid,c in counts.items() if c==max_count]
    candidates = []
    for rid in max_ids:
        repos = sorted(list(id_to_repos.get(rid, [])))
        swift_repos = [r for r in repos if r in swift_repo_set]
        candidates.append({"id": rid, "copies": counts[rid], "repos": repos, "swift_repos": swift_repos})
    result = {"max_copies": max_count, "candidates": candidates}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5KRbupHvs2wmPHCPXMMfBEDn': [], 'var_call_KK1dL8G6KJlTANfIWAh52t2G': [], 'var_call_0Egm93ckdSYZQKPTuYeDx3Ry': 'file_storage/call_0Egm93ckdSYZQKPTuYeDx3Ry.json', 'var_call_tezl9OVPxPVJjImyosaXXcQ7': 'file_storage/call_tezl9OVPxPVJjImyosaXXcQ7.json', 'var_call_Q25tp1Q7XUOgQLwg9OAIKqJf': [{'cnt': '105'}], 'var_call_OSJbegtlIVR7o1m5lEH4rMlB': [], 'var_call_jQQSgzJH4LwIFK5GGYOlnsgn': 'file_storage/call_jQQSgzJH4LwIFK5GGYOlnsgn.json'}

exec(code, env_args)
