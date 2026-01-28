code = """import json, re
import pandas as pd
from pathlib import Path

path = var_call_IAjEG38NPHV2k30GgeyImnc8
records = json.loads(Path(path).read_text())

pattern = re.compile(r"\n(?P<name>.+?)\n\n\(cid:190\) Updates:.*?Construction was completed[^\n]*?(?P<when>2022)[^\n]*", re.IGNORECASE|re.DOTALL)
projects=[]
for r in records:
    txt=r.get('text','')
    for m in pattern.finditer(txt):
        name=m.group('name').strip()
        projects.append(name)

# also capture lines like 'Construction was completed November 2022' without preceding Updates label exactly
pattern2 = re.compile(r"\n(?P<name>[A-Za-z0-9][^\n]{2,200}?)\n\(cid:190\) Updates:\s*Construction was completed[^\n]*2022", re.IGNORECASE)
for r in records:
    txt=r.get('text','')
    for m in pattern2.finditer(txt):
        projects.append(m.group('name').strip())

projects = sorted(set(projects))
# park-related filter
park_projects=[p for p in projects if re.search(r"park|playground|bluffs|bluff|trancas|shade structure", p, re.IGNORECASE)]

print('__RESULT__:')
print(json.dumps({'completed_2022_projects':projects,'park_related_completed_2022_projects':park_projects}))"""

env_args = {'var_call_MOZsNnIPPWYP1qoseOtLs0aQ': ['Funding'], 'var_call_HoQHAK2gY25prZMY2Nx6G8gf': ['civic_docs'], 'var_call_IAjEG38NPHV2k30GgeyImnc8': 'file_storage/call_IAjEG38NPHV2k30GgeyImnc8.json'}

exec(code, env_args)
