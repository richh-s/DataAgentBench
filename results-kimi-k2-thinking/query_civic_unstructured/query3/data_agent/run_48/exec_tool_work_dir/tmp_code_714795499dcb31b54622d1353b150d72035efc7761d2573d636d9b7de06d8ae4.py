code = """import json

funding_data = json.loads(open(locals()['var_functions.query_db:2']).read())
civic_docs = json.loads(open(locals()['var_functions.query_db:0']).read())

fema_list = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    check_name = name.lower()
    if 'fema' in check_name or 'emergency' in check_name:
        fema_list.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

status_data = []
for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        low = line.lower()
        keywords = ['project', 'repairs', 'sirens', 'warning', 'drainage']
        has_keyword = False
        for kw in keywords:
            if kw in low:
                has_keyword = True
                break
        
        if has_keyword:
            st = None
            for j in range(i+1, min(i+5, len(lines))):
                nxt = lines[j].lower()
                if 'design' in nxt and 'committee' not in nxt:
                    st = 'design'
                    break
                elif 'completed' in nxt or 'completion' in nxt:
                    st = 'completed'
                    break
                elif 'not started' in nxt:
                    st = 'not started'
                    break
            if st:
                status_data.append({'name': line, 'status': st})

output_list = []
for proj in fema_list:
    matched = 'Unknown'
    pname_lower = proj['Project_Name'].lower()
    
    for s in status_data:
        sname_lower = s['name'].lower()
        if pname_lower in sname_lower or sname_lower in pname_lower:
            matched = s['status']
            break
    
    output_list.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': matched
    })

print('__RESULT__:')
print(json.dumps(output_list, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
