code = """import json, re, pandas as pd

# load docs
with open(var_call_doDJq1s9rwUWUOVU3na3B1gf,'r',encoding='utf-8') as f:
    docs=json.load(f)

# load funding totals
with open(var_call_SGs0mH129VnZcNiI76ckFcuz,'r',encoding='utf-8') as f:
    fund=json.load(f)
fund_df=pd.DataFrame(fund)
fund_df['Total_Amount']=pd.to_numeric(fund_df['Total_Amount'],errors='coerce').fillna(0).astype(int)
fund_map=dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

start_pat=re.compile(r'Begin\s+(?:Construction|Design)\s*:\s*Spring\s*2022', re.I)
name_pat=re.compile(r'^[A-Z0-9][A-Za-z0-9\(\)\-\/,\&\s]{2,}$')

projects=set()
for d in docs:
    lines=[ln.strip() for ln in d.get('text','').splitlines()]
    idxs=[i for i,ln in enumerate(lines) if start_pat.search(ln)]
    for i in idxs:
        name=None
        for j in range(i-1, max(-1,i-120), -1):
            ln=lines[j]
            if not ln:
                continue
            if ln.startswith('(cid'):
                continue
            if 'Project Schedule' in ln or 'Estimated Schedule' in ln or 'Updates' in ln or 'Project Description' in ln:
                continue
            if ln.startswith(('Page','Agenda','Capital','Disaster','RECOMMENDED','DISCUSSION','To:','Prepared','Approved','Date prepared','Meeting date','Subject')):
                continue
            if name_pat.match(ln):
                if ln.lower() in {'project schedule','estimated schedule','updates','discussion','recommended action'}:
                    continue
                name=ln
                break
        if name:
            projects.add(name)

amounts={p:int(fund_map.get(p,0)) for p in sorted(projects)}

out={
  'spring_2022_started_projects_count': len(projects),
  'total_funding_usd': int(sum(amounts.values())),
  'matched_projects': [{'Project_Name':p,'Funding_USD':amounts[p]} for p in sorted(projects)]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XtEzw5AyTsnXaaX8ijHhlrwl': ['Funding'], 'var_call_rb6ikrCfiVg35rh8JoXlANJh': ['civic_docs'], 'var_call_doDJq1s9rwUWUOVU3na3B1gf': 'file_storage/call_doDJq1s9rwUWUOVU3na3B1gf.json', 'var_call_SGs0mH129VnZcNiI76ckFcuz': 'file_storage/call_SGs0mH129VnZcNiI76ckFcuz.json', 'var_call_Cf0GMiMWAxjQKqAOFkIfIzbA': {'spring_2022_started_projects_count': 0, 'total_funding_usd': 0, 'matched_projects': []}, 'var_call_WwdxDyhIKCquV7SLDSUB8gdq': [[50, '(cid:131) Begin Construction: Spring 2022'], [178, '(cid:131) Begin Construction: Spring 2022'], [327, '(cid:131) Begin Construction: Spring 2022'], [352, '(cid:131) Begin Construction: Spring 2022'], [363, '(cid:131) Begin Construction: Spring 2022']]}

exec(code, env_args)
