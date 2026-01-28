code = """import json
import re

# Load funding data
with open(var_functions.query_db_48, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
with open(var_functions.query_db_2, 'r') as f:
    civic_docs = json.load(f) if var_functions.query_db_2.endswith('.json') else var_functions.query_db_2

print('Loaded', len(funding_records), 'funding records and', len(civic_docs), 'civic docs')

# Build funding lookup
funding_lookup = dict((r['Project_Name'], int(r['Amount'])) for r in funding_records)

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Extract project names from lines containing Spring 2022
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Check previous lines for project name
                for j in range(i-1, max(0, i-4), -1):
                    prev = lines[j].strip().replace('•', '')
                    if prev and len(prev) < 150:
                        # Simple project detection
                        if any(k in prev.lower() for k in ['project', 'improvements', 'repairs']):
                            spring_projects.add(prev)
                            break

print('Found Spring 2022 projects:', len(spring_projects))

# Match with funding
matches = {}
for proj in spring_projects:
    if proj in funding_lookup:
        matches[proj] = funding_lookup[proj]
    else:
        # Try base name without suffix
        base_proj = proj.split('(')[0].strip()
        for fproj, amt in funding_lookup.items():
            if base_proj.lower() == fproj.split('(')[0].strip().lower():
                matches[fproj] = amt
                break

# Calculate results
result = {
    'projects': len(matches),
    'funding': sum(matches.values()),
    'names': list(matches.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
