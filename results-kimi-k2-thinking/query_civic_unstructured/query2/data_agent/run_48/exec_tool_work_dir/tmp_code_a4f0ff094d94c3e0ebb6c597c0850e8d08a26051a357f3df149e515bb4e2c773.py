code = """import json

# Read funding data
funding_data = var_functions.query_db:0

# Read civic documents path and load
f = open(var_functions.query_db:6)
civic_docs = json.load(f)
f.close()

print('Documents loaded:', len(civic_docs))
print('Funding records:', len(funding_data))

# Track park projects completed in 2022
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
        
        # Check if line contains park keywords
        line_lower = line.lower()
        has_park = False
        for keyword in ['park', 'playground', 'walkway']:
            if keyword in line_lower:
                has_park = True
                break
        
        if has_park:
            # Skip obvious headings
            if 'capital improvement' in line_lower or 'agenda' in line_lower:
                continue
            
            # Look for completion in 2022
            context_start = max(0, i-5)
            context_end = min(len(lines), i+8)
            context = ' '.join(lines[context_start:context_end])
            
            if 'completed' in context.lower() and '2022' in context:
                park_projects.append(line)
                print('Found:', line)

print('Park projects found:', len(park_projects))

# Calculate funding total
total_funding = 0
for proj in park_projects:
    for fund in funding_data:
        if fund['Project_Name'] == proj:
            total_funding += int(fund['Amount'])
            break

result = {
    'total_funding': total_funding,
    'project_count': len(park_projects)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
