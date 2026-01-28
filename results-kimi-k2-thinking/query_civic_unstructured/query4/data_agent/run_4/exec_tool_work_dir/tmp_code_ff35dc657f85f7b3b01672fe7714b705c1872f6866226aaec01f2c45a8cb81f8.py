code = """import json

# Load civic documents from file
civic_path = 'var_functions.query_db:2'
civic_path = civic_path.replace(':', '_') + '.json'
with open(civic_path) as f:
    civic_docs = json.load(f)

# Load funding records from file
funding_path = 'var_functions.query_db:4'
funding_path = funding_path.replace(':', '_') + '.json'
with open(funding_path) as f:
    funding_records = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Find projects that started in Spring 2022
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for lines that could be project names
            if len(line) > 10 and len(line) < 150:
                if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
                    if not line.startswith('(') and not line.startswith('To:') and not line.startswith('From:'):
                        spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

# Match projects with funding
matched_projects = []
used_projects = set()
total_funding = 0

for proj in spring_2022_projects:
    # Direct match
    if proj in funding_lookup and proj not in used_projects:
        amount = funding_lookup[proj]
        matched_projects.append({'name': proj, 'funding': amount})
        used_projects.add(proj)
        total_funding += amount
        continue
    
    # Partial match by substring
    proj_lower = proj.lower()
    for fund_name in funding_lookup:
        if fund_name in used_projects:
        if fund_name in used_projects:
            continue
        if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
            amount = funding_lookup[fund_name]
            matched_projects.append({'name': proj, 'funding': amount})
            used_projects.add(fund_name)
            total_funding += amount
            break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
