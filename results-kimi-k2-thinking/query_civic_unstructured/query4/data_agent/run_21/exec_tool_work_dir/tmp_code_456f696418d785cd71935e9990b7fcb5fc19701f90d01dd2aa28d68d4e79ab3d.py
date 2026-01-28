code = """import json, re, os

# Get file paths from stored results
funding_file = locals()['var_functions.query_db:48']
civic_file = locals()['var_functions.query_db:2']

# Read funding data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Read civic documents
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_lookup = {}
for r in funding_records:
    funding_lookup[r['Project_Name']] = int(r['Amount'])

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Find lines with Spring 2022
    for i, line in enumerate(lines):
        if 'Spring 2022' in line:
            # Look backwards for project name
            for j in range(i-1, max(0, i-4), -1):
                prev_line = lines[j].strip().replace('•', '')
                if prev_line and len(prev_line) > 5:
                    # Check if it looks like a project name
                    if any(k in prev_line.lower() for k in ['project', 'improvements', 'repairs', 'construction']):
                        spring_projects.add(prev_line)
                        break

# Match projects
matched = {}
for proj in spring_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
    else:
        # Try fuzzy match
        for fproj, amt in funding_lookup.items():
            if proj.lower().split('(')[0].strip() == fproj.lower().split('(')[0].strip():
                matched[fproj] = amt
                break

# Calculate result
total_projects = len(matched)
total_funding = sum(matched.values())

final_result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'project_list': list(matched.keys())
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
