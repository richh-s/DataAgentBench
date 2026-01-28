code = """import json

# Get funding data
funding = vars()['var_functions.query_db:0']

# Get and open civic documents file
civic_path = vars()['var_functions.query_db:6']
with open(civic_path) as f:
    docs = json.load(f)

print('Funding:', len(funding), 'Docs:', len(docs))

# Find park projects completed in 2022
projects = []
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 150:
            continue
        
        # Skip headings
        lower = line.lower()
        if 'capital improvement' in lower or 'agenda' in lower or 'page' in lower:
            continue
        
        # Check for park terms
        has_park = False
        for term in ['park', 'playground', 'walkway']:
            if term in lower:
                has_park = True
                break
        
        if has_park and line[0].isupper():
            # Check for completion in 2022
            start = max(0, i-5)
            end = min(len(lines), i+8)
            context = ' '.join(lines[start:end]).lower()
            
            if 'completed' in context and '2022' in context:
                if line not in [p['name'] for p in projects]:
                    projects.append({'name': line})

print('Park projects found:', len(projects))

# Calculate total funding
total = 0
for proj in projects:
    name = proj['name']
    for fund in funding:
        if fund['Project_Name'] == name:
            total += int(fund['Amount'])

result = {'total_funding': total, 'project_count': len(projects)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
