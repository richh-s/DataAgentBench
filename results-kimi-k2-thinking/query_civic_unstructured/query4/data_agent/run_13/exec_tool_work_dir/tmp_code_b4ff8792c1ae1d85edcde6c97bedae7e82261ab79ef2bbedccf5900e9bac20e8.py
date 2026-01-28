code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:4']
funding_2022_path = locals()['var_functions.query_db:70']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_2022_path, 'r') as f:
    funding_2022 = json.load(f)

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean:
            continue
        
        # Look for Spring 2022 patterns
        lower_line = line_clean.lower()
        
        # Check for Spring 2022 mentions (including March, April, May)
        has_spring_2022 = False
        if 'spring' in lower_line and '2022' in lower_line:
            has_spring_2022 = True
        elif '2022-spring' in lower_line:
            has_spring_2022 = True
        elif '2022' in lower_line:
            # Check for March, April, May
            if any(month in lower_line for month in ['mar', 'apr', 'may']):
                has_spring_2022 = True
        
        if has_spring_2022:
            # Look backwards for project name (usually a few lines before)
            project_name = None
            for j in range(max(0, i-3), i):
                prev_line = lines[j].strip()
                # Heuristic for project names
                if (len(prev_line) > 10 and 
                    prev_line[0].isupper() and 
                    not prev_line.startswith('Page') and 
                    not prev_line.startswith('Item') and
                    'PUBLIC WORKS' not in prev_line and
                    'COMMISSION' not in prev_line and
                    'AGENDA' not in prev_line):
                    project_name = prev_line
                    break
            
            if project_name:
                spring_2022_projects.add(project_name)

# Try to match projects with funding records
matched_projects = []
total_funding = 0

# Create a mapping of funding records for easier matching
funding_map = {}
for fund in funding_2022:
    funding_map[fund['Project_Name'].lower()] = {
        'name': fund['Project_Name'],
        'amount': int(fund['Amount'])
    }

# Match projects with funding
for project in spring_2022_projects:
    proj_lower = project.lower()
    
    # Check direct matches
    matched = False
    for fund_lower, fund_info in funding_map.items():
        # Check if project name is contained in funding name or vice versa
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matched_projects.append({
                'project_name': project,
                'funding_record': fund_info['name'],
                'amount': fund_info['amount']
            })
            total_funding += fund_info['amount']
            matched = True
            break
    
    # If no direct match, check partial word matches
    if not matched:
        # Extract key words from project name (skip common words)
        project_words = [word for word in proj_lower.split() 
                        if len(word) > 5 and word not in ['project', 'improvements', 'repairs', 'and', 'the']]
        
        for fund_lower, fund_info in funding_map.items():
            # Check if any project word appears in funding name
            if any(word in fund_lower for word in project_words):
                matched_projects.append({
                    'project_name': project,
                    'funding_record': fund_info['name'],
                    'amount': fund_info['amount']
                })
                total_funding += fund_info['amount']
                break

result = {
    'spring_2022_projects_count': len(spring_2022_projects),
    'total_funding': total_funding,
    'project_names': sorted(list(spring_2022_projects)),
    'matched_funding_records': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}], 'var_functions.execute_python:64': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.query_db:70': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}

exec(code, env_args)
