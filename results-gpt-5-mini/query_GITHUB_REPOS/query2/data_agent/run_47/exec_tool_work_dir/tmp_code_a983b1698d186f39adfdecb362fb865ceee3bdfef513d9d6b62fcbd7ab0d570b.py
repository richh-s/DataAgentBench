code = """import json, re
# load the previous query result file
path = var_call_xhRDJHqwELeVcsgzPfTbCiAa
with open(path, 'r') as f:
    data = json.load(f)

# filter entries for non-binary swift files
swift_entries = [e for e in data if isinstance(e.get('sample_path'), str) and e.get('sample_path').lower().endswith('.swift') and 'binary' not in (e.get('repo_data_description') or '').lower()]

def extract_copies(desc):
    if not desc:
        return 0
    desc = desc.lower()
    # common patterns: 'duplicated 8 times', 'appearing 8 times', 'copied 12 times', 'repeated 11 times', 'appearing 12 times'
    m = re.search(r'(\d+)\s*(?:times|time|copies|copied|duplicated|appearing|repeated)', desc)
    if m:
        return int(m.group(1))
    # fallback: find first number
    m2 = re.search(r'(\d+)', desc)
    return int(m2.group(1)) if m2 else 0

for e in swift_entries:
    e['copies'] = extract_copies(e.get('repo_data_description',''))

if not swift_entries:
    result = {'top_id': None, 'copies': 0, 'sample_path': None, 'repos': []}
else:
    # group by id to aggregate distinct repos
    by_id = {}
    for e in swift_entries:
        id_ = e['id']
        by_id.setdefault(id_, {'copies': e['copies'], 'sample_path': e.get('sample_path'), 'repos': set()})
        by_id[id_]['repos'].add(e.get('sample_repo_name'))
    # find id with max copies
    top_id, info = max(by_id.items(), key=lambda kv: kv[1]['copies'])
    result = {'top_id': top_id, 'copies': info['copies'], 'sample_path': info.get('sample_path'), 'repos': sorted(list(info['repos']))}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_toTC6KDKwNk42hcdjc4t3bFS': [], 'var_call_FjbKIl0m9cUPF1p8ZfAC8Mf3': [], 'var_call_xhRDJHqwELeVcsgzPfTbCiAa': 'file_storage/call_xhRDJHqwELeVcsgzPfTbCiAa.json'}

exec(code, env_args)
