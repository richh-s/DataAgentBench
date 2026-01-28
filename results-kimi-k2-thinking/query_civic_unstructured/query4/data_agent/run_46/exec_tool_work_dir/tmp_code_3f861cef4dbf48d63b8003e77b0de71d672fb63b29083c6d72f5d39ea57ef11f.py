code = """import json

civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_records = json.load(f)

print(f'Civic docs: {len(civic_docs)}, Funding: {len(funding_records)}')

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'Spring' in text:
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if '2022' in line and ('Spring' in line or 'Mar' in line or 'Apr' in line or 'May' in line):
                for j in range(i-1, max(-1, i-3), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) > 10 and not prev.startswith('cid:'):
                        clean = prev.replace('\u2022', '').replace('\u00e2\u20ac\u2022', '').strip()
                        if clean and 'Agenda' not in clean:
                            spring_projects.append(clean)
                            break

spring_projects = list(dict.fromkeys(spring_projects))
print(f'Found {len(spring_projects)} Spring 2022 projects:')
for p in spring_projects:
    print(f'  {p}')

funding_map = {}
for f in funding_records:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

matched = []
total = 0
for proj in spring_projects:
    if proj in funding_map:
        matched.append({'name': proj, 'amount': funding_map[proj]})
        total += funding_map[proj]
    else:
        for fund_name in funding_map:
            if proj in fund_name or fund_name in proj:
                matched.append({'name': proj, 'amount': funding_map[fund_name], 'match': fund_name})
                total += funding_map[fund_name]
                break

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}}

exec(code, env_args)
