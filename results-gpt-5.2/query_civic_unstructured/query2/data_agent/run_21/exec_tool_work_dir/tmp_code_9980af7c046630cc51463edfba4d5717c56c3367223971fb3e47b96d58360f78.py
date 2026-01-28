code = """import json, re
import pandas as pd

path_docs = var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def norm_status(s):
    s=s.strip().lower()
    return s

projects=[]
for d in docs:
    lines=[ln.strip() for ln in d.get('text','').splitlines()]
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
                projects.append({'Project_Name':ln,'status':current_status,'context':' '.join(lines[i:i+18]),'filename':d.get('filename')})

proj_df=pd.DataFrame(projects)
print('__RESULT__:')
print(json.dumps({'rows':int(len(proj_df)),'cols':list(proj_df.columns),'head':proj_df.head(5).to_dict(orient='records')}))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json', 'var_call_9wzPbJn4pIo9IAPXQeBcNCYw': {'doc_count': 19, 'sample_keys': ['filename', 'text']}}

exec(code, env_args)
