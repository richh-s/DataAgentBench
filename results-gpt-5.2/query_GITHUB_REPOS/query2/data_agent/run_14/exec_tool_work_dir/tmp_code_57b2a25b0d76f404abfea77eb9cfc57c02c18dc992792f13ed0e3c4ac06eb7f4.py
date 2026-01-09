code = """import json, re

# load swift contents rows
path = var_call_oiILXJk75Fv93HJ802x1zZWy
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

pat = re.compile(r'(?:duplicated|appears|appearing|copied)\s+([0-9]+)\s+times', re.I)

def copies(desc):
    if not desc:
        return None
    m = pat.search(desc)
    return int(m.group(1)) if m else None

best = None
for r in rows:
    # non-binary check
    desc = r.get('repo_data_description')
    if desc and 'non-binary' not in desc.lower():
        continue
    if desc and 'binary' in desc.lower() and 'non-binary' not in desc.lower():
        continue
    c = copies(desc)
    if c is None:
        continue
    if (best is None) or (c > best['copies']):
        best = {
            'id': r['id'],
            'repo': r['sample_repo_name'],
            'path': r['sample_path'],
            'copies': c,
            'desc': desc
        }

print('__RESULT__:')
print(json.dumps(best))"""

env_args = {'var_call_D2TdwPZWg1Wo2MzJ7HeDIhGZ': [], 'var_call_PgmM4zNeF4dhw2rSWmY3kQph': 'file_storage/call_PgmM4zNeF4dhw2rSWmY3kQph.json', 'var_call_yTJO9KML4b8xNXuoWNH3uqcl': [], 'var_call_p3eCX8eR7K13x6mgeIqqc40P': [{'n_swift': '1208'}], 'var_call_YxzEZgtp6Gjq6W5zwnuKOvX1': [{'n_swift_contents': '105'}], 'var_call_oiILXJk75Fv93HJ802x1zZWy': 'file_storage/call_oiILXJk75Fv93HJ802x1zZWy.json'}

exec(code, env_args)
