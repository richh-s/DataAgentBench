code = """import json
import re

# Get the variables directly from locals
funding_data = var_functions.query_db:5
civic_docs = var_functions.query_db:2

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Extract project information from civic documents using regex patterns
spring_2022_projects = []

# Patterns to identify start dates and project names in text
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for spring 2022 references and project names
    # Pattern for "Spring 2022" or "2022-Spring" or "2022-March" etc.
    spring_2022_pattern = r'(spring\s+2022|2022-spring|2022-0[3-5]|2022-march|2022-april|2022-may)'
    
    if re.search(spring_2022_pattern, text, re.IGNORECASE):
        # Try to extract project names that start in spring 2022
        # Look for patterns like project names followed by schedules
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if re.search(spring_2022_pattern, line, re.IGNORECASE):
                # Look backwards for project name
                for j in range(i-5, i):
                    if j >= 0 and lines[j].strip() and not lines[j].startswith('(') and 'Page' not in lines[j]:
                        project_name = lines[j].strip()
                        if project_name and len(project_name) > 10 and not project_name.startswith('•'):
                            spring_2022_projects.append({
                                'project_name': project_name,
                                'source_doc': doc['filename']
                            })
                            break

print(f"Found {len(spring_2022_projects)} potential spring 2022 projects")

# Match these projects with funding
project_names = [p['project_name'] for p in spring_2022_projects]
matched_funding = []

for funding_record in funding_data:
    funding_name = funding_record['Project_Name']
    for project_name in project_names:
        # Match by checking if funding_name contains the project name or vice versa
        if (funding_name.lower() in project_name.lower() or 
            project_name.lower() in funding_name.lower() or
            any(funding_name.lower().startswith(pn.lower().split()[0]) for pn in project_names if ' ' in pn)):
            matched_funding.append({
                'Project_Name': funding_record['Project_Name'],
                'Amount': int(funding_record['Amount'])
            })

# Remove duplicates (same project might match multiple times)
unique_funding = {}
for item in matched_funding:
    project = item['Project_Name']
    amt = item['Amount']
    if project in unique_funding:
        unique_funding[project] = max(unique_funding[project], amt)  # Keep max amount
    else:
        unique_funding[project] = amt

project_count = len(unique_funding)
total_funding = sum(unique_funding.values())

print(f"Final result: {project_count} projects, ${total_funding:,} total funding")

# Output result in required format
result = {
    'project_count': project_count,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
