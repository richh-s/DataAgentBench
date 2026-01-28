code = """import json

# Get the file paths from the stored variables
civic_docs_file = 'var_functions.query_db:2.json'.replace(':', '_')
funding_file = 'var_functions.query_db:4.json'.replace(':', '_')

# Load the data
civic_docs = json.load(open(civic_docs_file))
funding_recs = json.load(open(funding_file))

# Build funding lookup dictionary
funding_lookup = {}
for rec in funding_recs:
    proj_name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if proj_name:
        funding_lookup[proj_name] = amount

# Find projects that started in Spring 2022
spring_2022_projects = []
seen_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Look for project names in the text
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Identify project name lines
            if (len(line) > 10 and len(line) < 150 and 
                any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Replacement', 'Installation'])):
                if not line.startswith('(') and not line.startswith('To:') and not line.startswith('From:'):
                    spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

# Match projects with funding data
matched_projects = []
used_funding_names = set()
total_funding = 0

for proj_name in spring_2022_projects:
    # Direct exact match
    if proj_name in funding_lookup and proj_name not in used_funding_names:
        amount = funding_lookup[proj_name]
        matched_projects.append({'name': proj_name, 'funding': amount})
        used_funding_names.add(proj_name)
        total_funding += amount
        continue
    
    # Partial/substring matching
    proj_lower = proj_name.lower()
    for fund_name in funding_lookup:
        if fund_name in used_funding_names:
            continue
        # Check if one name is contained in the other or they overlap significantly
        if (proj_lower in fund_name.lower() or fund_name.lower() in proj_lower):
            amount = funding_lookup[fund_name]
            matched_projects.append({'name': proj_name, 'funding': amount})
            used_funding_names.add(fund_name)
            total_funding += amount
            break

# Remove any duplicate entries and get final count
final_projects = []
final_names = set()
for proj in matched_projects:
    if proj['name'] not in final_names:
        final_projects.append(proj)
        final_names.add(proj['name'])

final_count = len(final_projects)
final_total = sum(p['funding'] for p in final_projects)

result = {'project_count': final_count, 'total_funding': final_total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
