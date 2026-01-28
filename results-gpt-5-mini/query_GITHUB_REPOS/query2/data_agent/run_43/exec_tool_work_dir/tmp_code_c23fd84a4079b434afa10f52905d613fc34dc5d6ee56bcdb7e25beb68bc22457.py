code = """import json
# Accessing storage variables
records = var_call_jQQSgzJH4LwIFK5GGYOlnsgn
swift_repos = var_call_0Egm93ckdSYZQKPTuYeDx3Ry

# Build set of repositories declared Swift
swift_repo_set = set()
for r in swift_repos:
    name = r.get('repo_name')
    if name:
        swift_repo_set.add(name)

# Filter non-binary entries and count occurrences by id
counts = {}
id_to_repos = {}
for rec in records:
    rid = rec.get('id')
    desc = rec.get('repo_data_description') or ''
    if 'binary' in desc.lower():
        continue
    counts[rid] = counts.get(rid, 0) + 1
    id_to_repos.setdefault(rid, set()).add(rec.get('sample_repo_name'))

if not counts:
    result = {"error": "no non-binary swift files found"}
else:
    # find max
    max_count = max(counts.values())
    max_ids = [rid for rid,c in counts.items() if c==max_count]
    # For each id, find repos that are in swift_repo_set
    candidates = []
    for rid in max_ids:
        repos = sorted(list(id_to_repos.get(rid, [])))
        swift_containing = [r for r in repos if r in swift_repo_set]
        candidates.append({"id": rid, "copies": counts[rid], "repos": repos, "swift_repos": swift_containing})
    result = {"max_copies": max_count, "candidates": candidates}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5KRbupHvs2wmPHCPXMMfBEDn': [], 'var_call_KK1dL8G6KJlTANfIWAh52t2G': [], 'var_call_0Egm93ckdSYZQKPTuYeDx3Ry': 'file_storage/call_0Egm93ckdSYZQKPTuYeDx3Ry.json', 'var_call_tezl9OVPxPVJjImyosaXXcQ7': 'file_storage/call_tezl9OVPxPVJjImyosaXXcQ7.json', 'var_call_Q25tp1Q7XUOgQLwg9OAIKqJf': [{'cnt': '105'}], 'var_call_OSJbegtlIVR7o1m5lEH4rMlB': [], 'var_call_jQQSgzJH4LwIFK5GGYOlnsgn': 'file_storage/call_jQQSgzJH4LwIFK5GGYOlnsgn.json'}

exec(code, env_args)
