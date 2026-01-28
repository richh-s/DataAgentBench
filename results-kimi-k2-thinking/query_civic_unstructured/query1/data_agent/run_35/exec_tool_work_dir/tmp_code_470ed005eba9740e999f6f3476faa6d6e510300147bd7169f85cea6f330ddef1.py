code = """import json
import re

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
        lines = text.split('\n')
        in_design_section = False
        
        for line in lines:
            line = line.strip()
            
            # Check if we're entering the design section
            if 'Capital Improvement Projects (Design)' in line:
                in_design_section = True
                continue
                
            # Check if we're leaving the design section
            if in_design_section and ('Capital Improvement Projects (Construction)' in line or 
                                    'Capital Improvement Projects (Not Started)' in line):
                in_design_section = False
                continue
            
            # If we're in the design section, extract project names
            if in_design_section and line:
                # Skip common non-project lines
                skip_terms = ['•', 'Page', 'cid:', 'Updates:', 'Schedule:', 'To:', 'From:', 
                            'Subject:', 'Date', 'Prepared by', 'Approved by']
                if any(term in line for term in skip_terms):
                    continue
                    
                if line.isupper() and len(line) < 50:
                    continue
                    
                if len(line) < 10 or len(line) > 150:
                    continue
                    
                # Clean up project name
                project_name = line.strip()
                if project_name.endswith(':'):
                    project_name = project_name[:-1].strip()
                    
                # Skip common phrases
                if project_name.lower() in ['updates', 'project schedule', 'estimated schedule', 
                                          'recommended action', 'project description', 'discussion']:
                    continue
                    
                if project_name and project_name[0].isalnum():
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
        pass

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
print(json.dumps({'count': len(matched_projects), 'projects': matched_projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
