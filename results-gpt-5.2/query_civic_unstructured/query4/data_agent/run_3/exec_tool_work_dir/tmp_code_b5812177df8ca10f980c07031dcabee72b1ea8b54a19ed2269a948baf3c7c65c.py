code = """import json, re
import pandas as pd
from pathlib import Path

docs_var = var_call_NJuQuU8dAwc68QljUo19BomL
if isinstance(docs_var, str) and docs_var.endswith('.json'):
    docs = json.loads(Path(docs_var).read_text())
else:
    docs = docs_var

text_all = "\n\n".join(d.get('text','') for d in docs)
lines = text_all.splitlines()

records = []
current_project = None

begin_pat = re.compile(r'Begin\s+Construction\s*:\s*([A-Za-z]+\s*\d{4}|\d{4}-[A-Za-z]+|\d{4}-(?:Spring|Summer|Fall|Winter)|(?:Spring|Summer|Fall|Winter)\s*\d{4})', re.IGNORECASE)
start_pat = re.compile(r'\b(?:Start|Begin)\b[^:\n]{0,40}:\s*([A-Za-z]+\s*\d{4}|\d{4}-[A-Za-z]+|\d{4}-(?:Spring|Summer|Fall|Winter)|(?:Spring|Summer|Fall|Winter)\s*\d{4})', re.IGNORECASE)

section_headers = {
    'capital improvement projects (design)',
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'capital improvement projects',
    'disaster recovery projects',
    'disaster recovery projects (design)',
    'disaster recovery projects (construction)'
}

for ln in lines:
    s = ln.strip()
    if not s:
        continue
    if len(s) <= 120 and ':' not in s:
        sl = s.lower()
        if sl in section_headers:
            continue
        if 'project schedule' in sl or 'project description' in sl or 'updates' == sl:
            continue
        if 'page ' in sl or 'agenda item' in sl:
            continue
        current_project = s
    m = begin_pat.search(ln) or start_pat.search(ln)
    if m and current_project:
        records.append({'Project_Name': current_project, 'Start': m.group(1)})


def norm_season(s):
    s = s.strip().replace(',', ' ')
    s = re.sub(r'\s+', ' ', s)
    m = re.match(r'(\d{4})-(Spring|Summer|Fall|Winter)', s, re.IGNORECASE)
    if m:
        return f"{m.group(2).title()} {m.group(1)}"
    m = re.match(r'(Spring|Summer|Fall|Winter)\s*(\d{4})', s, re.IGNORECASE)
    if m:
        return f"{m.group(1).title()} {m.group(2)}"
    m = re.match(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s*(\d{4})', s, re.IGNORECASE)
    if m:
        month = m.group(1).lower()
        year = m.group(2)
        if month in ['march','april','may']:
            return f"Spring {year}"
        if month in ['june','july','august']:
            return f"Summer {year}"
        if month in ['september','october','november']:
            return f"Fall {year}"
        if month in ['december','january','february']:
            return f"Winter {year}"
    return s

if records:
    df = pd.DataFrame(records)
    df['Start_Norm'] = df['Start'].map(norm_season)
    spring2022 = df[df['Start_Norm'].str.lower().eq('spring 2022')]
    projects = sorted(spring2022['Project_Name'].dropna().unique().tolist())
else:
    projects = []

print('__RESULT__:')
print(json.dumps({'projects': projects, 'count': len(projects)}))"""

env_args = {'var_call_3PvoLb4aWAWEKtJBVZCC1wcP': ['Funding'], 'var_call_NJuQuU8dAwc68QljUo19BomL': 'file_storage/call_NJuQuU8dAwc68QljUo19BomL.json'}

exec(code, env_args)
