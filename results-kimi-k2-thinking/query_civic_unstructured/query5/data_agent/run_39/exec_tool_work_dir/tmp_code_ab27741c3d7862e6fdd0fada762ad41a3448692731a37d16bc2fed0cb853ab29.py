code = """import json
import re

# Access the storage entries using locals() as instructed
funding_file_path = locals()['var_functions.query_db:2']
civic_file_path = locals()['var_functions.query_db:6']

# Load the data from the files
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(funding_data)} funding records and {len(civic_docs)} civic documents')

# Identify disaster-related projects from funding data
disaster_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    # Check for disaster indicators in project name
    if any(indicator in project_name for indicator in ['(FEMA', '(CalOES', '(CalJPIA', 'FEMA', 'Fire', 'Emergency']):
        try:
            amount = int(record.get('Amount', 0))
        except:
            amount = 0
        disaster_funding.append({
            'name': project_name,
            'amount': amount,
            'source': record.get('Funding_Source', '')
        })

print(f'Found {len(disaster_funding)} disaster-related projects in funding data')

# Combine all civic document text for searching
all_civic_text = '\n\n'.join([doc.get('text', '') for doc in civic_docs])

# Find projects that started in 2022
projects_2022 = []

for project in disaster_funding:
    project_name = project['name']
    
    # First try exact match
    if project_name in all_civic_text:
        # Find the position and check context
        idx = all_civic_text.find(project_name)
        context = all_civic_text[max(0, idx-200):min(len(all_civic_text), idx+200)]
        
        # Check if 2022 appears with indicators of active/completed status
        if '2022' in context:
            lower_context = context.lower()
            if any(indicator in lower_context for indicator in ['completed', 'completion', 'start', 'begin', 'construction', 'design']):
                projects_2022.append(project)
                continue
    
    # Try base name without parenthetical suffix
    base_name = project_name.split('(')[0].strip()
    if base_name != project_name and base_name in all_civic_text:
        idx = all_civic_text.find(base_name)
        context = all_civic_text[max(0, idx-200):min(len(all_civic_text), idx+200)]
        
        if '2022' in context:
            lower_context = context.lower()
            if any(indicator in lower_context for indicator in ['completed', 'completion', 'start', 'begin', 'construction', 'design']):
                projects_2022.append(project)

# Remove duplicates
unique_projects = []
seen_names = set()
for p in projects_2022:
    if p['name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['name'])

# Calculate total funding
total_funding = sum(p['amount'] for p in unique_projects)

print(f'\nFound {len(unique_projects)} disaster projects from 2022')
print(f'Total funding: ${total_funding:,}')

for p in unique_projects:
    print(f"- {p['name']}: ${p['amount']:,}")

result = {
    'total_funding': total_funding,
    'project_count': len(unique_projects),
    'projects': unique_projects
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'test': True, 'funding_count': 0, 'civic_count': 0}}

exec(code, env_args)
