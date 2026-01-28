code = """import json

# Get file paths
civic_file = var_functions.query_db:50
funding_file = var_functions.query_db:60

# Load the data
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

# Create funding lookup
funding_lookup = {}
for rec in funding_recs:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Split into lines and look for project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Basic filtering
            if len(line) < 10 or len(line) > 200:
                continue
            skip_starts = ['(', 'To:', 'From:', 'Subject:', 'Date:']
            if any(line.startswith(s) for s in skip_starts):
                continue
            # Look for project keywords
            keywords = ['Project', 'Improvements', 'Repairs', 'Replacement']
            if any(k in line for k in keywords):
                spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding
matched = []
used = set()
total = 0

for proj in spring_projects:
    if proj in funding_lookup and proj not in used:
        amt = funding_lookup[proj]
        matched.append({'project': proj, 'funding': amt})
        used.add(proj)
        total += amt
    else:
        # Try partial match
        proj_lower = proj.lower()
        for fund_name in funding_lookup:
            if fund_name in used:
                continue
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                amt = funding_lookup[fund_name]
                matched.append({'project': proj, 'funding': amt})
                used.add(fund_name)
                total += amt
                break

# Get unique projects
unique = {}
for m in matched:
    if m['project'] not in unique:
        unique[m['project']] = m['funding']

count = len(unique)
total_funding = sum(unique.values())

result = json.dumps({'count': count, 'total_funding': total_funding})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}], 'var_functions.list_db:56': ['civic_docs'], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
