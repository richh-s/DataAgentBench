code = """import json, re
path = var_call_xhRDJHqwELeVcsgzPfTbCiAa
with open(path, 'r') as f:
    data = json.load(f)

# identify non-binary swift files
swift_entries = []
for e in data:
    sp = e.get('sample_path')
    desc = (e.get('repo_data_description') or '').lower()
    if not isinstance(sp, str):
        continue
    if not sp.lower().endswith('.swift'):
        continue
    is_nonbinary = ('non-binary' in desc) or ('not binary' in desc) or ('binary' not in desc)
    if not is_nonbinary:
        continue
    swift_entries.append(e)

def extract_copies(desc):
    if not desc:
        return 0
    m = re.search(r'(\d+)\s*(?:times|time|copies|copied|duplicated|appearing|repeated)', desc)
    if m:
        return int(m.group(1))
    m2 = re.search(r'(\d+)', desc)
    return int(m2.group(1)) if m2 else 0

for e in swift_entries:
    e['copies'] = extract_copies((e.get('repo_data_description') or '').lower())

# aggregate by id
by_id = {}
for e in swift_entries:
    id_ = e['id']
    by_id.setdefault(id_, {'copies': 0, 'sample_path': e.get('sample_path'), 'repos': set()})
    # use copies as max observed copies
    by_id[id_]['copies'] = max(by_id[id_]['copies'], e.get('copies',0))
    by_id[id_]['repos'].add(e.get('sample_repo_name'))

if not by_id:
    result = {'top_id': None, 'copies': 0, 'sample_path': None, 'repos': []}
else:
    top_id, info = max(by_id.items(), key=lambda kv: kv[1]['copies'])
    result = {'top_id': top_id, 'copies': info['copies'], 'sample_path': info.get('sample_path'), 'repos': sorted(list(info['repos']))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_toTC6KDKwNk42hcdjc4t3bFS': [], 'var_call_FjbKIl0m9cUPF1p8ZfAC8Mf3': [], 'var_call_xhRDJHqwELeVcsgzPfTbCiAa': 'file_storage/call_xhRDJHqwELeVcsgzPfTbCiAa.json', 'var_call_6FxGvlKSQL8i9XltCcCxcjex': {'top_id': None, 'copies': 0, 'sample_path': None, 'repos': []}}

exec(code, env_args)
