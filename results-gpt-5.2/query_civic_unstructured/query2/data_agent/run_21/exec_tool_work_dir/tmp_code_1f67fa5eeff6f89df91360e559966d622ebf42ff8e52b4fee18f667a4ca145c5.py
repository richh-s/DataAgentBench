code = """import json, re
import pandas as pd

path_docs = var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def norm_status(s):
    s=s.strip().lower()
    if s=='design': return 'design'
    if s=='construction': return 'construction'
    if s=='not started': return 'not started'
    return s

projects=[]
for d in docs:
    text=d.get('text','')
    lines=[ln.strip() for ln in text.splitlines()]
    current_status=None
    for i,ln in enumerate(lines):
        m=re.search(r'\bCapital Improvement Projects\s*\((Design|Construction|Not Started)\)', ln, re.IGNORECASE)
        if m:
            current_status=norm_status(m.group(1))
            continue
        if current_status and ln and len(ln)<140:
            low=ln.lower()
            if low.startswith(('updates','project schedule','recommended action','discussion','page','agenda item','to:','prepared','approved','date prepared','meeting date','subject')):
                continue
            if re.search(r'\bprojects\b', ln, re.IGNORECASE):
                continue
            window=' '.join(lines[i+1:i+8]).lower()
            if ('updates' in window) or ('project schedule' in window) or ('project description' in window) or ('estimated schedule' in window):
                pname=ln
                win2=' '.join(lines[i:i+18])
                projects.append({'Project_Name':pname,'status':current_status,'context':win2,'filename':d.get('filename')})

proj_df=pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','status'])

park_mask = proj_df['Project_Name'].str.contains(r'park|playground|bluffs', case=False, na=False) | proj_df['context'].str.contains(r'\bpark\b|playground|bluffs', case=False, na=False)
proj_df=proj_df[park_mask].copy()

completed_2022 = proj_df['context'].str.contains(r'completed.*2022', case=False, na=False)
proj_df=proj_df[completed_2022].copy()

path_fund = var_call_tSW7bYfRh9pqlIqOF2V66jZM
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df=pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])

merged=proj_df.merge(fund_df, on='Project_Name', how='inner')
answer_total=int(merged['total_amount'].sum())

out={'total_funding': answer_total,
     'projects': merged[['Project_Name','total_amount','filename']].drop_duplicates().sort_values('Project_Name').to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json'}

exec(code, env_args)
