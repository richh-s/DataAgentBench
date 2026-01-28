code = """import json
import re

# Load funding data
funding_file = open('var_functions.query_db:8', 'r')
funding = json.load(funding_file)
funding_file.close()

# Load civic documents
civic_file = open('var_functions.query_db:14', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Create funding lookup
fund_lookup = {}
for f in funding:
    name = f.get('Project_Name', '')
    fund_lookup[name] = int(f.get('Amount', 0))

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        # Skip common headers
        line_lower = line.lower()
        if 'page' in line_lower or 'agenda item' in line_lower or 'public works commission' in line_lower:
            continue
            
        # Look for project names
        if (not line.startswith('(') and 
            not line.startswith('\x95') and 
            not line.startswith('-') and
            not line.startswith('•') and
            'updates:' not in line_lower and 
            'project schedule:' not in line_lower and
            not line.isupper()):
            
            # Check if it's likely a project name
            if line.istitle() or (sum(1 for c in line if c.isupper()) > 2):
                
                # Look ahead for Spring 2022 dates
                for j in range(i+1, min(i+20, len(lines))):
                    next_line = lines[j].strip()
                    if '2022' in next_line:
                        if 'March' in next_line or 'April' in next_line or 'May' in next_line or 'Spring' in next_line:
                            spring_projects.append(line)
                            break

# Remove duplicates
unique_spring = []
seen = set()
for proj in spring_projects:
    if proj not in seen:
        seen.add(proj)
        unique_spring.append(proj)

# Match with funding
total_funding = 0
matched_names = []

for project_name in unique_spring:
    # Try exact match
    if project_name in fund_lookup:
        total_funding += fund_lookup[project_name]
        matched_names.append(project_name)
    else:
        # Try partial match
        for fund_name in fund_lookup:
            if len(project_name) > 15 and (project_name in fund_name or fund_name in project_name):
                total_funding += fund_lookup[fund_name]
                matched_names.append(fund_name)
                break

result = {
    'project_count': len(matched_names),
    'total_funding': total_funding,
    'projects': matched_names
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
