code = """import json
import re

civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

print(f'Documents: {len(civic_docs)}, Funding: {len(funding)}')

# Find projects that started in Spring 2022
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for Spring 2022 mentions
    if '2022' in text and 'Spring' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line and 'Spring' in line:
                # Look backwards for project name
                for j in range(i-1, max(-1, i-3), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) > 5 and not prev.startswith('cid:'):
                        clean_name = re.sub(r'^[\u2022\-]+\s*', '', prev)
                        clean_name = re.sub(r'^cid:\d+\s*', '', clean_name)
                        clean_name = ' '.join(clean_name.split())
                        if clean_name and 'Agenda' not in clean_name:
                            spring_projects.append(clean_name)
                        break

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))
print(f'Spring 2022 projects: {len(spring_projects)}')
for p in spring_projects:
    print(f'  {p}')

# Build funding map
funding_map = {}
for f in funding:
    name = f['Project_Name']
    amt = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amt

# Match projects with funding
matched = []
total_funding = 0
for proj in spring_projects:
    if proj in funding_map:
        matched.append({'project': proj, 'funding': funding_map[proj]})
        total_funding += funding_map[proj]
    else:
        for fname, famt in funding_map.items():
            if proj in fname or fname in proj:
                matched.append({'project': proj, 'funding': famt, 'matched_to': fname})
                total_funding += famt
                break

result = {
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}}

exec(code, env_args)
