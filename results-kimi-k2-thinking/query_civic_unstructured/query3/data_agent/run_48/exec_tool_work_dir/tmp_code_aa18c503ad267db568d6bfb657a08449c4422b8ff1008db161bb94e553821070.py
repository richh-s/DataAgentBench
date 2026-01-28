code = """import json

f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

f_data = json.load(open(f_path))
c_data = json.load(open(c_path))

fema_projects = []
for rec in f_data:
    name = rec.get('Project_Name', '')
    lower_name = name.lower()
    if 'fema' in lower_name or 'emergency' in lower_name:
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

doc_status = []
for doc in c_data:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low_line = line.lower()
            has_kw = 'project' in low_line or 'repairs' in low_line or 'sirens' in low_line or 'warning' in low_line
            if has_kw:
                proj_status = None
                for j in range(i+1, min(i+4, len(lines))):
                    nxt = lines[j].lower()
                    design_found = 'design' in nxt
                    completed_found = 'completed' in nxt or 'completion' in nxt
                    notstarted_found = 'not started' in nxt
                    if design_found and 'committee' not in nxt:
                        proj_status = 'design'
                        break
                    if completed_found:
                        proj_status = 'completed'
                        break
                    if notstarted_found:
                        proj_status = 'not started'
                        break
                if proj_status:
                    doc_status.append({'name': line, 'status': proj_status})

final_list = []
for proj in fema_projects:
    current_status = 'Unknown'
    for ds in doc_status:
        proj_name_lower = proj['Project_Name'].lower()
        status_name_lower = ds['name'].lower()
        if proj_name_lower in status_name_lower or status_name_lower in proj_name_lower:
            current_status = ds['status']
            break
    final_list.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': current_status
    })

result_str = json.dumps(final_list, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
