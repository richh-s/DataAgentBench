code = """import json

# Load funding records
try:
    funding_records = var_functions.query_db:0
except Exception as e:
    print('Error loading funding data:', e)
    funding_records = []

# Load civic documents from file
f = open(var_functions.query_db:6)
civic_docs = json.load(f)
f.close()

print('Funding records count:', len(funding_records))
print('Civic documents count:', len(civic_docs))

# Extract park projects from documents
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find park-related projects with completion in 2022
    if 'completed' in text.lower() and '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) < 150 and line:
                line_lower = line.lower()
                if any(keyword in line_lower for keyword in ['park', 'playground', 'walkway']):
                    # Skip headings
                    if not any(word in line_lower for word in ['capital improvement', 'agenda', 'page']):
                        # Check if this line is a project name
                        if line not in [p['name'] for p in park_projects]:
                            park_projects.append({'name': line})
                            print('Found project:', line)

print('Total park projects found:', len(park_projects))

# Match with funding data
total_funding = 0
matched_projects = []
for proj in park_projects:
    proj_name = proj['name']
    for fund in funding_records:
        if fund['Project_Name'] == proj_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({'project': proj_name, 'amount': amount})
            print('Matched funding:', proj_name, amount)

result = {
    'total_funding_2022': total_funding,
    'matched_projects': matched_projects,
    'park_projects_count': len(park_projects)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
