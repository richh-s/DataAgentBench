code = """import json
import re

funding = []
with open('var_functions.query_db:8', 'r') as f:
    funding = json.load(f)

civic_docs = []
with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

# Build funding dictionary
fund_dict = {}
for item in funding:
    name = item.get('Project_Name', '')
    fund_dict[name] = int(item.get('Amount', 0))

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
        skip_words = ['page', 'agenda item', 'public works commission']
        if any(word in line.lower() for word in skip_words):
            continue
            
        # Look for project names (title case, not bullet points)
        if (not line.startswith(('(', '\x95', '-')) and 
            'updates:' not in line.lower() and 
            'project schedule:' not in line.lower() and
            not line.isupper() and
            (line.istitle() or sum(1 for c in line if c.isupper()) > 3)):
            
            # Check following lines for Spring 2022 reference
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line:
                    if any(month in next_line for month in ['March', 'April', 'May']) or 'Spring' in next_line:
                        spring_projects.append(line)
                        break

# Remove duplicates
unique_projects = list(set(spring_projects))

# Match with funding
matched_funding = 0
matched_project_names = []

# Try to match each project with funding
for project_name in unique_projects:
    # Direct match
    if project_name in fund_dict:
        matched_funding += fund_dict[project_name]
        matched_project_names.append(project_name)
        continue
    
    # Partial match - check if project name contains funding project name or vice versa
    for fund_name in fund_dict.keys():
        if (project_name in fund_name or fund_name in project_name) and len(project_name) > 15:
            matched_funding += fund_dict[fund_name]
            matched_project_names.append(fund_name)
            break

result = {
    'project_count': len(matched_project_names),
    'total_funding': matched_funding,
    'project_names': matched_project_names
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
