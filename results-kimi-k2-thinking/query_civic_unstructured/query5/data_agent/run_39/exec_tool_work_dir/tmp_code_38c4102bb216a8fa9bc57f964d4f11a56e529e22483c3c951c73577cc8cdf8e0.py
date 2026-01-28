code = """import json
import re

# The storage keys contain file paths
funding_file_path = var_functions.query_db:2
civic_file_path = var_functions.query_db:6

print('Loading funding data from:', funding_file_path)
print('Loading civic docs from:', civic_file_path)

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(funding_data)} funding records and {len(civic_docs)} civic documents')

# Identify disaster projects from funding data
disaster_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if any(kw in project_name for kw in ['(FEMA', '(CalOES', '(CalJPIA', 'Fire', 'Emergency', 'FEMA']):
        disaster_projects.append({
            'name': project_name,
            'amount': int(record.get('Amount', 0)),
            'source': record.get('Funding_Source')
        })

print(f'Found {len(disaster_projects)} disaster projects in funding data')

# Search for projects starting in 2022 in civic documents
all_text = '\n'.join([doc.get('text', '') for doc in civic_docs])

projects_2022 = []
for project in disaster_projects:
    project_name = project['name']
    
    # Check if project name appears with 2022 context
    if project_name in all_text:
        idx = all_text.find(project_name)
        # Check surrounding context for 2022
        context_start = max(0, idx - 200)
        context_end = min(len(all_text), idx + 200)
        context = all_text[context_start:context_end]
        
        if '2022' in context:
            lower_context = context.lower()
            # Check for completion/start indicators
            if any(ind in lower_context for ind in ['completed', 'completion', 'start', 'begin', 'construction']):
                projects_2022.append(project)

# Also check base names without suffixes
for project in disaster_projects:
    if project in projects_2022:
        continue
        
    base_name = project['name'].split('(')[0].strip()
    if base_name != project['name'] and base_name in all_text:
        idx = all_text.find(base_name)
        if idx >= 0:
            context_start = max(0, idx - 200)
            context_end = min(len(all_text), idx + 200)
            context = all_text[context_start:context_end]
            
            if '2022' in context:
                lower_context = context.lower()
                if any(ind in lower_context for ind in ['completed', 'completion', 'start', 'begin', 'construction']):
                    projects_2022.append(project)

# Remove duplicates
unique_projects = []
seen_names = set()
for p in projects_2022:
    if p['name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['name'])

total_funding = sum(p['amount'] for p in unique_projects)

result = {
    'total_funding': total_funding,
    'project_count': len(unique_projects),
    'projects': unique_projects
}

print(f'__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'test': True, 'funding_count': 0, 'civic_count': 0}}

exec(code, env_args)
