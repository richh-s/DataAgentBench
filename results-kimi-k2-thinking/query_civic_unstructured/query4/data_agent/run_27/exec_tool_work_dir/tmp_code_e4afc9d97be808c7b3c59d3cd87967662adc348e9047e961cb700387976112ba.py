code = """import json
import re

# Load data from files
mongo_file = globals()['var_functions.query_db:5']
funding_file = globals()['var_functions.query_db:20']

# Handle if they're file paths or already loaded data
if isinstance(mongo_file, str) and 'json' in mongo_file:
    with open(mongo_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = mongo_file

if isinstance(funding_file, str) and 'json' in funding_file:
    with open(funding_file, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_file

# Create funding map
funding_map = {}
for rec in funding_records:
    funding_map[rec['Project_Name'].strip()] = int(rec['Amount'])

spring_2022_projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Detect project name (typically a standalone line, title case, not a bullet or metadata)
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not line.startswith('▪') and
            not line.lower().startswith('page ') and
            not line.lower().startswith('agenda') and
            not any(x in line.lower() for x in ['project schedule', 'updates:', 'complete design:', 'begin construction:'])):
            
            # Simple heuristic: if line has no colons, not too short, and looks like a title
            if ':' not in line and len(line) < 100 and not line.isupper():
                current_project = line
        
        # Check for Spring 2022 in schedule lines
        if current_project and '2022' in line:
            has_spring = 'Spring 2022' in line or 'spring 2022' in line
            has_spring_months = any(m in line for m in ['Mar 2022', 'Apr 2022', 'May 2022', 'March 2022', 'April 2022', 'May 2022'])
            
            if has_spring or has_spring_months:
                spring_2022_projects.append(current_project)
                break

# Match projects with funding
matched = []
total_funding = 0

for proj in spring_2022_projects:
    # Direct match
    if proj in funding_map:
        matched.append({'name': proj, 'funding': funding_map[proj]})
        total_funding += funding_map[proj]
    else:
        # Try variations
        variations = [
            proj,
            proj.replace(' Project', ''),
            proj.replace(' Improvements', ''),
            proj.replace(' Repair', ''),
            re.sub(r'\s+', ' ', proj).strip()
        ]
        
        found = False
        for var in variations:
            if var in funding_map:
                matched.append({'name': proj, 'matched': var, 'funding': funding_map[var]})
                total_funding += funding_map[var]
                found = True
                break
        
        if not found:
            # Search for substring match
            for fund_name, amount in funding_map.items():
                if (proj.lower() in fund_name.lower() or 
                    fund_name.lower() in proj.lower()):
                    matched.append({'name': proj, 'matched': fund_name, 'funding': amount})
                    total_funding += amount
                    break

result = {
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': [{'name': m['name'], 'funding': m['funding']} for m in matched]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}, 'var_functions.query_db:36': [{'count': '500', 'total_funding': '28094000'}]}

exec(code, env_args)
