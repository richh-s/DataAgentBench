code = """import json

funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:0']

funding_data = json.loads(open(funding_path).read())
civic_docs = json.loads(open(civic_path).read())

fema_emergency_projects = []
for record in funding_data:
    name = record['Project_Name']
    if ('FEMA' in name or 'fema' in name or 'emergency' in name.lower()):
        fema_emergency_projects.append({
            'Project_Name': name,
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount'])
        })

extracted_status = []
for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10 and ('project' in line.lower() or 'repairs' in line.lower() or 'sirens' in line.lower()):
            status = None
            for j in range(i+1, min(i+4, len(lines))):
                nxt_line = lines[j].lower()
                if 'design' in nxt_line:
                    status = 'design'
                    break
                elif 'completed' in nxt_line:
                    status = 'completed'
                    break
                elif 'not started' in nxt_line:
                    status = 'not started'
                    break
            if status:
                extracted_status.append({'name': line, 'status': status})

final_results = []
for proj in fema_emergency_projects:
    matched_status = 'Unknown'
    for st in extracted_status:
        proj_lower = proj['Project_Name'].lower()
        name_lower = st['name'].lower()
        if proj_lower in name_lower or name_lower in proj_lower:
            matched_status = st['status']
            break
    
    final_results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': matched_status
    })

output = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
