code = """import json

# Read data from storage
civic_docs_file = var_functions.query_db:6
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_functions.query_db:0

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_records)} funding records")

# Find park projects completed in 2022
park_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for park-related project names
        if line and ('park' in line.lower() or 'playground' in line.lower() or 'walkway' in line.lower()):
            # Look ahead for completion in 2022
            look_ahead = '
'.join(lines[i:i+10]).lower()
            if 'completed' in look_ahead and '2022' in look_ahead:
                park_2022_projects.append(line)
        
        i += 1

print(f"Found {len(park_2022_projects)} park projects from 2022")

# Match with funding
total_funding = 0
matched = []

for project_name in park_2022_projects:
    for fund in funding_records:
        if fund['Project_Name'] == project_name:
            amount = int(fund['Amount'])
            total_funding += amount
            matched.append({'name': project_name, 'amount': amount})

result = {
    'total_park_projects_2022': len(park_2022_projects),
    'total_funding': total_funding,
    'matched_projects': matched
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
