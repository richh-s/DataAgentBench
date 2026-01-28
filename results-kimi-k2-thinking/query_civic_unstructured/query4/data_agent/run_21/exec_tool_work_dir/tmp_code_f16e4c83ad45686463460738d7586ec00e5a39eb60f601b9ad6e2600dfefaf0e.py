code = """import json
import re

# Load data from the variables stored by previous tool calls
funding_path = var_functions.query_db_12
civic_path = var_functions.query_db_2

# Load funding records
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_records)} funding records and {len(civic_docs)} civic documents")

# Build funding lookup by project name
funding_lookup = {}
for record in funding_records:
    proj_name = record['Project_Name'].strip()
    funding_lookup[proj_name] = {
        'amount': int(record['Amount']),
        'source': record['Funding_Source']
    }

print(f"Created funding lookup with {len(funding_lookup)} entries")

# Find Spring 2022 projects in civic documents
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project names and Spring 2022 mentions in proximity
    potential_projects = []
    for line in lines:
        line = line.strip()
        # Look for project names (title case lines with project keywords)
        if line and len(line) < 150:
            if any(word in line.lower() for word in ['project', 'improvements', 'repairs', 'repaving', 'installation', 'construction', 'upgrades']):
                potential_projects.append(line.replace('•', '').strip())
    
    # Look for Spring 2022 mentions in the document
    spring_mentions = []
    for i, line in enumerate(lines):
        if 'Spring 2022' in line or '2022-Spring' in line or ('2022' in line and 'Spring' in line):
            spring_mentions.append((i, line.strip()))
    
    # If we found Spring 2022 and there are potential projects in the doc, add them
    if spring_mentions and potential_projects:
        # Add the most recent project before each Spring 2022 mention
        for spring_line_num, spring_line in spring_mentions:
            # Look backwards for the nearest project name
            for i in range(spring_line_num - 1, max(0, spring_line_num - 10), -1):
                if i < len(lines) and lines[i].strip() in potential_projects:
                    spring_2022_projects.add(lines[i].strip())
                    break

print(f"Found {len(spring_2022_projects)} unique Spring 2022 projects in documents")

# Match projects with funding data
matched_projects = {}

for proj_name in spring_2022_projects:
    # Direct match
    if proj_name in funding_lookup:
        matched_projects[proj_name] = funding_lookup[proj_name]
    else:
        # Fuzzy matching
        for funding_proj, funding_info in funding_lookup.items():
            if (funding_proj.lower() in proj_name.lower() or 
                proj_name.lower() in funding_proj.lower()):
                matched_projects[funding_proj] = funding_info
                break

print(f"Matched {len(matched_projects)} projects with funding data")

# Calculate totals
total_count = len(matched_projects)
total_funding = sum(info['amount'] for info in matched_projects.values())

# Prepare output
output = {
    'total_projects': total_count,
    'total_funding': total_funding,
    'projects': matched_projects
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records'}

exec(code, env_args)
