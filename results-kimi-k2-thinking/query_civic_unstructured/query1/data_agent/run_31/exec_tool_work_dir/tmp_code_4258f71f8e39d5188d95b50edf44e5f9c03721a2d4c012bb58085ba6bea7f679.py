code = """import json
f1=var_functions.query_db:2
f2=var_functions.query_db:5
with open(f1) as f:
    funding=json.load(f)
with open(f2) as f:
    civic=json.load(f)
funding_names=[]
for rec in funding:
    if int(rec['Amount'])>50000:
        funding_names.append(rec['Project_Name'])
design_projects=[]
for doc in civic:
    if 'text' in doc:
        text=doc['text']
        if 'Capital' in text and 'Design' in text:
            for line in text.split('\n'):
                line=line.strip()
                if line and len(line)>8 and len(line)<60:
                    lower=line.lower()
                    if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower:
                        design_projects.append(line)
unique_design=list(set(design_projects))
matched=0
for proj in unique_design:
    for fund in funding_names:
        if proj.lower().replace(' ','') in fund.lower().replace(' ','') or fund.lower().replace(' ','') in proj.lower().replace(' ',''):
            matched+=1
            break
print('__RESULT__:')
print(json.dumps({'count':matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
