code = """import json

# Load funding data and civic documents
funding_data = var_functions.query_db:0
civic_path = var_functions.query_db:6

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if not text:
        continue
    
    lines = text.split('\n')
    
    # Find all lines that might be project names containing park terms
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip lines that are obvious headings/metadata
        if any(term in line.lower() for term in ['capital improvement', 'disaster recovery', 'agenda', 'page', 'to:', 'subject:']):
            continue
        
        # Look for park-related terms
        line_lower = line.lower()
        if 'park' in line_lower or 'playground' in line_lower or 'walkway' in line_lower:
            # Check if line looks like a project name (not too long, starts with capital)
            if len(line) < 150 and line[0].isupper():
                # Look for surrounding context indicating completion in 2022
                context_start = max(0, i-5)
                context_end = min(len(lines), i+8)
                context = ' '.join(lines[context_start:context_end])
                
                if 'completed' in context.lower() and '2022' in context:
                    # Avoid duplicate entries
                    if not any(p['name'] == line for p in park_projects_2022):
                        park_projects_2022.append({
                            'name': line,
                            'filename': filename
                        })

print('Park projects completed in 2022 found:', len(park_projects_2022))
for proj in park_projects_2022:
    print('  -', proj['name'])

# Match projects with funding data and calculate total
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    project_name = proj['name']
    
    # Find matching funding record
    for fund in funding_data:
        if fund['Project_Name'] == project_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'Project_Name': project_name,
                'Amount': amount
            })
            break

print('\nMatched projects with funding:', len(matched_projects))
for proj in matched_projects:
    print('  -', proj['Project_Name'], ': $' + str(proj['Amount']))

results = {
    'total_funding_2022': total_funding,
    'matched_projects': matched_projects,
    'total_park_projects_found': len(park_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
