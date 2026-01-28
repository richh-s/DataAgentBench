code = """import json
import re

# Access the stored results
docs = locals()['var_functions.query_db:8']
funding = locals()['var_functions.query_db:10']

# Build funding lookup table
funding_lookup = {}
for item in funding:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Search for park projects completed in 2022
park_projects = []
all_text = ''

for doc in docs:
    text = doc.get('text', '')
    all_text += text + '\n'
    lines = text.split('\n')
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        if not line or 'Page' in line or '---' in line or len(line) < 10:
            continue
        
        # Skip lines that start with bullet points or common markers
        if line[0] in ['-', '*', '+', '(', '[']:
            continue
        
        # Skip header lines
        if line.isupper() or 'PROJECTS' in line.upper():
            continue
        
        # Check if line looks like a project name
        has_caps = any(c.isupper() for c in line[:20])
        if not has_caps:
            continue
        
        # Look ahead for completion information
        for j in range(i + 1, min(i + 15, len(lines))):
            next_line = lines[j].strip()
            
            # Check if completed in 2022
            if 'completed' in next_line.lower() and '2022' in next_line:
                # Check if park-related
                if 'park' in line.lower():
                    park_projects.append(line)
                    break
                # Check for specific park projects
                elif any(keyword in line.lower() for keyword in ['bluffs', 'shade', 'structure', 'walkway', 'playground']):
                    # Verify park context in surrounding text
                    context_start = max(0, i - 5)
                    context_end = min(len(lines), i + 20)
                    context = ' '.join(lines[context_start:context_end]).lower()
                    if 'park' in context:
                        park_projects.append(line)
                        break

# Remove duplicates
park_projects = list(set(park_projects))

# Calculate total funding
matched_projects = []
total_funding = 0

for proj in park_projects:
    proj_key = proj.lower().replace(' ', '')
    
    # Direct match
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total_funding += amount
        matched_projects.append({'project': proj, 'amount': amount})
    else:
        # Try without parenthetical suffixes
        clean_key = re.sub(r'\([^)]*\)', '', proj_key).strip()
        if clean_key in funding_lookup:
            amount = funding_lookup[clean_key]
            total_funding += amount
            matched_projects.append({'project': proj, 'amount': amount})

# Also check for specific known projects from preview
known_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

for proj in known_projects:
    if proj in all_text and '2022' in all_text:
        proj_key = proj.lower().replace(' ', '')
        if proj_key in funding_lookup:
            # Avoid duplicates
            if not any(m['project'] == proj for m in matched_projects):
                amount = funding_lookup[proj_key]
                total_funding += amount
                matched_projects.append({'project': proj, 'amount': amount})

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
