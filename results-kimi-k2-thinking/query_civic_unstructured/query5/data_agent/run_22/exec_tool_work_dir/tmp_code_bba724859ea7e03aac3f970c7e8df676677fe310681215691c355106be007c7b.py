code = """import json
import re
import os

# Load data from files
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:7

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs_data = json.load(f)

# Build funding map
funding_map = {}
for r in funding_data:
    name = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    funding_map[name] = funding_map.get(name, 0) + amount

# Extract disaster projects with 2022 dates from civic docs
disaster_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('(') or any(kw in line.lower() for kw in ['page', 'agenda item']):
            continue
        if (len(line) > 5 and i < len(lines) - 1 and 
            any(indicator in lines[i+1] for indicator in ['Updates:', 'Project Schedule:', '(cid:'])):
            project_name = line
            is_disaster = False
            has_2022 = False
            
            # Check following lines for disaster indicators and 2022 dates
            for j in range(i+1, min(i+10, len(lines))):
                check_line = lines[j]
                if any(kw in check_line.upper() for kw in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                    is_disaster = True
                if '2022' in check_line and any(schedule_word in check_line.upper() for schedule_word in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'SCHEDULE']):
                    has_2022 = True
            
            if is_disaster and has_2022:
                disaster_projects.append(project_name)

# Calculate funding for disaster projects started in 2022
total_funding = 0
matched_projects = []
for disaster_proj in disaster_projects:
    for fund_name, amount in funding_map.items():
        if (disaster_proj in fund_name or fund_name in disaster_proj or
            any(token in fund_name for token in disaster_proj.split() if len(token) > 8)):
            total_funding += amount
            matched_projects.append((disaster_proj, amount))
            break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'disaster_projects_found': len(disaster_projects),
    'projects_funded': len(matched_projects),
    'example_projects': disaster_projects[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
