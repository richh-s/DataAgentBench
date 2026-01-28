code = """import json
import re

# Get stored data
civic_docs_result = locals().get('var_functions.query_db:2')
funding_result = locals().get('var_functions.query_db:5')

# Handle civic docs data
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_result

# Handle funding data
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

print(f"Loaded {len(civic_docs_data)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Create funding lookup map
funding_map = {}
for record in funding_data:
    key = record['Project_Name'].strip().lower()
    funding_map[key] = int(record['Amount'])

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
        
    text_lower = text.lower()
    if '2022-spring' in text_lower or '2022-march' in text_lower or '2022-april' in text_lower or '2022-may' in text_lower:
        # Extract project name by looking for headings near date mentions
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if '2022-spring' in line_lower or '2022-march' in line_lower or '2022-april' in line_lower or '2022-may' in line_lower:
                # Look backwards for project name (up to 3 lines)
                project_name = None
                for j in range(i-1, max(i-4, -1), -1):
                    prev_line = lines[j].strip()
                    clean_line = prev_line.replace('●', '').replace('■', '').strip()
                    if (clean_line and len(clean_line) > 10 and 
                        'project schedule' not in clean_line.lower() and
                        'updates:' not in clean_line.lower() and
                        'complete design' not in clean_line.lower() and
                        not clean_line.startswith('(')):
                        project_name = clean_line
                        break
                
                if project_name:
                    # Get funding amount
                    funding_amount = 0
                    project_key = project_name.lower()
                    
                    # Direct match
                    if project_key in funding_map:
                        funding_amount = funding_map[project_key]
                    else:
                        # Try variations
                        for funded_key, amount in funding_map.items():
                            if (funded_key in project_key or project_key in funded_key or
                                funded_key.replace(' project', '') in project_key):
                                funding_amount = amount
                                break
                    
                    spring_2022_projects.append({
                        'name': project_name,
                        'funding': funding_amount
                    })

# Remove duplicates
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['name']
    if name not in unique_projects or proj['funding'] > 0:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())
total_project_count = len(final_projects)
total_funding_amount = sum(p['funding'] for p in final_projects)
projects_with_funding = [p for p in final_projects if p['funding'] > 0]

print(f"\nFinal Results:")
print(f"Total Spring 2022 projects: {total_project_count}")
print(f"Total funding: ${total_funding_amount:,}")
print(f"Projects with funding: {len(projects_with_funding)}")

result = {
    'project_count': total_project_count,
    'total_funding': total_funding_amount,
    'detailed_projects': projects_with_funding[:10]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
