code = """import json
# var_call_B3cqelzDZtIesXQcbZXEcDSc is provided by previous query_db call and contains a file path
p = var_call_B3cqelzDZtIesXQcbZXEcDSc
with open(p, 'r', encoding='utf-8') as f:
    records = json.load(f)

selected = []
for r in records:
    title = (r.get('title') or '').lower()
    artist = (r.get('artist') or '').lower()
    # heuristics for matching 'Street Hype' by Brucqe/ Bruce Maginnis
    if 'street hype' in title or 'streeth ype' in title or 'streethype' in title or 'sttreet hype' in title or '011-street hype' in title:
        selected.append(int(r['track_id']))
        continue
    if 'maginnis' in artist and 'street' in title:
        selected.append(int(r['track_id']))
        continue
    if 'brucqe' in artist and 'street' in title:
        selected.append(int(r['track_id']))
        continue
    # also catch cases where title contains 'street' and artist contains 'bruce' (typo)
    if 'bruce' in artist and 'street' in title:
        selected.append(int(r['track_id']))

# unique
selected = sorted(list(set(selected)))

print('__RESULT__:')
print(json.dumps(selected))"""

env_args = {'var_call_B3cqelzDZtIesXQcbZXEcDSc': 'file_storage/call_B3cqelzDZtIesXQcbZXEcDSc.json'}

exec(code, env_args)
