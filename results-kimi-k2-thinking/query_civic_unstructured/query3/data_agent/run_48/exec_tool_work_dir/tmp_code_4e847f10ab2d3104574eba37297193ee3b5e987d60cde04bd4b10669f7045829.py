code = """import json

funding_data = json.loads(open(locals()['var_functions.query_db:2']).read())
civic_docs = json.loads(open(locals()['var_functions.query_db:0']).read())

fema_projects = []
for r in funding_data:
    n = r.get('Project_Name', '')
    nl = n.lower()
    if 'fema' in nl or 'emergency' in nl:
        fema_projects.append({
            'Project_Name': n,
            'Funding_Source': r.get('Funding_Source', ''),
            'Amount': int(r.get('Amount', 0))
        })

project_status = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low = line.lower()
            if any(kw in low for kw in ['project', 'repairs', 'sirens', 'warning']):
                st = None
                for j in range(i+1, min(i+4, len(lines))):
                    nxt = lines[j].lower()
                    if 'design' in nxt:
                        st = 'design'
                        break
                    elif 'completed' in nxt or 'completion' in nxt:
                        st = 'completed'
                        break
                    elif 'not started' in nxt:
                        st = 'not started'
                        break
                if st:
                    project_status.append({'name': line, 'status': st})

results = []
for proj in fema_projects:
    status_match = 'Unknown'
    for ps in project_status:
        if proj['Project_Name'].lower() in ps['name'].lower() or ps['name'].lower() in proj['Project_Name'].lower():
            status_match = ps['status']
            break
    
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status_match
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
