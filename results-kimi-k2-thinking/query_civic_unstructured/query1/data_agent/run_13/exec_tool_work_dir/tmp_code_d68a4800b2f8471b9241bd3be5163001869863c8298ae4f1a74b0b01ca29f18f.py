code = """import json

funding_path = var_functions.query_db:64
civic_path = var_functions.query_db:54

with open(funding_path) as f:
    f_data = json.load(f)

with open(civic_path) as f:
    c_data = json.load(f)

f_names = [r['Project_Name'] for r in f_data]

design_projects = []

# Extract design project names from the first document
text = c_data[0]['text'].lower()

# Find design section
start = text.find('capital improvement projects (design)')
if start != -1:
    end = text.find('capital improvement projects (construction)', start)
    if end == -1:
        end = text.find('capital improvement projects (not started)', start)
    if end == -1:
        end = text.find('disaster recovery projects', start)
    if end == -1:
        end = len(text)
    
    section = text[start:end]
    lines = section.split('\n')
    
    for line in lines:
        clean_line = line.strip()
        if not clean_line or len(clean_line) < 10:
            continue
        
        lower_line = clean_line.lower()
        
        # Skip status/update lines based on keywords
        skip = False
        for keyword in ['updates:', 'schedule:', 'advertise:', 'staff', 'city', 'project is', 'prepared', 'approved']:
            if keyword in lower_line:
                skip = True
                break
        
        if skip:
            continue
        
        if '(cid' in lower_line or clean_line.startswith('('):
            continue
        
        if clean_line.startswith('to:') or clean_line.startswith('date') or clean_line.startswith('meeting'):
            continue
        
        # Skip lines with 4-digit years
        import re
        if re.search(r'\d{4}', lower_line) and len(clean_line.split()) <= 4:
            continue
        
        project_name = clean_line.strip().title()
        if project_name and project_name not in design_projects:
            design_projects.append(project_name)

# Match with funding data
matched = []
for design in design_projects:
    design_clean = design.lower().split('(')[0].strip()
    for fund in f_names:
        fund_clean = fund.lower().split('(')[0].strip()
        if design_clean == fund_clean:
            if design not in matched:
                matched.append(design)
                break

result = len(matched)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
