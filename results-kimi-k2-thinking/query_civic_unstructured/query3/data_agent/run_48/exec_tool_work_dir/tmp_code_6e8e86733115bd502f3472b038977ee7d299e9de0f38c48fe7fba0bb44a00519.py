code = """import json, os
f=open(locals()['var_functions.query_db:2']);data1=json.load(f);f.close()
f=open(locals()['var_functions.query_db:0']);data2=json.load(f);f.close()

fema=[]
for r in data1:
    n=r['Project_Name']
    if 'FEMA' in n or 'fema' in n or 'emergency' in n.lower():
        fema.append({'Project_Name':n,'Funding_Source':r['Funding_Source'],'Amount':int(r['Amount'])})

status=[]
for d in data2:
    txt=d.get('text','')
    lines=txt.split('\n')
    for i in range(len(lines)):
        line=lines[i].strip()
        if len(line)>10 and ('project' in line.lower() or 'repairs' in line.lower() or 'sirens' in line.lower()):
            st=None
            for j in range(i+1,min(i+4,len(lines))):
                nxt=lines[j].lower()
                if 'design' in nxt:st='design';break
                elif 'completed' in nxt:st='completed';break
                elif 'not started' in nxt:st='not started';break
            if st:status.append({'name':line,'status':st})

res=[]
for p in fema:
    s='Unknown'
    for st in status:
        if p['Project_Name'].lower() in st['name'].lower() or st['name'].lower() in p['Project_Name'].lower():
            s=st['status'];break
    res.append({'Project_Name':p['Project_Name'],'Funding_Source':p['Funding_Source'],'Amount':p['Amount'],'Status':s})

print('__RESULT__:')
print(json.dumps(res,indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
