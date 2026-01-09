code = """import json, re
from pathlib import Path
import pandas as pd

fp = var_call_cgTL4d0JXxa77RARkUT45mZG
if isinstance(fp, str) and fp.endswith('.json'):
    docs = json.loads(Path(fp).read_text())
else:
    docs = fp

text_all = "\n\n".join(d.get('text','') for d in docs)
lines = text_all.splitlines()

records=[]
current=None

def looks_like_project(s):
    if not s or len(s)>140 or ':' in s: 
        return False
    sl=s.lower()
    bad_phrases=['capital improvement projects','disaster recovery projects','disaster projects','project schedule','project description','recommended action','discussion','updates','estimated schedule','page','agenda item']
    return not any(bp in sl for bp in bad_phrases)

begin_re = re.compile(r"Begin\s+(?:Construction|Design)\s*:\s*([^\n]+)", re.IGNORECASE)
award_begin_re = re.compile(r"Award\s+Contract\s+and\s+Begin\s+Construction\s*:\s*([^\n]+)", re.IGNORECASE)

for ln in lines:
    s=ln.strip()
    if looks_like_project(s):
        current=s
    m = award_begin_re.search(ln) or begin_re.search(ln)
    if m and current:
        date = m.group(1).strip()
        records.append({'Project_Name': current, 'Start_raw': date})

# normalize and detect spring 2022 presence

def is_spring2022(raw):
    r=raw.lower()
    # include spring 2022 and spring/summer 2022, spring of 2022
    if 'spring' in r and '2022' in r:
        return True
    # months mapping
    m = re.search(r"(march|april|may)\s+2022", r)
    return bool(m)

spring_projects = sorted({rec['Project_Name'] for rec in records if is_spring2022(rec['Start_raw'])})

print('__RESULT__:')
print(json.dumps({'projects': spring_projects, 'count': len(spring_projects)}))"""

env_args = {'var_call_3PvoLb4aWAWEKtJBVZCC1wcP': ['Funding'], 'var_call_NJuQuU8dAwc68QljUo19BomL': 'file_storage/call_NJuQuU8dAwc68QljUo19BomL.json', 'var_call_cgTL4d0JXxa77RARkUT45mZG': 'file_storage/call_cgTL4d0JXxa77RARkUT45mZG.json'}

exec(code, env_args)
