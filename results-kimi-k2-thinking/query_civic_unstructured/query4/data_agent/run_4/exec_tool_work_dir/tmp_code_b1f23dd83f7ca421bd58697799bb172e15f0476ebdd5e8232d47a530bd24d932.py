code = """import json
import re

# Load civic documents
civic_path = var_functions.query_db:50
civic_docs = json.load(open(civic_path))

# Load funding data
funding_path = var_functions.query_db:60
funding_data = json.load(open(funding_path))

# Create funding lookup by project name
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(fund.get('Amount', 0))

print(f"Loaded {len(civic_docs)} documents and {len(funding_lookup)} funded projects")

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document mentions Spring 2022
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Extract potential project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty or too short/long lines
            if len(line) < 10 or len(line) > 200:
                continue
            # Skip formatting lines
            if line.startswith('(') or line.startswith('To:') or line.startswith('From:') or line.startswith('Subject:'):
                continue
                
            # Look for project name indicators
            project_keywords = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation', 'System', 'Facility', 'Road', 'Park', 'Drainage']
            if any(keyword in line for keyword in project_keywords):
                spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))
print(f"Found {len(spring_2022_projects)} potential Spring 2022 projects")

# Match with funding data
matched_projects = []
used_funding_names = set()
total_funding = 0

for proj in spring_2022_projects:
    # Exact match
    if proj in funding_lookup and proj not in used_funding_names:
        amount = funding_lookup[proj]
        matched_projects.append({'project': proj, 'funding': amount})
        used_funding_names.add(proj)
        total_funding += amount
        continue
    
    # Partial match
    proj_lower = proj.lower()
    for fund_name in funding_lookup:
        if fund_name in used_funding_names:
            continue
        # Check for substring match with reasonable length difference
        if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
            if abs(len(proj) - len(fund_name)) < 50:  # Avoid false matches
                amount = funding_lookup[fund_name]
                matched_projects.append({'project': proj, 'matched_funding': fund_name, 'funding': amount})
                used_funding_names.add(fund_name)
                total_funding += amount
                break

# Remove duplicates and prepare final result
unique_projects = {}
for mp in matched_projects:
    proj_key = mp['project']
    if proj_key not in unique_projects:
        unique_projects[proj_key] = mp['funding']

final_count = len(unique_projects)
final_total = sum(unique_projects.values())

result = {
    'project_count': final_count,
    'total_funding': final_total,
    'sample_projects': list(unique_projects.items())[:10]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
