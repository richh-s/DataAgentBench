code = """import json

funding_key = 'var_function-call-18362202212542543188'
civic_key = 'var_function-call-18362202212542543219'

funding_path = locals()[funding_key]
civic_path = locals()[civic_key]

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

projects_extracted = []
active_project = None
current_section = 'Unknown'

def save_project(proj, lst):
    if proj:
        proj['text'] = '\\n'.join(proj['text_lines'])
        del proj['text_lines']
        lst.append(proj)

for doc in civic_data:
    text = doc['text'].replace('\\r\\n', '\\n')
    lines = text.split('\\n')
    current_section = 'Unknown'
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        if 'Capital Improvement Projects (Design)' in line:
            new_sec = 'Design'
        elif 'Capital Improvement Projects (Construction)' in line:
            new_sec = 'Construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            new_sec = 'Not Started'
        elif 'Disaster Recovery Projects' in line:
            new_sec = 'Disaster'
        else:
            new_sec = current_section
            
        if new_sec != current_section:
            save_project(active_project, projects_extracted)
            active_project = None
            current_section = new_sec
            continue
            
        if line.startswith('(cid:190)') or line.startswith('(cid:131)') or line.startswith('Updates:') or line.startswith('Project Schedule:') or line.startswith('Project Description:') or line.startswith('Project Updates:'):
            if active_project:
                active_project['text_lines'].append(line)
            continue
            
        junk = ['Page ', 'Agenda Item', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']
        if any(x in line for x in junk):
            continue
            
        is_name = False
        for j in range(i + 1, min(i + 6, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if nl.startswith('(cid:190)'):
                is_name = True
                break
            else:
                break
        
        if is_name:
            save_project(active_project, projects_extracted)
            active_project = {
                'name': line,
                'section': current_section,
                'text_lines': []
            }
        else:
            if active_project:
                active_project['text_lines'].append(line)

    save_project(active_project, projects_extracted)
    active_project = None

results = []
keywords = ['emergency', 'fema', 'disaster', 'fire', 'warning', 'evacuation']

for fund in funding_data:
    f_name = fund['Project_Name']
    f_source = fund['Funding_Source']
    f_amount = fund['Amount']
    
    f_related = False
    for k in keywords:
        if k in f_name.lower():
            f_related = True
            break
            
    match = None
    f_name_clean = f_name.lower().strip()
    
    for p in projects_extracted:
        p_name_clean = p['name'].lower().strip()
        if p_name_clean == f_name_clean:
            match = p
            break
            
    if not match:
        for p in projects_extracted:
            p_name_clean = p['name'].lower().strip()
            if f_name_clean.startswith(p_name_clean) and len(p_name_clean) > 5:
                match = p
                break
                
    if not match:
        for p in projects_extracted:
            p_name_clean = p['name'].lower().strip()
            if p_name_clean.startswith(f_name_clean) and len(f_name_clean) > 5:
                match = p
                break

    if not match:
        # Check substrings
        for p in projects_extracted:
            p_name_clean = p['name'].lower().strip()
            if p_name_clean in f_name_clean and len(p_name_clean) > 10:
                match = p
                break
    
    status = 'Unknown'
    p_related = False
    
    if match:
        sec = match['section']
        txt = match['text'].lower()
        if sec == 'Design': status = 'design'
        elif sec == 'Not Started': status = 'not started'
        elif sec == 'Construction':
            if 'completed' in txt and 'notice of completion' in txt: status = 'completed'
            elif 'completed' in txt and 'construction was completed' in txt: status = 'completed'
            else: status = 'construction' # Keeping as extracted
        elif sec == 'Disaster':
            if 'completed' in txt: status = 'completed'
            elif 'design' in txt: status = 'design'
            elif 'construction' in txt: status = 'construction'
            
        full_text = match['name'] + ' ' + match['text']
        if any(k in full_text.lower() for k in keywords):
            p_related = True
            
    if f_related or p_related:
        results.append({
            'Project_Name': f_name,
            'Funding_Source': f_source,
            'Amount': f_amount,
            'Status': status
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-5064142693074181436': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-5064142693074180553': 'file_storage/function-call-5064142693074180553.json', 'var_function-call-18362202212542543188': 'file_storage/function-call-18362202212542543188.json', 'var_function-call-18362202212542543219': 'file_storage/function-call-18362202212542543219.json'}

exec(code, env_args)
