code = """import json

# Load data from storage
funding_data = var_functions.query_db_0
civic_file_path = var_functions.query_db_6

print('Funding records loaded:', len(funding_data))

# Load civic documents from file path
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print('Civic documents loaded:', len(civic_docs))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 150:
            continue
        
        # Skip common headings
        lower_line = line.lower()
        if any(heading in lower_line for heading in ['capital improvement', 'disaster recovery', 'agenda']):
            continue
        
        # Check for park-related terms
        if any(keyword in lower_line for keyword in ['park', 'playground', 'walkway']):
            # Check surrounding context for completion in 2022
            context_start = max(0, i-5)
            context_end = min(len(lines), i+8)
            context = '\n'.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                if not any(p['name'] == line for p in park_projects_2022):
                    park_projects_2022.append({
                        'name': line,
                        'status': 'completed',
                        'year': '2022'
                    })
                        
print('Found park projects completed in 2022:', len(park_projects_2022))
for proj in park_projects_2022:
    print('  -', proj['name'])

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    proj_name = proj['name']
    for fund in funding_data:
        if fund['Project_Name'] == proj_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': proj_name,
                'amount': amount
            })
            print('Matched funding:', proj_name, '$' + str(amount))

print('\nTotal funding for park projects completed in 2022:', '$' + str(total_funding))

result = {
    'total_funding_2022': total_funding,
    'matched_projects': matched_projects,
    'park_projects_count': len(park_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
