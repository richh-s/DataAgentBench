code = """import json

# Load data
funding_data = var_functions.query_db:0
print('Funding records:', len(funding_data))

civic_path = var_functions.query_db:6
print('Civic docs path:', civic_path)

with open(civic_path) as f:
    civic_docs = json.load(f)

print('Documents:', len(civic_docs))

# Process data
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('
')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for park terms
        if 'park' in line.lower() or 'playground' in line.lower() or 'walkway' in line.lower():
            # Check context for completion in 2022
            context_start = max(0, i-5)
            context_end = min(len(lines), i+8)
            context = ' '.join(lines[context_start:context_end])
            
            if 'completed' in context.lower() and '2022' in context:
                if line not in [p['name'] for p in park_projects]:
                    park_projects.append({'name': line})

print('Park projects:', len(park_projects))

# Calculate funding total
total = 0
matched = []
for proj in park_projects:
    proj_name = proj['name']
    for fund in funding_data:
        if fund['Project_Name'] == proj_name:
            amount = int(fund['Amount'])
            total += amount
            matched.append({'name': proj_name, 'amount': amount})

result = {
    'total_funding': total,
    'matched': matched,
    'park_projects_count': len(park_projects)
}

print('Matching projects:', len(matched))
print('Total funding:', total)

# Output result
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
