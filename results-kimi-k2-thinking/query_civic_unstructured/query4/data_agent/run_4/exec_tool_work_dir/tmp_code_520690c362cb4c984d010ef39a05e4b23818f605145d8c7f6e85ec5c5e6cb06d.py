code = """import json

# Load data from files
civic_docs = json.load(open(var_functions.query_db:2))
funding_recs = json.load(open(var_functions.query_db:4))

# Build funding map by project name
funding = {}
for r in funding_recs:
    name = r.get('Project_Name','')
    if name:
        funding[name] = int(r.get('Amount',0))

# Find projects that start in Spring 2022 and have funding
found = []
for doc in civic_docs:
    text = doc.get('text','')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 10 < len(line) < 150 and any(k in line for k in ['Project','Improvements','Repairs']):
                if not line.startswith('(') and line in funding:
                    if line not in [f['name'] for f in found]:
                        found.append({'name':line,'funding':funding[line]})
                elif not line.startswith('('):
                    for f_name in funding:
                        if line.lower() in f_name.lower() or f_name.lower() in line.lower():
                            if f_name not in [f['name'] for f in found]:
                                found.append({'name':f_name,'funding':funding[f_name]})
                            break

count = len(found)
total = sum(f['funding'] for f in found)

print('__RESULT__:')
print(json.dumps({'count':count,'total_funding':total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
