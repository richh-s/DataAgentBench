code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

civic_docs = load_records(var_call_EO4v1yp3Uj7WyrQzaRGJbxtD)
funding = load_records(var_call_LbdE6UW2GnuMIdmVDJSZoy3B)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

projects = []
for doc in civic_docs:
    t = (doc.get('text') or '').replace('\r','')
    lines = [ln.strip() for ln in t.split('\n')]
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if line and len(line) < 120 and not re.search(r'(Projects\b|Agenda|^Page\s+\d|^Item\b|Recommended Action|DISCUSSION|^To:|Prepared by:|Subject:|Updates:|Project Schedule)', line, re.I):
            window = "\n".join(lines[i:i+35])
            if re.search(r'Project Schedule', window, re.I):
                st = None
                for pat in [r'Begin Construction\s*:\s*([^\n]+)', r'Begin\s+Construction\s*:\s*([^\n]+)', r'Begin\s+Design\s*:\s*([^\n]+)', r'Start\s+Construction\s*:\s*([^\n]+)']:
                    mm = re.search(pat, window, re.I)
                    if mm:
                        st = mm.group(1).strip()
                        break
                projects.append({'Project_Name': line, 'st': st, 'filename': doc.get('filename')})
                i += 5
                continue
        i += 1

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','st'])

spring_months = ['march','april','may']

def is_spring_2022(st):
    if st is None:
        return False
    s = str(st).strip().lower()
    if '2022' not in s:
        return False
    if 'spring' in s:
        return True
    for m in spring_months:
        if m in s:
            return True
    if re.search(r'2022[-/](0?3|0?4|0?5)\b', s):
        return True
    return False

spring_df = proj_df[proj_df['st'].apply(is_spring_2022)].copy()
spring_df['funding'] = spring_df['Project_Name'].map(fund_map).fillna(0).astype(int)

count_projects = int(spring_df['Project_Name'].nunique())
total_funding = int(spring_df.drop_duplicates(subset=['Project_Name'])['funding'].sum())

out = {'projects_started_spring_2022': count_projects, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EO4v1yp3Uj7WyrQzaRGJbxtD': 'file_storage/call_EO4v1yp3Uj7WyrQzaRGJbxtD.json', 'var_call_LbdE6UW2GnuMIdmVDJSZoy3B': 'file_storage/call_LbdE6UW2GnuMIdmVDJSZoy3B.json'}

exec(code, env_args)
