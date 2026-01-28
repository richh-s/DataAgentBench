code = """import json
import re

# Load funding data from file
funding_file = 'var_functions.query_db:8'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents from file
civic_file = 'var_functions.query_db:2'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if 'Construction was completed' in line and '2022' in line:
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) < 100:
                    lower = prev_line.lower()
                    if 'park' in lower or 'playground' in lower:
                        park_projects_2022.add(prev_line)

# Find funding for these projects
project_names_in_funding = [f['Project_Name'] for f in funding_data]
matching_projects = []
total_funding = 0

for park_project in park_projects_2022:
    # Exact match
    if park_project in project_names_in_funding:
        for f in funding_data:
            if f['Project_Name'] == park_project:
                amount = int(f['Amount'])
                matching_projects.append({'project': park_project, 'amount': amount})
                total_funding += amount
                break
    else:
        # Fuzzy match
        for f in funding_data:
            if park_project.lower() in f['Project_Name'].lower():
                amount = int(f['Amount'])
                matching_projects.append({'project': f['Project_Name'], 'amount': amount})
                total_funding += amount
                break

print('__RESULT__:')
print(json.dumps({
    'park_projects_completed_2022': list(park_projects_2022),
    'matching_projects': matching_projects,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
