code = """import json

# Load data
funding_path = locals()['var_functions.query_db:24']
with open(funding_path, 'r') as f:
    funding = json.load(f)

civic_path = locals()['var_functions.query_db:26']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map
funding_map = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', 0))
    if name and amount > 0:
        funding_map[name] = amount

# Identify park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completed construction projects mentioning 2022
    if 'Construction)' in text and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for park-related project names
            if ('park' in line.lower() and 
                len(line) > 15 and 
                not line.startswith('(') and
                'Project' not in line[:20]):
                
                # Check if this line or nearby mentions 2022 completion
                context = ' '.join(lines[max(0,i-2):min(len(lines),i+4)])
                if '2022' in context and 'complete' in context.lower():
                    park_projects_2022.append(line)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Find funding for these projects
total_funding = 0
matched_projects = []

for park_project in park_projects_2022:
    # Direct match
    if park_project in funding_map:
        total_funding += funding_map[park_project]
        matched_projects.append(park_project)
    else:
        # Partial/fuzzy match
        for funded_name in funding_map:
            if (park_project.lower() in funded_name.lower() or 
                funded_name.lower() in park_project.lower()):
                total_funding += funding_map[funded_name]
                matched_projects.append(funded_name)
                break

result = {
    'park_projects_found': park_projects_2022,
    'funded_projects': matched_projects,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
