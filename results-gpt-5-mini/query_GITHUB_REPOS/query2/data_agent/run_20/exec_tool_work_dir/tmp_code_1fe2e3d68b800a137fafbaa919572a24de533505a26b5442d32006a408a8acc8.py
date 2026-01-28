code = """import json, re

data_path = var_call_xDzCCeBp2zeDXdbtdpOtaITh
with open(data_path, 'r') as f:
    data = json.load(f)

results = []
for r in data:
    desc = r.get('repo_data_description','') or ''
    # find number before keywords
    m = re.search(r'(\d+)\s*(?=(?:times|time|copied|appearing|duplicated|seen|repeated))', desc, flags=re.I)
    if m:
        count = int(m.group(1))
    else:
        # fallback: search any number
        m2 = re.search(r'(\d+)', desc)
        count = int(m2.group(1)) if m2 else 1
    results.append({
        'id': r.get('id'),
        'sample_repo_name': r.get('sample_repo_name'),
        'sample_path': r.get('sample_path'),
        'count': count
    })

# find max count
max_count = max([x['count'] for x in results]) if results else 0
max_records = [x for x in results if x['count']==max_count]

out = {'max_count': max_count, 'max_records': max_records}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_64wtttyxZleAyJbWgZDrD4nf': ['commits', 'contents', 'files'], 'var_call_zDsFP1NQ8OcZk7QgxRMD7fVj': ['languages', 'repos', 'licenses'], 'var_call_xDzCCeBp2zeDXdbtdpOtaITh': 'file_storage/call_xDzCCeBp2zeDXdbtdpOtaITh.json', 'var_call_HgRZrr9azxaAmWmMe130BxCC': 'file_storage/call_HgRZrr9azxaAmWmMe130BxCC.json'}

exec(code, env_args)
