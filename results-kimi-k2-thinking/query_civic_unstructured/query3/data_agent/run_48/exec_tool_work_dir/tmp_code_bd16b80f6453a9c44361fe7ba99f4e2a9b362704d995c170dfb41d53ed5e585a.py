code = """import json

f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(c_path, 'r') as f:
    civic = json.load(f)

fema = []
for rec in funding:
    n = rec['Project_Name']
    if 'FEMA' in n or 'fema' in n or 'emergency' in n.lower():
        fema.append({
            'Project_Name': n,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

status_data = []
for doc in civic:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low = line.lower()
            if 'project' in low or 'repairs' in low or 'sirens' in low:
                st = None
                for j in range(i+1, min(i+4, len(lines))):
                    nxt = lines[j].lower()
                    if 'design' in nxt:
                        st = 'design'
                        break
                    elif 'completed' in nxt:
                        st = 'completed'
                        break
                    elif 'not started' in nxt:
                        st = 'not started'
                        break
                if st:
                    status_data.append({'name': line, 'status': st})

results = []
for proj in fema:
    current_status = 'Unknown'
    for s in status_data:
        if proj['Project_Name'].lower() in s['name'].lower() or s['name'].lower() in proj['Project_Name'].lower():
            current_status = s['status']
            break
    
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': current_status
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
