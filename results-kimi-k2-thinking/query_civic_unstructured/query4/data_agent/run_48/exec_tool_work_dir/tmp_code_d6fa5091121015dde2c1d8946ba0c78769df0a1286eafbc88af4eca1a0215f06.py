code = """import json
import re

# Load funding data
with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Build funding dictionary with project names as keys
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    funding_lookup[name] = int(item.get('Amount', 0))

# Find all projects with Spring 2022 dates
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 5:
            continue
            
        # Look for lines that might be project names
        # Skip headers and footers
        if any(keyword in line.lower() for keyword in ['page', 'agenda item', 'public works commission']):
            continue
            
        # Skip schedule lines and update lines
        if 'updates:' in line.lower() or 'project schedule:' in line.lower() or \
           'complete design:' in line.lower() or 'advertise:' in line.lower() or \
           'begin construction:' in line.lower() or 'estimated schedule:' in line.lower():
            continue
            
        # Look for title case or proper case lines that aren't bullet points
        if not line.startswith(('(', '-', '•', '·')) and \
           (line.istitle() or (any(c.isupper() for c in line) and not line.isupper())):
            
            # Check if this project has Spring 2022 in nearby lines
            # Look ahead up to 20 lines for date references
            has_spring_2022 = False
            for j in range(i, min(i+20, len(lines))):
                context_line = lines[j].strip()
                # Look for 2022 with Spring or March/April/May
                if '2022' in context_line:
                    # Check for Spring reference
                    if 'Spring' in context_line or 'March' in context_line or \
                       'April' in context_line or 'May' in context_line or \
                       '2022-03' in context_line or '2022-04' in context_line or \
                       '2022-05' in context_line:
                        has_spring_2022 = True
                        break
            
            if has_spring_2022:
                print('Found potential project:', line)
                spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

print('\nSpring 2022 projects:', spring_2022_projects)

# Try to match these projects with funding data
total_funding = 0
matched_projects = []

for project_name in spring_2022_projects:
    # Exact match
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({
            'name': project_name,
            'funding': amount
        })
    else:
        # Try partial match - look for funding projects that contain this name
        for fund_name, amount in funding_lookup.items():
            # Skip very short partial matches
            if len(project_name) > 15 and (project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower()):
                total_funding += amount
                matched_projects.append({
                    'name': project_name,
                    'matched_fund': fund_name,
                    'funding': amount
                })
                break

# Also check projects with '2022' in their name from funding data directly
# These are likely started in 2022
direct_2022_projects = []
for fund_name, amount in funding_lookup.items():
    if '2022' in fund_name and amount > 0:
        direct_2022_projects.append({
            'name': fund_name,
            'funding': amount
        })

# Combine results - include direct 2022 projects if not already matched
for proj in direct_2022_projects:
    if not any(p['name'] == proj['name'] for p in matched_projects):
        matched_projects.append(proj)
        total_funding += proj['funding']

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('\nFinal result:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': []}

exec(code, env_args)
