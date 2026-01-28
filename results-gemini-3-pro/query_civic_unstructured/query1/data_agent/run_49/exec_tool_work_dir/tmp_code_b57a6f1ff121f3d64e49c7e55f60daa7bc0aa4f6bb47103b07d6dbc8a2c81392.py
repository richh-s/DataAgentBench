code = """import json

# Load funding results
funding_file = locals()['var_function-call-12998690230637064644']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funded_projects = set()
for row in funding_data:
    if row.get('Project_Name'):
        funded_projects.add(row['Project_Name'].strip())

# Load civic docs
docs_file = locals()['var_function-call-12998690230637064277']
with open(docs_file, 'r') as f:
    docs_data = json.load(f)

design_projects = set()

for doc in docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    in_design_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect start of section
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            i += 1
            continue
            
        # Detect end of section
        if in_design_section:
            if 'Capital Improvement Projects (' in line and '(Design)' not in line:
                in_design_section = False
                break
            if 'Disaster Recovery Projects' in line:
                in_design_section = False
                break
                
            # Extract project name
            if line:
                is_project = False
                for k in range(1, 6):
                    if i + k < len(lines):
                        next_line = lines[i+k].strip()
                        # Check for Updates or Project Description
                        if 'Updates:' in next_line or 'Project Description:' in next_line or '(cid:190)' in next_line:
                            is_project = True
                            break
                
                if is_project:
                    if 'Page' not in line and 'Agenda' not in line:
                        design_projects.add(line)
        
        i += 1

# Intersect
matching_projects = []
for dp in design_projects:
    if dp in funded_projects:
        matching_projects.append(dp)

print('__RESULT__:')
print(json.dumps({
    'design_projects_found': list(design_projects),
    'matching_projects': matching_projects,
    'count': len(matching_projects)
}))"""

env_args = {'var_function-call-12998690230637064644': 'file_storage/function-call-12998690230637064644.json', 'var_function-call-12998690230637064277': 'file_storage/function-call-12998690230637064277.json'}

exec(code, env_args)
