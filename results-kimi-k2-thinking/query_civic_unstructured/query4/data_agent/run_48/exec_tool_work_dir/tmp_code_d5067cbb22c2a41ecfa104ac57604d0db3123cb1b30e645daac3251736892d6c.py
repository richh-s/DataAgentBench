code = """import json
import re

# Load data
with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for f in funding_data:
    name = f.get('Project_Name', '')
    funding_lookup[name] = {
        'amount': int(f.get('Amount', 0)),
        'source': f.get('Funding_Source', '')
    }

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers
        if any(x in line.lower() for x in ['page', 'agenda item', 'public works commission']):
            continue
            
        # Look for project names
        if (not line.startswith(('(', '·', '-', '•')) and 
            not any(phrase in line.lower() for phrase in ['updates:', 'project schedule:', 'complete', 'advertise'])):
            
            # Check following lines for Spring 2022
            for j in range(i+1, min(i+20, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and ('March' in next_line or 'April' in next_line or 'May' in next_line or 'Spring' in next_line):
                    project_name = line
                    
                    # Get type
                    name_lower = project_name.lower()
                    if 'fema' in name_lower or 'fire' in name_lower:
                        proj_type = 'disaster'
                    else:
                        proj_type = 'capital'
                    
                    spring_projects.append({
                        'name': project_name,
                        'type': proj_type
                    })
                    break

# Remove duplicates
unique_projects = list({p['name']: p for p in spring_projects}.values())

# Match with funding
funded_projects = []
total_funding = 0

for project in unique_projects:
    name = project['name']
    
    # Direct match
    if name in funding_lookup:
        fund = funding_lookup[name]
        funded_projects.append({
            'name': name,
            'type': project['type'],
            'funding': fund['amount']
        })
        total_funding += fund['amount']
    else:
        # Try partial match
        for fund_name in funding_lookup.keys():
            if name in fund_name or fund_name in name:
                if len(name) > 15:  # Only match substantial projects
                    fund = funding_lookup[fund_name]
                    funded_projects.append({
                        'name': name,
                        'type': project['type'],
                        'funding': fund['amount']
                    })
                    total_funding += fund['amount']
                    break

# Output result
result = {
    'project_count': len(funded_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
