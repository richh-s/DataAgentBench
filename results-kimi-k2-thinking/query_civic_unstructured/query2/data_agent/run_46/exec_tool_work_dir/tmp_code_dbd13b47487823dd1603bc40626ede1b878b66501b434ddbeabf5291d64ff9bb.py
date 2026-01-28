code = """import json, re

# Load civic documents
civic_docs_file = '../var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = '../var_functions.query_db:10'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Parse civic documents for park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project sections
    
    # Pattern 1: project name followed by completion info
    # Look for lines ending with project names, followed by completion status
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and headers
        if not line or '---' in line or 'Agenda Item' in line or 'Page' in line:
            i += 1
            continue
        
        # Check if this line might be a project name (not a bullet point)
        if len(line) > 5 and len(line) < 200 and not line[0] in '-*+([({' and 'PROJECTS' not in line.upper():
            # Look ahead for completion info
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                
                # Check if completed in 2022
                if 'completed' in next_line.lower() and '2022' in next_line:
                    # Check if it's park-related
                    project_lower = line.lower()
                    if 'park' in project_lower or ('Park' in line and ('shade' in project_lower or 'structure' in project_lower or 'repair' in project_lower)):
                        park_projects_2022.append({
                            'name': line,
                            'completion_info': next_line
                        })
                        break
                # Also check for Complete Construction: pattern
                elif 'Complete Construction:' in next_line and '2022' in next_line:
                    project_lower = line.lower()
                    if 'park' in project_lower:
                        park_projects_2022.append({
                            'name': line,
                            'completion_info': next_line
                        })
                        break
        
        i += 1

# Calculate total funding for matching projects
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    proj_name = proj['name']
    proj_key = proj_name.lower().replace(' ', '')
    
    # Direct match
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total_funding += amount
        matched_projects.append({
            'project': proj_name,
            'amount': amount
        })
    else:
        # Try fuzzy matching
        proj_lower = proj_name.lower()
        for fund_name, fund_amount in funding_lookup.items():
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                total_funding += fund_amount
                matched_projects.append({
                    'project': proj_name,
                    'matched_funding_name': fund_name,
                    'amount': fund_amount
                })
                break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
