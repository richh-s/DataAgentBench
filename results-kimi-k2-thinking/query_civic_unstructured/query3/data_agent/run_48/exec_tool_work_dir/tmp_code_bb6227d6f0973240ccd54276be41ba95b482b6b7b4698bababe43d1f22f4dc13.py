code = """import json, os

# Load data directly from files
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:0']

funding_list = []
civic_list = []

with open(funding_file, 'r') as f:
    funding_list = json.load(f)
with open(civic_file, 'r') as f:
    civic_list = json.load(f)

print('Loaded:', len(funding_list), 'funding records,', len(civic_list), 'civic documents')

# Get FEMA/emergency projects
fema_emergency = []
for rec in funding_list:
    project_name = rec['Project_Name']
    check_name = project_name.lower()
    if 'fema' in check_name or 'emergency' in check_name:
        fema_emergency.append({
            'Project_Name': project_name,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

print('Found', len(fema_emergency), 'FEMA/emergency projects')

# Extract status from docs
status_extracted = []
for doc in civic_list:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        low_line = line.lower()
        has_kw = False
        for kw in ['project', 'repairs', 'sirens', 'warning', 'drainage']:
            if kw in low_line:
                has_kw = True
                break
        
        if has_kw:
            proj_status = None
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'design' in next_line:
                    proj_status = 'design'
                    break
                elif 'completed' in next_line or 'completion' in next_line:
                    proj_status = 'completed'
                    break
                elif 'not started' in next_line:
                    proj_status = 'not started'
                    break
            
            if proj_status:
                status_extracted.append({'name': line, 'status': proj_status})

print('Extracted', len(status_extracted), 'project statuses')

# Match and compile results
final_results = []
for project in fema_emergency:
    matched_status = 'Unknown'
    project_lower = project['Project_Name'].lower()
    
    for status_item in status_extracted:
        item_lower = status_item['name'].lower()
        if project_lower in item_lower or item_lower in project_lower:
            matched_status = status_item['status']
            break
    
    final_results.append({
        'Project_Name': project['Project_Name'],
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': matched_status
    })

result_json = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
