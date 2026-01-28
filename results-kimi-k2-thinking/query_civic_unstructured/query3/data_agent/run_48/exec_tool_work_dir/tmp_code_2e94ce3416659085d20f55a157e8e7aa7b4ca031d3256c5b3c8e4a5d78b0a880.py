code = """import json

f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

funding = json.load(open(f_path))
docs = json.load(open(c_path))

fema_list = []
for rec in funding:
    name = rec['Project_Name']
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_list.append({
            'Project_Name': name,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

status_list = []
for doc in docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low_line = line.lower()
            if 'project' in low_line or 'repairs' in low_line or 'sirens' in low_line:
                s = None
                for j in range(i+1, min(i+4, len(lines))):
                    nxt = lines[j].lower()
                    if 'design' in nxt and 'committee' not in nxt:
                        s = 'design'
                        break
                    if 'completed' in nxt or 'completion' in nxt:
                        s = 'completed'
                        break
                    if 'not started' in nxt:
                        s = 'not started'
                        break
                if s:
                    status_list.append({'name': line, 'status': s})

results = []
for p in fema_list:
    matched = 'Unknown'
    for st in status_list:
        p_low = p['Project_Name'].lower()
        n_low = st['name'].lower()
        if p_low in n_low or n_low in p_low:
            matched = st['status']
            break
    results.append({'Project_Name': p['Project_Name'], 'Funding_Source': p['Funding_Source'], 'Amount': p['Amount'], 'Status': matched})

output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
