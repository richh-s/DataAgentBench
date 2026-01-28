code = """import json, re

civic_docs_path = 'var_functions.query_db:2'
funding_path = 'var_functions.query_db:5'

with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

print('Docs:', len(civic_docs), 'Funding:', len(funding))

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if '2022' in line and ('Spring' in line or 'Mar' in line or 'Apr' in line or 'May' in line):
            # Look backwards for project name (previous non-empty line)
            for j in range(i-1, max(0, i-5), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('cid:') and len(prev_line) > 10:
                    # Clean up project name
                    proj_name = re.sub(r'^(cid:\d+|[\u2022â€¢\-\*]+\s*)', '', prev_line)
                    proj_name = re.sub(r'\s+', ' ', proj_name).strip()
                    if proj_name and 'Agenda' not in proj_name:
                        spring_projects.append(proj_name)
                    break

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))
print('Spring projects found:', spring_projects)

# Build funding map
funding_map = {}
for f in funding:
    funding_map[f['Project_Name']] = funding_map.get(f['Project_Name'], 0) + int(f['Amount'])

# Match and sum
matched = []
total = 0
for proj in spring_projects:
    if proj in funding_map:
        matched.append({'name': proj, 'amount': funding_map[proj]})
        total += funding_map[proj]
    else:
        # Try partial match
        for fund_name, amount in funding_map.items():
            if proj in fund_name or fund_name in proj:
                matched.append({'name': proj, 'amount': amount, 'matched': fund_name})
                total += amount
                break

result = {'count': len(matched), 'total_funding': total, 'matches': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}}

exec(code, env_args)
