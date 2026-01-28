code = """import json, re, pandas as pd
fund_path = var_call_WHrlzje0QOdM5LXX1osbzV3A
with open(fund_path,'r',encoding='utf-8') as f:
    funding=json.load(f)
fund_df=pd.DataFrame(funding)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'],errors='coerce').fillna(0).astype(int)
fund_names=set(fund_df['Project_Name'].tolist())

path=var_call_0CnqxWQsjqy2gwyNYQFjegOX
with open(path,'r',encoding='utf-8') as f:
    docs=json.load(f)

start_markers=[
    re.compile(r'\\bStart(?:ed)?\\b\\s*:?\\s*([A-Za-z0-9\\- ,/]+)',re.IGNORECASE),
    re.compile(r'\\bBegin\\s+Construction\\b\\s*:?\\s*([A-Za-z0-9\\- ,/]+)',re.IGNORECASE),
    re.compile(r'\\bBegin\\b\\s*:?\\s*(\\d{4}[A-Za-z0-9\\- ,/]*)',re.IGNORECASE),
]
related_kw=re.compile(r'FEMA|CalOES|CalJPIA|Woolsey|Fire|Disaster',re.IGNORECASE)

def find_started_2022_for_project(text,pname):
    idx=text.find(pname)
    if idx==-1:
        return False
    snippet=text[max(0,idx-400):idx+800]
    if (not related_kw.search(snippet)) and (not related_kw.search(pname)):
        return False
    for pat in start_markers:
        m=pat.search(snippet)
        if m and '2022' in m.group(1):
            return True
    if '2022' in snippet and re.search(r'Begin\\s+Construction',snippet,re.IGNORECASE):
        for m in re.finditer(r'Begin\\s+Construction[^\\n]{0,80}',snippet,flags=re.IGNORECASE):
            if '2022' in m.group(0):
                return True
    return False

started_2022_projects=set()
likely_names=[n for n in fund_names if related_kw.search(n)]

for d in docs:
    text=d.get('text','') or ''
    if '2022' not in text:
        continue
    for pname in likely_names:
        if pname in text and find_started_2022_for_project(text,pname):
            started_2022_projects.add(pname)

sel=fund_df[fund_df['Project_Name'].isin(started_2022_projects)]
ans=int(sel['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding':ans,'num_unique_projects':len(started_2022_projects),'projects':sorted(started_2022_projects)}))"""

env_args = {'var_call_WHrlzje0QOdM5LXX1osbzV3A': 'file_storage/call_WHrlzje0QOdM5LXX1osbzV3A.json', 'var_call_0CnqxWQsjqy2gwyNYQFjegOX': 'file_storage/call_0CnqxWQsjqy2gwyNYQFjegOX.json', 'var_call_NeiwFZNACJVkcMK3PXRvWo6A': {'total_funding': 0, 'num_projects': 0, 'projects': []}}

exec(code, env_args)
