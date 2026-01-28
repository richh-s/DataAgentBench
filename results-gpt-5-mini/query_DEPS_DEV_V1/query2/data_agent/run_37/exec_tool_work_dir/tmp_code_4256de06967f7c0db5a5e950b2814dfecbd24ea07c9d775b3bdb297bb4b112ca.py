code = """import json
fp = var_call_xoiRbYVhG6oB3Nh77ykHM5fW
with open(fp, 'r') as f:
    records = json.load(f)
seen = set()
pairs = []
for r in records:
    t = (r['Name'], r['Version'])
    if t not in seen:
        seen.add(t)
        pairs.append({'Name': t[0], 'Version': t[1]})
    if len(pairs) >= 500:
        break
out = {'num_pairs_total': len(seen), 'pairs_sample': pairs}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GFjoBvPPCjrqO1febE5dj3UX': ['packageinfo'], 'var_call_GEHAWCkzbkVYIGaW9lhUPqPS': ['project_info', 'project_packageversion'], 'var_call_xoiRbYVhG6oB3Nh77ykHM5fW': 'file_storage/call_xoiRbYVhG6oB3Nh77ykHM5fW.json'}

exec(code, env_args)
