code = """import json

# Load funding data and civic documents
f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

funding_list = json.loads(open(f_path).read())
civic_list = json.loads(open(c_path).read())

# Find FEMA and emergency projects
fema_emergency_projects = []
for rec in funding_list:
    project_name = rec.get('Project_Name', '')
    if 'FEMA' in project_name or 'fema' in project_name or 'emergency' in project_name.lower():
        fema_emergency_projects.append({
            'Project_Name': project_name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

# Extract project status from civic documents
project_status_list = []
for doc in civic_list:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            line_lower = line.lower()
            # Check for project name patterns
            if any(kw in line_lower for kw in ['project', 'repairs', 'sirens', 'warning', 'drainage']):
                status = None
                for j in range(i+1, min(i+4, len(lines))):
                    next_line = lines[j].lower()
                    if 'design' in next_line and 'committee' not in next_line:
                        status = 'design'
                        break
                    elif 'completed' in next_line or 'completion' in next_line:
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                if status:
                    project_status_list.append({'name': line, 'status': status})

# Match and compile final results
final_output = []
for proj in fema_emergency_projects:
    current_status = 'Unknown'
    proj_name_lower = proj['Project_Name'].lower()
    
    for status_entry in project_status_list:
        entry_name_lower = status_entry['name'].lower()
        # Check for name match (partial match is acceptable)
        if proj_name_lower in entry_name_lower or entry_name_lower in proj_name_lower:
            current_status = status_entry['status']
            break
    
    final_output.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': current_status
    })

# Format and print result
result_json = json.dumps(final_output, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
