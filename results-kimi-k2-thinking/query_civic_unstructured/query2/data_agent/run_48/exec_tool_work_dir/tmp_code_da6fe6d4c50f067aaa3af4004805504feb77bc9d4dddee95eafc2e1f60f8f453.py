code = """import json

# Load funding and civic documents data
funding_data = var_functions.query_db:0

civic_file = open(var_functions.query_db:6)
civic_docs = json.load(civic_file)
civic_file.close()

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 150:
            continue
        
        # Skip headings
        skip_words = ['capital improvement', 'agenda', 'page', 'subject:', 'to:']
        if any(word in line.lower() for word in skip_words):
            continue
        
        # Check for park-related terms
        line_lower = line.lower()
        has_park = False
        for term in ['park', 'playground', 'walkway']:
            if term in line_lower:
                has_park = True
                break
        
        if has_park:
            # Look for completion in 2022 in surrounding lines
            context_start = max(0, i-5)
            context_end = min(len(lines), i+8)
            context_lines = lines[context_start:context_end]
            context = ' '.join(context_lines).lower()
            
            if 'completed' in context and '2022' in context:
                if line not in [p['name'] for p in park_projects]:
                    park_projects.append({'name': line, 'filename': doc.get('filename', '')})

print('Found park projects completed in 2022:', len(park_projects))
for proj in park_projects:
    print('  -', proj['name'])

# Match with funding data
total_funding = 0
matched_projects = []

for proj in park_projects:
    proj_name = proj['name']
    for fund_record in funding_data:
        if fund_record['Project_Name'] == proj_name:
            amount = int(fund_record['Amount'])
            total_funding += amount
            matched_projects.append({'project': proj_name, 'amount': amount})
            print('Funding matched:', proj_name, '$' + str(amount))

result = {
    'total_funding_2022': total_funding,
    'matched_projects': matched_projects,
    'park_projects_count': len(park_projects)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
