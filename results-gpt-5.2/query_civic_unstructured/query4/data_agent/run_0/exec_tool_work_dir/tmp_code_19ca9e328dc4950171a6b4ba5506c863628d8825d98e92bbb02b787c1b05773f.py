code = """import json, re
import pandas as pd

path = var_call_0IOfBTuzQ6xbjdLixQphJanm
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
for d in docs:
    text = (d.get('text','') or '').replace('\r','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if (not ln) or (len(ln) > 120):
            continue
        low = ln.lower()
        if low in {
            'capital improvement projects (design)',
            'capital improvement projects (construction)',
            'capital improvement projects (not started)',
            'disaster recovery projects (design)',
            'disaster recovery projects (construction)',
            'disaster recovery projects (not started)'
        }:
            continue
        window = ' '.join(lines[i:i+8]).lower()
        if ('updates' in window) and (('project schedule' in window) or ('estimated schedule' in window)):
            name = ln
            chunk = ' '.join(lines[i:i+120])
            m = re.search(r'Begin\s+Construction\s*:\s*([^\n]+?)(?=\s{2,}|\s[A-Z][a-z]+\s\d{4}|$)', chunk, flags=re.IGNORECASE)
            if m:
                start = m.group(1).strip()
                projects.append({'Project_Name': name, 'start_raw': start, 'filename': d.get('filename')})

df = pd.DataFrame(projects)
if df.empty:
    out = {'project_names': [], 'n_projects': 0}
else:
    df = df.drop_duplicates(subset=['Project_Name'], keep='first')
    mask = df['start_raw'].str.contains(r'\bSpring\b\s*,?\s*2022\b', case=False, regex=True, na=False)
    proj_names = df.loc[mask, 'Project_Name'].tolist()
    out = {'project_names': proj_names, 'n_projects': int(len(proj_names))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cIwF1DzZYyGVbJgRQXIZE4Sd': ['Funding'], 'var_call_38K6ah1O9g5pFFoNyAINarzm': ['civic_docs'], 'var_call_0IOfBTuzQ6xbjdLixQphJanm': 'file_storage/call_0IOfBTuzQ6xbjdLixQphJanm.json'}

exec(code, env_args)
