code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# First, identify disaster-related projects from funding data
disaster_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    # Check if it's disaster-related based on naming patterns
    if any(keyword in project_name for keyword in ['(FEMA', '(CalOES', '(CalJPIA', 'Fire', 'Emergency', 'FEMA']):
        try:
            amount = int(record.get('Amount', 0))
        except:
            amount = 0
        disaster_projects.append({
            'Project_Name': project_name,
            'Amount': amount,
            'Funding_Source': record.get('Funding_Source', '')
        })

print(f'Found {len(disaster_projects)} disaster-related projects in funding data')

# Extract all text from civic documents for searching
all_civic_text = '\n\n'.join([doc.get('text', '') for doc in civic_docs])

# Find which disaster projects started in 2022
projects_2022 = []

for project in disaster_projects:
    project_name = project['Project_Name']
    
    # Search for project name in civic documents
    if project_name in all_civic_text:
        # Find all occurrences with context
        name_pos = all_civic_text.find(project_name)
        while name_pos != -1:
            # Get context around the project name
            context_start = max(0, name_pos - 300)
            context_end = min(len(all_civic_text), name_pos + 300)
            context = all_civic_text[context_start:context_end]
            
            # Check if 2022 is mentioned indicating start/completion
            if '2022' in context:
                # Check if it's related to start/completion/active status
                lower_context = context.lower()
                if any(indicator in lower_context for indicator in ['completed', 'completion', 'start', 'begin', 'advertise', 'construction']):
                    projects_2022.append(project)
                    break
            
            # Find next occurrence
            name_pos = all_civic_text.find(project_name, name_pos + 1)

# Also check for variations (without parenthetical suffixes)
additional_projects = []
for project in disaster_projects:
    project_name = project['Project_Name']
    # Skip if we already found this project
    if any(p['Project_Name'] == project_name for p in projects_2022):
        continue
    
    # Extract base name without parentheses
    base_name = project_name.split('(')[0].strip()
    if len(base_name) < len(project_name):
        # Check if base name is in civic documents with 2022
        if base_name in all_civic_text:
            name_pos = all_civic_text.find(base_name)
            while name_pos != -1:
                context_start = max(0, name_pos - 300)
                context_end = min(len(all_civic_text), name_pos + 300)
                context = all_civic_text[context_start:context_end]
                
                if '2022' in context:
                    lower_context = context.lower()
                    if any(indicator in lower_context for indicator in ['completed', 'completion', 'start', 'begin', 'advertise', 'construction']):
                        additional_projects.append(project)
                        break
                
                name_pos = all_civic_text.find(base_name, name_pos + 1)

# Combine results
all_2022_projects = projects_2022 + additional_projects

# Remove duplicates
deduplicated = []
seen_names = set()
for p in all_2022_projects:
    if p['Project_Name'] not in seen_names:
        deduplicated.append(p)
        seen_names.add(p['Project_Name'])

# Calculate total funding
total_funding = sum(p['Amount'] for p in deduplicated)

print(f'\nFound {len(deduplicated)} disaster projects from 2022')
print(f'Total funding: ${total_funding:,}')

for p in deduplicated:
    print(f"- {p['Project_Name']}: ${p['Amount']:,}")

result = {
    'total_funding': total_funding,
    'project_count': len(deduplicated),
    'projects': deduplicated
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
