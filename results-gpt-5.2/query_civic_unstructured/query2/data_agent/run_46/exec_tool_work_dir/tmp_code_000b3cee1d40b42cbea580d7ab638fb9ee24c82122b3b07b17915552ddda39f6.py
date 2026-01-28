code = """import json, re
from pathlib import Path

path = var_call_IAjEG38NPHV2k30GgeyImnc8
records = json.loads(Path(path).read_text())

projects=set()
pattern = re.compile(r'\n(?P<name>[^\n]{3,200}?)\n\(cid:190\) Updates:\s*(?:\(cid:131\)\s*)?Construction was completed[^\n]*2022', re.IGNORECASE)
for r in records:
    txt=r.get('text','')
    for m in pattern.finditer(txt):
        projects.add(m.group('name').strip())

projects = sorted(projects)
park_projects=[p for p in projects if re.search(r'park|playground|bluffs|shade structure', p, re.IGNORECASE)]

print('__RESULT__:')
print(json.dumps({'park_related_completed_2022_projects':park_projects,'all_completed_2022_projects':projects}))"""

env_args = {'var_call_MOZsNnIPPWYP1qoseOtLs0aQ': ['Funding'], 'var_call_HoQHAK2gY25prZMY2Nx6G8gf': ['civic_docs'], 'var_call_IAjEG38NPHV2k30GgeyImnc8': 'file_storage/call_IAjEG38NPHV2k30GgeyImnc8.json'}

exec(code, env_args)
