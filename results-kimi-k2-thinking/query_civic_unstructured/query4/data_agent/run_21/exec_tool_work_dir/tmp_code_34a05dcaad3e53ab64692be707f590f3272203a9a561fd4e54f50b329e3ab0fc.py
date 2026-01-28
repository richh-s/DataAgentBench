code = """import json
import re
import os

# Load funding data
with open(var_functions.query_db_84, 'r') as f:
    funding_records = json.load(f)

# Load civic documents with Spring 2022
with open(var_functions.query_db_74, 'r') as f:
    spring_docs = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[project_name] = amount

# Find Spring 2022 projects in civic documents
spring_2022_projects = set()

for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Look backwards for project name (up to 4 lines back)
            for j in range(i-1, max(0, i-4), -1):
                prev_line = lines[j].strip()
                # Remove bullet points and clean
                prev_line = prev_line.replace('•', '').replace('·', '').strip()
                
                # Skip empty lines
                if not prev_line:
                    continue
                
                # Check if this looks like a project name
                project_keywords = ['project', 'improvements', 'repairs', 'construction', 'installation', 'upgrades', 'renovation', 'replacement']
                has_keyword = any(keyword in prev_line.lower() for keyword in project_keywords)
                
                # Check if line is reasonable length for a project name
                if 5 < len(prev_line) < 200 and has_keyword:
                    spring_2022_projects.add(prev_line)
                    break

# Match projects with funding data
matched_projects = {}
for spring_proj in spring_2022_projects:
    # Direct match
    if spring_proj in funding_lookup:
        matched_projects[spring_proj] = funding_lookup[spring_proj]
    else:
        # Try base name match (without parentheses suffixes)
        base_spring = spring_proj.split('(')[0].strip().lower()
        for fund_proj, amount in funding_lookup.items():
            base_fund = fund_proj.split('(')[0].strip().lower()
            if base_spring == base_fund:
                matched_projects[fund_proj] = amount
                break

# Calculate totals
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print('='*60)
print('SPRING 2022 PROJECTS: %d' % total_projects)
print('TOTAL FUNDING: $%d' % total_funding)
print('='*60)

for proj_name, amount in matched_projects.items():
    print('• %s: $%d' % (proj_name, amount))

result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'projects': [{'name': name, 'funding': amt} for name, amt in matched_projects.items()]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
