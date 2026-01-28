code = """import json
import re

# Load data with proper variable access
result1 = var_functions.query_db:2
result2 = var_functions.query_db:12

with open(result1, 'r') as f:
    civic_docs = json.load(f)

with open(result2, 'r') as f:
    funding_records = json.load(f)

# Create funding dictionary
funding_dict = {}
for rec in funding_records:
    funding_dict[rec['Project_Name']] = int(rec['Amount'])

spring_projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip short lines or bullets
        if len(line) < 5 or line.startswith('('):
            continue
        
        # Check following lines for Spring 2022 indicators
        max_lookahead = min(i + 8, len(lines))
        for j in range(i + 1, max_lookahead):
            next_line = lines[j].lower()
            
            # Check various Spring 2022 patterns
            is_spring = False
            if 'spring 2022' in next_line or '2022-spring' in next_line:
                is_spring = True
            if 'march 2022' in next_line or '2022-03' in next_line:
                is_spring = True
            if 'april 2022' in next_line or '2022-04' in next_line:
                is_spring = True  
            if 'may 2022' in next_line or '2022-05' in next_line:
                is_spring = True
                
            if is_spring:
                # Found a Spring 2022 project
                project_name = line
                if project_name in funding_dict:
                    spring_projects.append({
                        'name': project_name,
                        'funding': funding_dict[project_name]
                    })
                break  # Move to next potential project

# Remove duplicates
unique_names = set()
unique_projects = []
for proj in spring_projects:
    if proj['name'] not in unique_names:
        unique_names.add(proj['name'])
        unique_projects.append(proj)

# Calculate results
count = len(unique_projects)
total_funding = sum(p['funding'] for p in unique_projects)

# Special check for known 2022 Morning View project
morning_view = '2022 Morning View Resurfacing & Storm Drain Improvements'
if morning_view in funding_dict:
    print('Special: Morning View project has funding of %d' % funding_dict[morning_view])

result = {
    'spring_2022_count': count,
    'total_funding': total_funding,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
