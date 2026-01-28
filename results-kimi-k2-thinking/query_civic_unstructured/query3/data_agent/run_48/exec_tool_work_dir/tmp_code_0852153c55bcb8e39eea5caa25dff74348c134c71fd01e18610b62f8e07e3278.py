code = """import json

fpath = locals()['var_functions.query_db:2']
cpath = locals()['var_functions.query_db:0']

fdata = json.load(open(fpath))
cdata = json.load(open(cpath))

fema = []
for rec in fdata:
    n = rec['Project_Name']
    nl = n.lower()
    if 'fema' in nl or 'emergency' in nl:
        fema.append({
            'Project_Name': n,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

status_entries = []
for doc in cdata:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low_line = line.lower()
            has_kw = False
            for kw in ['project', 'repairs', 'sirens', 'warning']:
                if kw in low_line:
                    has_kw = True
                    break
            if has_kw:
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
                    status_entries.append({'name': line, 'status': st})

final_results = []
for proj in fema:
    s = 'Unknown'
    proj_lower = proj['Project_Name'].lower()
    for se in status_entries:
        se_lower = se['name'].lower()
        if proj_lower in se_lower or se_lower in proj_lower:
            s = se['status']
            break
    final_results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': s
    })

output = json.dumps(final_results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
