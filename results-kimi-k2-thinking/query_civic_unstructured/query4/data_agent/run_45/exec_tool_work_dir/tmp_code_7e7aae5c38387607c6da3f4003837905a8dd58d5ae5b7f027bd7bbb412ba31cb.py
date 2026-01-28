code = """import json
civic_file = globals()['var_functions.query_db:60']
funding_file = globals()['var_functions.query_db:48']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Loaded civic docs:', len(civic_docs))
print('Loaded funding records:', len(funding_data))

spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022-Spring' in text or '2022-March' in text or '2022-April' in text or '2022-May' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line and sum(1 for c in line if c.isupper()) > 5:
                spring_projects.append(line)

unique_projects = list(set(spring_projects))
print('Spring 2022 projects:', len(unique_projects))

funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if name:
        funding_map[name] = amount
        base = name.split('(')[0].strip()
        funding_map[base] = amount

matched = []
total = 0
for proj in unique_projects:
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

result = {'project_count': len(matched), 'total_funding': total, 'projects': matched[:20]}
print('Matched projects:', len(matched))
print('Total funding:', total)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
