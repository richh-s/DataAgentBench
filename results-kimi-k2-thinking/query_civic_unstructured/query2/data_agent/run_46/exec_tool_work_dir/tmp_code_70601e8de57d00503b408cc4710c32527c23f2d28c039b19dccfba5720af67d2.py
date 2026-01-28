code = """import json
import re

# Access storage variables
civic_docs = locals()['var_functions.query_db:8']
funding_data = locals()['var_functions.query_db:10']

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Parse documents for park projects completed in 2022
park_projects_2022 = []
all_text = ''

for doc in civic_docs:
    text = doc.get('text', '')
    all_text += text + '\n'
    lines = text.split('\n')
    
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or 'Page' in line or '---' in line:
            continue
        
        # Look for project names
        if (len(line) > 10 and not line[0] in '-*(' and 
            'PROJECTS' not in line.upper() and i < len(lines)-2):
            
            # Look ahead for completion info
            for j in range(i+1, min(i+8, len(lines))):
                next_line = lines[j].strip()
                
                # Check if completed in 2022 and park-related
                if 'completed' in next_line.lower() and '2022' in next_line:
                    project_lower = line.lower()
                    if ('park' in project_lower or 
                        'bluffs' in project_lower or 
                        'shade' in project_lower or
                        ('structure' in project_lower and 'park' in text.lower())):
                        
                        park_projects_2022.append(line)
                        break

# Get unique projects
unique_park_projects = list(set(park_projects_2022))

# Find funding matches
total_funding = 0
matched_projects = []

for proj in unique_park_projects:
    proj_key = proj.lower().replace(' ', '')
    amount = 0
    
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
    else:
        # Try without parentheses content
        clean_key = re.sub(r'\([^)]*\)', '', proj_key).strip()
        if clean_key in funding_lookup:
            amount = funding_lookup[clean_key]
    
    if amount > 0:
        total_funding += amount
        matched_projects.append({
            'project': proj,
            'amount': amount
        })

# Also check for known projects from preview
known_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

for proj in known_projects:
    if proj in all_text and '2022' in all_text:
        proj_key = proj.lower().replace(' ', '')
        if proj_key in funding_lookup:
            already_matched = any(m['project'] == proj for m in matched_projects)
            if not already_matched:
                amount = funding_lookup[proj_key]
                total_funding += amount
                matched_projects.append({
                    'project': proj,
                    'amount': amount
                })

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
