code = """import json

f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

with open(f_path, 'r') as f:
    funding_data = json.load(f)
with open(c_path, 'r') as f:
    civic_data = json.load(f)

fema_proj = []
for rec in funding_data:
    pname = rec.get('Project_Name', '')
    pcheck = pname.lower()
    if 'fema' in pcheck or 'emergency' in pcheck:
        fema_proj.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

document_status = []
for doc in civic_data:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            ln = line.lower()
            keywords = ['project', 'repairs', 'sirens', 'warning']
            has_keyword = False
            for kw in keywords:
                if kw in ln:
                    has_keyword = True
                    break
            if has_keyword:
                st = None
                for j in range(i+1, min(i+4, len(lines))):
                    nxt_ln = lines[j].lower()
                    if 'design' in nxt_ln:
                        st = 'design'
                        break
                    if 'completed' in nxt_ln or 'completion' in nxt_ln:
                        st = 'completed'
                        break
                    if 'not started' in nxt_ln:
                        st = 'not started'
                        break
                if st:
                    document_status.append({'name': line, 'status': st})

results = []
for proj in fema_proj:
    matched = 'Unknown'
    proj_lower = proj['Project_Name'].lower()
    for st in document_status:
        st_lower = st['name'].lower()
        if proj_lower in st_lower or st_lower in proj_lower:
            matched = st['status']
            break
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': matched
    })

output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
