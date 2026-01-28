code = """import json

# Read the data files
with open('var_functions.query_db:0', 'r') as f:
    civic_docs_data = json.load(f)

with open('var_functions.query_db:1', 'r') as f:
    funding_data = json.load(f)

# Extract projects from civic documents
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for capital improvement projects in design phase
    if 'Capital Improvement Projects' in text:
        # Extract the design section
        design_start = text.find('Capital Improvement Projects (Design)')
        if design_start > 0:
            # Find where the design section ends
            construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
            design_section = text[design_start:construction_start if construction_start > 0 else None]
            
            lines = design_section.split('\n')
            
            for line in lines:
                line = line.strip()
                
                # Skip empty and obviously non-project lines
                if not line or line.startswith('•') or line.startswith('('):
                    continue
                if 'Page' in line or 'cid:' in line:
                    continue
                if 'Updates:' in line or 'Schedule:' in line:
                    continue
                if line.isupper() and len(line) < 50:
                    continue
                if len(line) < 10 or len(line) > 150:
                    continue
                    
                project_name = line.strip()
                # Clean name
                if project_name.endswith(':'):
                    project_name = project_name[:-1].strip()
                    
                # Skip duplicates and common phrases
                if (project_name and project_name not in [p['Project_Name'] for p in projects] and
                    project_name[0].isalnum() and
                    project_name.lower() not in ['updates', 'project schedule', 'estimated schedule']):
                    projects.append({
                        'Project_Name': project_name,
                        'status': 'design',
                        'type': 'capital'
                    })

# Remove duplicates
seen = set()
unique_projects = []
for p in projects:
    if p['Project_Name'] not in seen:
        seen.add(p['Project_Name'])
        unique_projects.append(p)
projects = unique_projects

# Create funding lookup
funding_dict = {}
for item in funding_data:
    try:
        amount = int(str(item['Amount']).replace(',', ''))
        funding_dict[item['Project_Name']] = amount
    except:
        continue

# Match projects with funding > $50,000
matched_projects = []
for project in projects:
    proj_name = project['Project_Name']
    if proj_name in funding_dict and funding_dict[proj_name] > 50000:
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding': funding_dict[proj_name]
        })

print('__RESULT__:')
print(json.dumps({'count': len(matched_projects), 'sample_projects': matched_projects[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
