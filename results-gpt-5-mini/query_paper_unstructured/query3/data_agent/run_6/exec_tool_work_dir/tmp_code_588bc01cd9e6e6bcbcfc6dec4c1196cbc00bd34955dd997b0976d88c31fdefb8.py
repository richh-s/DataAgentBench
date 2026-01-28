code = """import json, re
path = var_call_h8CIT19siyAbgT4EYFNOWynA
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

out = []
for i, d in enumerate(docs[:20]):
    filename = d.get('filename')
    text = d.get('text','')
    years = re.findall(r"\b(?:19|20)\d{2}\b", text)
    emp = bool(re.search(r"empirical", text, re.I))
    out.append({'filename': filename, 'years_found': years[:5], 'empirical': emp})

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_h8CIT19siyAbgT4EYFNOWynA': 'file_storage/call_h8CIT19siyAbgT4EYFNOWynA.json', 'var_call_3dA7kX9PtJ8QLXwxTaRemCVm': []}

exec(code, env_args)
