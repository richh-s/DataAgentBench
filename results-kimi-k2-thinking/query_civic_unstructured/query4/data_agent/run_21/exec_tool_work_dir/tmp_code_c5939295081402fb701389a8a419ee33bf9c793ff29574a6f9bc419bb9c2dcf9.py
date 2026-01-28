code = """import json, os, re

# Load data
funding_path = var_functions.query_db_48
civic_path = var_functions.query_db_2

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_documents = json.load(f)

# Build funding map
funding_dict = {}
for r in funding_data:
    funding_dict[r['Project_Name']] = int(r['Amount'])

# Find Spring 2022 projects (simplified)
spring_projects = set()

for doc in civic_documents:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if 'Spring 2022' in line:
            # Simple: just take the line before as project name if it exists
            if i > 0:
                project_name = lines[i-1].strip().replace('•', '')
                if project_name and len(project_name) > 5:
                    spring_projects.add(project_name)

# Match with funding (simple exact match only)
matches = {}
for proj in spring_projects:
    if proj in funding_dict:
        matches[proj] = funding_dict[proj]

# Calculate results
total_projects = len(matches)
total_funding = sum(matches.values())

print('__RESULT__:')
print(json.dumps({
    'total_projects': total_projects,
    'total_funding': total_funding,
    'project_details': list(matches.items())
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
