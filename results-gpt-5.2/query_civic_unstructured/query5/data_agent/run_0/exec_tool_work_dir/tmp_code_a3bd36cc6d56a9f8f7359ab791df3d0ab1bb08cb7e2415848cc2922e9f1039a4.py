code = """import json, re
from pathlib import Path
import pandas as pd

path = var_call_wi0kriPU676jmRWzLdlOfEUb
records = json.loads(Path(path).read_text())

projects = []
for rec in records:
    text = rec.get('text','')
    if not re.search(r'(?i)Disaster Recovery Projects', text):
        continue
    m = re.search(r'(?is)Disaster Recovery Projects.*?(?=\n\s*Capital Improvement Projects|\Z)', text)
    if not m:
        continue
    sec = m.group(0)
    lines = [ln.strip() for ln in sec.splitlines()]
    for i, ln in enumerate(lines):
        if not ln or len(ln) > 120:
            continue
        if 'disaster recovery projects' in ln.lower():
            continue
        if ln.lower().startswith(('(cid:', 'updates', 'project schedule', 'project description', 'recommended', 'discussion', 'page ')):
            continue
        if ln[0] in ['•','-']:
            continue
        window = '\n'.join(lines[i+1:i+8])
        if re.search(r'(?i)Updates|Project Schedule|Complete Design|Begin Construction|Advertise|Complete Construction', window):
            projects.append({'Project_Name': ln, 'context': sec})

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

starts = []
for _, row in proj_df.iterrows():
    pname = row['Project_Name']
    sec = row['context']
    idx = sec.lower().find(pname.lower())
    snippet = sec[idx: idx+800] if idx!=-1 else sec
    st = None
    patterns = [
        r'(?i)Start\s*:?\s*([A-Za-z0-9, \-]+\b20\d{2}[A-Za-z0-9, \-]*)',
        r'(?i)Begin\s+Construction\s*:?\s*([A-Za-z0-9, \-]+)',
        r'(?i)Begin\s*:?\s*([A-Za-z0-9, \-]+)'
    ]
    for pat in patterns:
        mm = re.search(pat, snippet)
        if mm:
            st = mm.group(1).strip()
            break
    if st is None:
        yrs = re.findall(r'(20\d{2})', snippet)
        if yrs:
            st = yrs[0]
    starts.append(st)

proj_df['st'] = starts
proj_2022 = proj_df[proj_df['st'].fillna('').str.contains('2022')]

result = {
    'disaster_projects_started_2022': proj_2022['Project_Name'].dropna().unique().tolist(),
    'count': int(proj_2022['Project_Name'].nunique())
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_a8hKK4f4Tr2ixmXpxBCjRL9U': ['Funding'], 'var_call_wXuCoPPr84FBUy6k2eaVpiC8': ['civic_docs'], 'var_call_wi0kriPU676jmRWzLdlOfEUb': 'file_storage/call_wi0kriPU676jmRWzLdlOfEUb.json'}

exec(code, env_args)
