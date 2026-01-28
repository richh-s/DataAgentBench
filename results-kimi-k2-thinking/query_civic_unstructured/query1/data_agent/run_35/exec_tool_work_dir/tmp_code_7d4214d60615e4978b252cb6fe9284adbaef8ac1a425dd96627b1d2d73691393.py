code = """import json

# Read the actual data from the files
civic_file_path = locals()['var_functions.query_db:0']
funding_file_path = locals()['var_functions.query_db:1']

with open(civic_file_path, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Now extract capital design projects from civic documents
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        # Find end of design section
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = text.find('Disaster Recovery Projects', design_start)
        if construction_start < 0:
            construction_start = len(text)
            
        design_section = text[design_start:construction_start]
        
        # Extract lines that look like project names
        for line in design_section.split('\n'):
            line = line.strip()
            
            # Heuristic: project names are typically 10-150 chars, not all caps, don't start with bullets
            if (len(line) >= 10 and len(line) <= 150 and 
                not line.isupper() and 
                not line.startswith('•') and 
                not line.startswith('(') and
                'Page' not in line and 'cid:' not in line and
                'Updates:' not in line and 'Schedule:' not in line and
                line[0].isalnum()):
                
                project_name = line.strip()
                if project_name.endswith(':'):
                    project_name = project_name[:-1].strip()
                
                # Avoid duplicates
                if not any(p['Project_Name'] == project_name for p in projects):
                    projects.append({
                        'Project_Name': project_name,
                        'status': 'design',
                        'type': 'capital'
                    })

# Create funding lookup
funding_dict = {}
for item in funding_data:
    try:
        amount = int(str(item['Amount']).replace(',', '').strip())
        funding_dict[item['Project_Name']] = amount
    except:
        pass

# Find capital design projects with funding > $50,000
matched_projects = []
for proj in projects:
    name = proj['Project_Name']
    if name in funding_dict and funding_dict[name] > 50000:
        matched_projects.append(name)

print('__RESULT__:')
print(json.dumps({'count': len(matched_projects), 'projects': matched_projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:14': {'available_variables': ['var_functions.query_db:0', 'var_functions.query_db:1', '__builtins__', 'json']}, 'var_functions.execute_python:18': {'civic_docs_length': 38, 'funding_length': 38, 'civic_docs_sample': 'fi'}, 'var_functions.execute_python:20': {'civic_var_type': "<class 'str'>", 'funding_var_type': "<class 'str'>", 'civic_var_preview': 'file_storage/functions.query_db:0.json', 'funding_var_preview': 'file_storage/functions.query_db:1.json'}}

exec(code, env_args)
