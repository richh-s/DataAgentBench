code = """import json

# Load the data
funding_data = var_functions.query_db:0
civic_docs = json.load(open(var_functions.query_db:6))

print('Loaded', len(civic_docs), 'documents and', len(funding_data), 'funding records')

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
        
        # Skip headings
        if any(term in line.lower() for term in ['capital improvement', 'agenda', 'page', 'subject:']):
            continue
        
        # Check for park terms in potential project name
        line_lower = line.lower()
        if 'park' in line_lower or 'playground' in line_lower or 'walkway' in line_lower:
            if line[0].isupper():
                # Look for 2022 completion in context
                context_start = max(0, i-5)
                context_end = min(len(lines), i+8)
                context = ' '.join(lines[context_start:context_end]).lower()
                
                if 'completed' in context and '2022' in context:
                    if line not in [p['name'] for p in park_projects_2022]:
                        park_projects_2022.append({'name': line, 'filename': doc.get('filename', '')})

print('Found park projects completed in 2022:', len(park_projects_2022))

# Match with funding and calculate total
total_funding = 0
matched = []

for proj in park_projects_2022:
    proj_name = proj['name']
    for fund in funding_data:
        if fund['Project_Name'] == proj_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched.append({'Project_Name': proj_name, 'Amount': amount})

result = {
    'total_funding_2022': total_funding,
    'matched_projects': matched,
    'park_projects_count': len(park_projects_2022)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
