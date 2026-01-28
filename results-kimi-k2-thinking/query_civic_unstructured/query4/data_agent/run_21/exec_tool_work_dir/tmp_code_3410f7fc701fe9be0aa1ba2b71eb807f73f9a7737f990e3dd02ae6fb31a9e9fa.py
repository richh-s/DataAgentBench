code = """import json
import re

# Load data from files
funding_data = []
civic_data = []

# Read funding records
funding_file = var_functions.query_db_48
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents
 civic_file = var_functions.query_db_2
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Create funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find Spring 2022 projects
spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for Spring 2022 mentions and extract project names
    for i, line in enumerate(lines):
        if 'Spring 2022' in line:
            # Look backwards for project name
            for j in range(i-1, max(-1, i-4), -1):
                potential_name = lines[j].strip().replace('•', '').replace('·', '')
                # Check if it's a reasonable project name
                if 5 < len(potential_name) < 150:
                    # Look for project keywords or title case
                    has_keyword = any(k in potential_name.lower() for k in ['project', 'improvements', 'repairs', 'construction', 'installation'])
                    if has_keyword:
                        spring_projects.append(potential_name)
                        break

# Get unique projects
unique_spring = list(set(spring_projects))

print(f"Found {len(unique_spring)} unique Spring 2022 projects")

# Match with funding data
matches = []
total_funding = 0

for spring_proj in unique_spring:
    # Direct match
    if spring_proj in funding_dict:
        amount = funding_dict[spring_proj]
        matches.append({'name': spring_proj, 'funding': amount})
        total_funding += amount
    else:
        # Try matching base name
        base_spring = spring_proj.split('(')[0].strip()
        for fund_proj, amount in funding_dict.items():
            base_fund = fund_proj.split('(')[0].strip()
            if base_spring.lower() == base_fund.lower():
                matches.append({'name': fund_proj, 'funding': amount})
                total_funding += amount
                break

# Output results
result = {
    'total_projects': len(matches),
    'total_funding': total_funding,
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
