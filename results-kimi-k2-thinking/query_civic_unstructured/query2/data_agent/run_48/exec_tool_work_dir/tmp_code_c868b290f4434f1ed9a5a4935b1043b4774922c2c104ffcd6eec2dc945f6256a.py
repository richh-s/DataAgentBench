code = """import json

# Load data from files
civic_path = var_functions.query_db:6
funding_data = var_functions.query_db:0

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Docs:', len(civic_docs), 'Funding records:', len(funding_data))

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    if not text:
        continue
    
    # Simple pattern matching
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this line is likely a project name with park-related terms
        line_lower = line.lower()
        if any(term in line_lower for term in ['park', 'playground', 'walkway', 'walkway']):
            # Look for completion in 2022 in surrounding text
            context = '\n'.join(lines[max(0,i-5):min(len(lines),i+10)]).lower()
            if 'completed' in context and '2022' in context:
                # Additional check to avoid headings
                if not any(heading in line_lower for heading in ['capital improvement', 'disaster recovery', 'public works']):
                    park_projects.append({
                        'name': line,
                        'filename': filename,
                        'topic': 'park',
                        'status': 'completed',
                        'year': '2022'
                    })

print('Park projects completed in 2022:', len(park_projects))
for p in park_projects:
    print('-', p['name'])

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for park_proj in park_projects:
    proj_name = park_proj['name']
    for fund_record in funding_data:
        if fund_record['Project_Name'] == proj_name:
            amount = int(fund_record['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': proj_name,
                'amount': amount
            })
            break

result = {
    'total_funding_2022': total_funding,
    'matched_projects': matched_projects,
    'park_projects_found': len(park_projects)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
