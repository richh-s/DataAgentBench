code = """import json
import re

# Load funding data from file
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs from file
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Data loaded successfully')
print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_docs)}')

# Identify potential disaster projects from funding data
disaster_candidates = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    # Check if project name indicates disaster-related work
    if ('FEMA' in project_name or 
        '(CalOES' in project_name or 
        '(CalJPIA' in project_name or
        'fire' in project_name.lower() or
        'emergency' in project_name.lower()):
        disaster_candidates.append(record)

print(f'Disaster candidates from funding: {len(disaster_candidates)}')

# Process civic docs to find 2022 information
all_text = ''
for doc in civic_docs:
    all_text += ' ' + doc.get('text', '')

# Find disaster projects that started in 2022
disaster_projects_2022 = []

for project in disaster_candidates:
    project_name = project.get('Project_Name')
    amount = int(project.get('Amount', 0))
    
    # Check if this project appears in the civic documents with 2022 reference
    if project_name in all_text:
        # Find occurrences
        pattern = project_name.replace('(', '\(').replace(')', '\)').replace('.', '\.')
        matches = re.finditer(pattern, all_text)
        
        started_2022 = False
        
        for match in matches:
            start = max(0, match.start() - 200)
            end = min(len(all_text), match.end() + 200)
            context = all_text[start:end]
            
            # Check if 2022 appears in context and indicates start/completion
            if '2022' in context:
                # Look for indicators that suggest start or active status in 2022
                if any(ind in context.lower() for ind in ['completed', 'completion', 'start', 'st:', 'begin', 'advertise']):
                    started_2022 = True
                    break
        
        if started_2022:
            disaster_projects_2022.append({
                'Project_Name': project_name,
                'Amount': amount,
                'Funding_Source': project.get('Funding_Source')
            })

# Calculate totals
total_funding = sum(p['Amount'] for p in disaster_projects_2022)

print(f'\nDisaster projects from 2022: {len(disaster_projects_2022)}')
print(f'Total funding: ${total_funding:,}')

for p in disaster_projects_2022:
    print(f"- {p['Project_Name']}: ${p['Amount']:,}")

result = {
    'total_funding': total_funding,
    'project_count': len(disaster_projects_2022),
    'projects': disaster_projects_2022
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
