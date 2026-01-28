code = """import json
with open(var_call_w5WiviLNuqM8uC0FZH8mDfoo,'r',encoding='utf-8') as f:
    civic_docs=json.load(f)
with open(var_call_2shR4Lt5stCYfxsgZWUvQECb,'r',encoding='utf-8') as f:
    funding=json.load(f)
pk=['park','playground','walkway','bluffs','bench','benches','playground']
extracted=set()
for doc in civic_docs:
    lines=[ln.strip() for ln in doc.get('text','').splitlines()]
    for i,ln in enumerate(lines):
        low=ln.lower()
        if '2022' in low and 'completed' in low:
            # look up to 6 lines above for a line with park keyword
            for j in range(max(0,i-6),i+1):
                l2=lines[j]
                if any(k in l2.lower() for k in pk):
                    extracted.add(l2)
                    break
        if any(k in low for k in pk) and '2022' in low and 'completed' in low:
            extracted.add(ln)

projects=[p for p in sorted(extracted) if len(p)>3]
matched=[]
for fr in funding:
    name=fr.get('Project_Name','')
    nl=name.lower()
    for proj in projects:
        pl=proj.lower()
        if pl==nl or pl in nl or nl in pl:
            try:
                amt=int(str(fr.get('Amount','0')).replace(',',''))
            except:
                try:
                    amt=int(float(fr.get('Amount','0')))
                except:
                    amt=0
            matched.append({'project_doc_name':proj,'funding_project_name':name,'amount':amt})

total=sum(m['amount'] for m in matched)
print('__RESULT__:')
print(json.dumps({'projects':projects,'matched':matched,'total':total}))"""

env_args = {'var_call_w5WiviLNuqM8uC0FZH8mDfoo': 'file_storage/call_w5WiviLNuqM8uC0FZH8mDfoo.json', 'var_call_2shR4Lt5stCYfxsgZWUvQECb': 'file_storage/call_2shR4Lt5stCYfxsgZWUvQECb.json', 'var_call_UQeZLuXO6HMfdozF8MGZJz3e': {'civic_docs_count': 19, 'funding_records_count': 500}}

exec(code, env_args)
