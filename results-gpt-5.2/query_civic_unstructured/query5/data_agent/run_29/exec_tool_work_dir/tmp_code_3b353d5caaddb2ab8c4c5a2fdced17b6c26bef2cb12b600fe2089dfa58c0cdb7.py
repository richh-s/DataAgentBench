code = """import json, re
import pandas as pd

funding_path = var_call_nHRMYqSVnORVdcf9fNlGp5zY
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

docs_path = var_call_ES96BvPmC6nu2gxnR5QnBRTK
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['total_amount'] = funding_df['total_amount'].astype(int)
funding_projects = set(funding_df['Project_Name'].tolist())

kw = re.compile(r"\b(FEMA|CalOES|CalJPIA|Disaster|Fire|Woolsey|Emergency)\b", re.I)
disaster_projects = sorted([p for p in funding_projects if kw.search(p)])

pattern_begin_2022 = re.compile(r"\b(Begin Construction|Start|Construction Start)\b.*\b2022\b", re.I | re.S)

started_2022 = set()
for p in disaster_projects:
    pat = re.compile(re.escape(p))
    for d in docs:
        text = d.get('text','') or ''
        for m in pat.finditer(text):
            start = max(0, m.start()-500)
            end = min(len(text), m.end()+800)
            window = text[start:end]
            if pattern_begin_2022.search(window):
                started_2022.add(p)
                break
        if p in started_2022:
            break

sel = funding_df[funding_df['Project_Name'].isin(started_2022)]

total = int(sel['total_amount'].sum())

out = {"total_funding": total, "project_count": int(len(started_2022)), "projects": sorted(started_2022)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nHRMYqSVnORVdcf9fNlGp5zY': 'file_storage/call_nHRMYqSVnORVdcf9fNlGp5zY.json', 'var_call_ES96BvPmC6nu2gxnR5QnBRTK': 'file_storage/call_ES96BvPmC6nu2gxnR5QnBRTK.json', 'var_call_bD0CMSEohTSzPUBNK2etoltd': ['Funding'], 'var_call_eFBAq1NpGU12CEd60t2iqiC1': ['civic_docs'], 'var_call_245QqTKSvC4CBZADdk3qP5ze': {'total_funding': 0, 'project_count': 0, 'projects': []}}

exec(code, env_args)
