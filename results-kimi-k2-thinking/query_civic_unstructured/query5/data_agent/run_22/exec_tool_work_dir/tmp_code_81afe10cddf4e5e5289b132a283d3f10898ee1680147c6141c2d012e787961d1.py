code = """import json
import re

# Load the data files
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:7']

with open(funding_path) as f:
    funding_data = json.load(f)
with open(civic_path) as f:
    civic_docs_data = json.load(f)

# Step 1: Find all funding for disaster-related projects (containing FEMA/CalOES/CalJPIA)
disaster_funding = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    # Check if this is a disaster project based on name
    if any(keyword.upper() in proj_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER']):
        disaster_funding[proj_name] = disaster_funding.get(proj_name, 0) + amount

# Step 2: Look for projects with 2022 dates in civic documents
disaster_projects_2022 = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find disaster project sections and check for 2022 dates
    if any(keyword.upper() in text.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER']):
        # Look for project names and dates in the text
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and not line.startswith('(') and 'page' not in line.lower() and 'agenda' not in line.lower():
                # Check if next line indicates project info
                if i < len(lines) - 1 and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                    project_name = line
                    
                    # Search for disaster indicators and 2022 dates in following lines
                    is_disaster = False
                    has_2022 = False
                    
                    for j in range(i+1, min(i+15, len(lines))):
                        check_line = lines[j].upper()
                        # Check for disaster indicators
                        if any(indicator in check_line for indicator in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY', 'RECOVERY']):
                            is_disaster = True
                        # Check for 2022 dates in schedule context
                        if '2022' in check_line and any(schedule_word in check_line for schedule_word in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'SCHEDULE']):
                            has_2022 = True
                    
                    if is_disaster and has_2022 and project_name:
                        disaster_projects_2022.append(project_name)
            i += 1

# Step 3: Match projects with funding and calculate total
total_funding = 0
matched_projects = []
unmatched_projects = []

for project_name in disaster_projects_2022:
    matched = False
    for fund_name, amount in disaster_funding.items():
        # Check for name match
        if (project_name in fund_name or fund_name in project_name or
            project_name.replace(' ', '').replace('-', '') in fund_name.replace(' ', '').replace('-', '')):
            total_funding += amount
            matched_projects.append((project_name, amount))
            matched = True
            break
    if not matched:
        unmatched_projects.append(project_name)

# Add any disaster funding that wasn't captured but has project names that are disaster-related
disaster_names_from_funding = list(disaster_funding.keys())

result = {
    'total_funding': total_funding,
    'disaster_projects_with_2022_dates': len(disaster_projects_2022),
    'matched_funding_records': len(matched_projects),
    'unmatched_projects': len(unmatched_projects),
    'sample_matched_projects': [p[0] for p in matched_projects[:5]] if matched_projects else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
