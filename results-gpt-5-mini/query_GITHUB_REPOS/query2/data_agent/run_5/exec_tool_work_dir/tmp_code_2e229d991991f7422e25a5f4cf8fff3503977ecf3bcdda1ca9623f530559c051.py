code = """import json, re
# var_call_5kwmVYoTwP0phgwlqdFkzai6 is the path to the JSON result from previous query
p = var_call_5kwmVYoTwP0phgwlqdFkzai6
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract counts from repo_data_description
counts = {}
id_to_repos = {}
pattern = re.compile(r"(\d+)\s+times", re.IGNORECASE)
for rec in data:
    idv = rec.get('id')
    desc = rec.get('repo_data_description','')
    m = pattern.search(desc)
    if m:
        cnt = int(m.group(1))
    else:
        # fallback: look for 'appearing N' or 'copied N' or 'seen N' etc
        m2 = re.search(r"(\d+)\s+(?:appearing|copied|seen|duplicated|repeated)", desc, re.IGNORECASE)
        if m2:
            cnt = int(m2.group(1))
        else:
            # assume single occurrence if no number found
            cnt = 1
    counts[idv] = max(counts.get(idv,0), cnt)
    # collect repo names
    repo = rec.get('sample_repo_name')
    id_to_repos.setdefault(idv, set()).add(repo)

if not counts:
    result = {"top_count":0, "top_ids":[], "repos":[], "id_to_repos":{}}
else:
    maxcnt = max(counts.values())
    top_ids = [i for i,c in counts.items() if c==maxcnt]
    repos = sorted({r for i in top_ids for r in id_to_repos.get(i,[]) if r})
    id_to_repos_serializable = {i:sorted(list(s)) for i,s in id_to_repos.items()}
    result = {"top_count": maxcnt, "top_ids": top_ids, "repos": repos, "id_to_repos": id_to_repos_serializable}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1yQTuc2aUf7C6YNMNKB4Bl8J': 'file_storage/call_1yQTuc2aUf7C6YNMNKB4Bl8J.json', 'var_call_5kwmVYoTwP0phgwlqdFkzai6': 'file_storage/call_5kwmVYoTwP0phgwlqdFkzai6.json'}

exec(code, env_args)
