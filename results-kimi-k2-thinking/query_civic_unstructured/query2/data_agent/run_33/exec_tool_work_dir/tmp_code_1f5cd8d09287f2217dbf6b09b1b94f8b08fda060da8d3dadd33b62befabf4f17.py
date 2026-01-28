code = """import json
import re

# Load data from files
civic_docs_file = locals()['var_functions.query_db:34']
funding_file = locals()['var_functions.query_db:8']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Check if this line mentions completion in 2022
        if 'Construction was completed' in line and '2022' in line:
            # Look backwards up to 5 lines for the project name
            for j in range(max(0, i-5), i):
                proj_line = lines[j].strip()
                # Skip empty lines and lines starting with parentheses (metadata)
                if proj_line and not proj_line.startswith('(') and len(proj_line) < 150:
                    # Check if it's park-related
                    lower_proj = proj_line.lower()
                    if 'park' in lower_proj or 'playground' in lower_proj:
                        park_projects_2022.add(proj_line)
                        break

# Find funding matches
matches = []
total_funding = 0

for park_proj in park_projects_2022:
    # Try exact match first
    found = False
    for fund in funding_data:
        if fund['Project_Name'] == park_proj:
            amount = int(fund['Amount'])
            matches.append({'project': park_proj, 'amount': amount})
            total_funding += amount
            found = True
            break
    
    # If no exact match, try partial match
    if not found:
        for fund in funding_data:
            fund_name_lower = fund['Project_Name'].lower()
            park_proj_lower = park_proj.lower()
            # Check if one contains the other
            if park_proj_lower in fund_name_lower or fund_name_lower in park_proj_lower:
                amount = int(fund['Amount'])
                matches.append({'project': fund['Project_Name'], 'amount': amount})
                total_funding += amount
                break

result = {
    'park_projects': list(park_projects_2022),
    'funding_matches': matches,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'has_funding': False, 'has_civic': False}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
