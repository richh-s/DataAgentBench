code = """import json
import re

# Load funding data and civic documents from file paths
with open(var_functions.query_db_2, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db_5, 'r') as f:
    civic_docs = json.load(f)

print("Loaded", len(funding_data), "funding records and", len(civic_docs), "civic documents")

# Create funding dictionary for projects > $50k
funding_dict = {}
for record in funding_data:
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        funding_dict[record.get('Project_Name', '')] = {
            'amount': amount,
            'funding_id': record.get('Funding_ID'),
            'funding_source': record.get('Funding_Source')
        }

print("Funding dictionary created with", len(funding_dict), "projects")

# Extract project information from text
all_projects = []
for doc in civic_docs:
    text_lines = doc.get('text', '').split('\n')
    current_project = None
    
    for line in text_lines:
        line = line.strip()
        if not line or len(line) < 5:
            continue
            
        # Skip headings and non-project lines
        skip_terms = ['project schedule', 'updates', 'discussion', 'recommended action', 'agenda', 'to:', 'prepared by:', 'date prepared:', 'meeting date:', 'subject:']
        if any(term in line.lower() for term in skip_terms):
            continue
        
        # Look for potential project names (short lines that are not status lines)
        if len(line) < 100 and not line.startswith('(') and not any(term in line.lower() for term in ['complete design:', 'advertise:', 'begin construction:']):
            if current_project and current_project.get('name'):
                all_projects.append(current_project)
            
            current_project = {'name': line, 'status': None, 'type': None, 'topics': []}
        
        # Extract status and type if we have a current project
        if current_project:
            lower = line.lower()
            if 'design' in lower:
                current_project['status'] = 'design'
            elif 'completed' in lower:
                current_project['status'] = 'completed'
            
            if 'capital' in lower or 'capital improvement' in lower:
                current_project['type'] = 'capital'
            elif 'fema' in lower or 'disaster' in lower or 'recovery' in lower:
                current_project['type'] = 'disaster'

# Don't forget the last project
if current_project and current_project.get('name'):
    all_projects.append(current_project)

print("Extracted", len(all_projects), "potential projects")

# Filter for capital projects with design status and matching funding
matching_projects = []
for project in all_projects:
    if project.get('type') == 'capital' and project.get('status') == 'design':
        project_name = project.get('name')
        if project_name in funding_dict:
            matching_projects.append({
                'project_name': project_name,
                'funding_amount': funding_dict[project_name]['amount'],
                'funding_source': funding_dict[project_name]['funding_source']
            })

result = {'count': len(matching_projects), 'projects': matching_projects[:10]}  # Show first 10
print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
