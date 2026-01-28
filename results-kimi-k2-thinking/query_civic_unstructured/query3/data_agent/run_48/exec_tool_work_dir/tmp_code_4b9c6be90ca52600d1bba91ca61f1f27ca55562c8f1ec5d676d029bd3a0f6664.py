code = """import json

fpath = locals()['var_functions.query_db:2']
cpath = locals()['var_functions.query_db:0']

fdata = json.loads(open(fpath).read())
cdata = json.loads(open(cpath).read())

fema = []
for rec in fdata:
    n = rec['Project_Name'].lower()
    if 'fema' in n or 'emergency' in n:
        fema.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

all_status = []
for doc in cdata:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low = line.lower()
            if 'project' in low or 'repairs' in low or 'sirens' in low or 'warning' in low:
                st = None
                for j in range(i+1, min(i+4, len(lines))):
                    nxt = lines[j].lower()
                    if 'design' in nxt:
                        st = 'design'
                        break
                    if 'completed' in nxt or 'completion' in nxt:
                        st = 'completed'
                        break
                    if 'not started' in nxt:
                        st = 'not started'
                        break
                if st:
                    all_status.append({'name': line, 'status': st})

results = []
for p in fema:
    s = 'Unknown'
    for status in all_status:
        p_low = p['Project_Name'].lower()
        n_low = status['name'].lower()
        if p_low in n_low or n_low in p_low:
            s = status['status']
            break
    results.append({'Project_Name': p['Project_Name'], 'Funding_Source': p['Funding_Source'], 'Amount': p['Amount'], 'Status': s})

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
