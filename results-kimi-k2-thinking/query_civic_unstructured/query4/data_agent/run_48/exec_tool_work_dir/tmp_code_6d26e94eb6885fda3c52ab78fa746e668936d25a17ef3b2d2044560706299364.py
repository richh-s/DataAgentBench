code = """import json
import re

# Load funding data
f_file = open('var_functions.query_db:8', 'r')
funding_data = json.load(f_file)
f_file.close()

# Load civic documents
c_file = open('var_functions.query_db:14', 'r')
civic_docs = json.load(c_file)
c_file.close()

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    funding_lookup[name] = int(item.get('Amount', 0))

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        line_lower = line.lower()
        if 'page' in line_lower or 'agenda item' in line_lower:
            continue
            
        # Check for project name patterns
        if (not line.startswith('(') and 
            not line.startswith('·') and
            not line.startswith('-') and  
            'updates:' not in line_lower and
            'project schedule:' not in line_lower):
            
            if line.istitle() or sum(1 for c in line if c.isupper()) > 3:
                # Look for Spring 2022 in following lines
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j].strip()
                    if '2022' in next_line:
                        if 'March' in next_line or 'April' in next_line or 'May' in next_line:
                            spring_projects.append(line)
                            break
                        elif 'Spring' in next_line:
                            spring_projects.append(line)
                            break

# Remove duplicates
unique_projects = list(set(spring_projects))

# Match with funding
total_funded = 0
success_matches = []

for proj_name in unique_projects:
    if proj_name in funding_lookup:
        total_funded += funding_lookup[proj_name]
        success_matches.append(proj_name)
    else:
        # Try partial match
        for fund_name, amount in funding_lookup.items():
            if len(proj_name) > 15 and (proj_name in fund_name or fund_name in proj_name):
                total_funded += amount
                success_matches.append(fund_name)
                break

result = {
    'project_count': len(success_matches),
    'total_funding': total_funded
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
