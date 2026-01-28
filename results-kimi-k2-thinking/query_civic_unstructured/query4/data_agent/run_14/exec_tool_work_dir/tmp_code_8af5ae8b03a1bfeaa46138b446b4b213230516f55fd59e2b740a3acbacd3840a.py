code = """import json
import re

# Access the data
civic_docs_data = var_functions.query_db:2
funding_data = var_functions.query_db:5

# Handle potential file paths
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print(f"Civic docs: {len(civic_docs_data)} documents")
print(f"Funding records: {len(funding_data)} records")

# Build project name mapping for matching
project_funding_map = {}
for record in funding_data:
    name = record['Project_Name'].strip().lower()
    project_funding_map[name] = record

print(f"\nBuilt funding map with {len(project_funding_map)} project names")

# Extract Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for Spring 2022 mentions
    if '2022-spring' in text.lower() or '2022-march' in text.lower() or '2022-april' in text.lower() or '2022-may' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if '2022-spring' in line_lower or '2022-march' in line_lower or '2022-april' in line_lower or '2022-may' in line_lower:
                # Look for project name before this line
                project_name = None
                for j in range(i-1, max(i-5, -1), -1):
                    prev_line = lines[j].strip()
                    if prev_line and len(prev_line) > 10:
                        # Clean common artifacts
                        clean_line = prev_line.replace('●', '').replace('■', '').replace('□', '').strip()
                        if (clean_line and not clean_line.startswith('(') and 
                            'project schedule' not in clean_line.lower() and 
                            'updates' not in clean_line.lower() and
                            'complete design' not in clean_line.lower() and
                            len(clean_line) > 5):
                            project_name = clean_line
                            break
                
                if project_name:
                    # Check if this project has funding
                    project_key = project_name.lower()
                    funding_amount = 0
                    
                    # Try direct match
                    if project_key in project_funding_map:
                        funding_amount = int(project_funding_map[project_key]['Amount'])
                    else:
                        # Try fuzzy matching
                        for funded_name, record in project_funding_map.items():
                            if (funded_name in project_key or project_key in funded_name or
                                funded_name.replace(' project', '') in project_key or
                                project_key.replace(' project', '') in funded_name):
                                funding_amount = int(record['Amount'])
                                break
                    
                    spring_2022_projects.append({
                        'Project_Name': project_name,
                        'Funding_Amount': funding_amount,
                        'Document': filename
                    })

print(f"\nFound {len(spring_2022_projects)} Spring 2022 projects")

# Try alternative approach: extract all projects and filter by date context
alternative_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split into project sections
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        if len(section.strip()) < 50:
            continue
            
        section_lower = section.lower()
        # Check if section contains Spring 2022 date
        if ('2022-spring' in section_lower or '2022-march' in section_lower or 
            '2022-april' in section_lower or '2022-may' in section_lower):
            
            # Extract project name (first significant line)
            lines = section.split('\n')
            project_name = None
            for line in lines:
                line = line.strip()
                if line and len(line) > 10 and not line.startswith('('):
                    clean_line = line.replace('●', '').replace('■', '').strip()
                    if (clean_line and 'project schedule' not in clean_line.lower() and 
                        'updates' not in clean_line.lower()):
                        project_name = clean_line
                        break
            
            if project_name and len(project_name) < 200:  # Reasonable length
                # Find funding
                funding_amount = 0
                project_key = project_name.lower()
                
                if project_key in project_funding_map:
                    funding_amount = int(project_funding_map[project_key]['Amount'])
                
                alternative_projects.append({
                    'Project_Name': project_name,
                    'Funding_Amount': funding_amount,
                    'Document': filename
                })

# Combine unique projects
unique_projects = {}
for proj in spring_2022_projects + alternative_projects:
    name = proj['Project_Name']
    if name not in unique_projects or proj['Funding_Amount'] > 0:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())

print(f"Total unique Spring 2022 projects: {len(final_projects)}")
print(f"Projects with funding: {sum(1 for p in final_projects if p['Funding_Amount'] > 0)}")

# Calculate totals
total_funding = sum(p['Funding_Amount'] for p in final_projects)

result = {
    'project_count': len(final_projects),
    'total_funding': total_funding,
    'projects_with_funding': [p for p in final_projects if p['Funding_Amount'] > 0],
    'all_projects_sample': final_projects[:20]
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
