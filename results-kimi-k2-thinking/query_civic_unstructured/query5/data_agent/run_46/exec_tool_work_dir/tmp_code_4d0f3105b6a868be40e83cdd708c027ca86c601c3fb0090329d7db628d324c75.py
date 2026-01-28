code = """import json
import re

# Get the data from storage
civic_docs = locals()['var_functions.query_db:32']
funding_records = locals()['var_functions.query_db:2']

# Find disaster-related projects that mention 2022
disaster_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for lines that might be project names
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and very short lines
        if not line or len(line) < 5:
            continue
            
        # Check if line looks like a project name (starts with capital letters)
        if re.match(r'^[A-Z][a-zA-Z\s\-&]+', line):
            # Check if it's disaster-related
            has_fema = 'FEMA' in line
            has_caloes = 'CalOES' in line
            has_caljpia = 'CalJPIA' in line
            has_disaster = 'disaster' in text.lower()
            
            is_disaster = has_fema or has_caloes or has_caljpia
            
            # Also check if the document contains disaster indicators
            if not is_disaster and (has_disaster or 'CalOES' in text or 'CalJPIA' in text):
                # Check if project name suggests disaster work
                if 'storm' in line.lower() or 'drain' in line.lower() or 'road' in line.lower():
                    is_disaster = True
            
            if is_disaster:
                # Check if this project started in 2022
                if '2022' in line or '2022' in text[text.find(line):text.find(line)+500]:
                    # Clean up the project name
                    project_name = re.sub(r'\s*\(FEMA[^\)]*\)$', '', line).strip()
                    project_name = re.sub(r'\s*\(CalOES[^\)]*\)$', '', line).strip()
                    project_name = re.sub(r'\s*\(CalJPIA[^\)]*\)$', '', line).strip()
                    
                    if project_name and project_name not in disaster_2022_projects:
                        disaster_2022_projects.append(project_name)

# Match funding records to these projects
funding_amounts = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if this funding record matches any of our disaster projects
    for disaster_proj in disaster_2022_projects:
        # Direct match or partial match
        if (disaster_proj.lower() in project_name.lower() or 
            project_name.lower().replace(' (fema project)', '') in disaster_proj.lower()):
            if project_name not in funding_amounts:
                funding_amounts[project_name] = 0
            funding_amounts[project_name] += amount

total_funding = sum(funding_amounts.values())

print('__RESULT__:')
print(json.dumps({
    "total_funding": total_funding,
    "project_count": len(disaster_2022_projects),
    "matched_projects": len(funding_amounts),
    "projects": disaster_2022_projects,
    "funding_breakdown": funding_amounts
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
