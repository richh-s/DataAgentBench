code = """import json
import re
import os

# Load the data using file paths from storage
funding_path = 'var_functions.query_db:6'
civic_path = 'var_functions.query_db:7'

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for item in funding:
    proj_name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    fund_map[proj_name] = fund_map.get(proj_name, 0) + amount

# Extract disaster projects started in 2022
disaster_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
        
        # Check if this looks like a project title (followed by project info)
        if i < len(lines) - 1 and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
            project_name = line
            
            # Check following lines for disaster indicators and 2022 dates
            is_disaster = False
            has_2022 = False
            
            for j in range(i+1, min(i+12, len(lines))):
                check_line = lines[j].upper()
                
                # Disaster indicators
                if any(indicator in check_line for indicator in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                    is_disaster = True
                
                # 2022 date indicators
                if '2022' in check_line and any(schedule_word in check_line for schedule_word in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'SCHEDULE']):
                    has_2022 = True
            
            if is_disaster and has_2022 and project_name:
                disaster_projs.append(project_name)

# Calculate total funding for these projects
total_funding = 0
matched_funding = []

for proj_name in disaster_projs:
    for fund_proj_name, amount in fund_map.items():
        # Check for exact or partial matches
        if proj_name == fund_proj_name or proj_name in fund_proj_name or fund_proj_name in proj_name:
            total_funding += amount
            matched_funding.append((proj_name, amount))
            break
        
        # Check for word overlap (for similar names)
        proj_words = set([w.lower() for w in re.findall(r'\w+', proj_name) if len(w) > 5])
        fund_words = set([w.lower() for w in re.findall(r'\w+', fund_proj_name) if len(w) > 5])
        
        if proj_words.intersection(fund_words):
            total_funding += amount
            matched_funding.append((proj_name, amount))
            break

# Output results
print('__RESULT__:')
print(json.dumps({
    'total_funding_for_disaster_projects_2022': total_funding,
    'number_of_disaster_projects_found': len(disaster_projs),
    'number_of_projects_matched_with_funding': len(matched_funding),
    'sample_matched_projects': [p[0] for p in matched_funding[:5]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
