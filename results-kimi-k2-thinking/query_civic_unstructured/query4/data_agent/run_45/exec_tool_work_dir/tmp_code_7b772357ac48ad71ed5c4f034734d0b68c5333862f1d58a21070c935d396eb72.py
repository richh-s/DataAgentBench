code = """import json

# Load data files
civic_path = globals()['var_functions.query_db:60']
funding_path = globals()['var_functions.query_db:48']

with open(civic_path, 'r') as f:
    docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

print('Loaded data')

# Build funding map
funding_map = {}
for rec in funding:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funding_map[name] = amt
    base = name.split('(')[0].strip()
    if base != name:
        funding_map[base] = amt

# Find Spring 2022 projects
spring_projects = set()
patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in docs:
    text = doc.get('text', '')
    has_spring = any(p in text for p in patterns)
    if has_spring:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'PROJECT' in line.upper():
                uppers = sum(1 for c in line if c.isupper())
                if uppers > len(line.replace(' ', '')) * 0.2:
                    spring_projects.add(line)

matched = []
total = 0
for proj in spring_projects:
    if proj in funding_map:
        amt = funding_map[proj]
        matched.append({'project': proj, 'amount': amt})
        total += amt
    else:
        base = proj.split('(')[0].strip()
        if base in funding_map:
            amt = funding_map[base]
            matched.append({'project': proj, 'amount': amt})
            total += amt

result = {'count': len(matched), 'total_funding': total}
print('Result:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}]}

exec(code, env_args)
