code = """import json, os, re

# Access stored results
funding_path = var_functions.query_db_48
civic_path = var_functions.query_db_2

# Load funding data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_path, 'r') as f:
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
    
    for i in range(len(lines)):
        line = lines[i]
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Look backwards for project name
            for j in range(i-1, max(0, i-3), -1):
                prev = lines[j].strip().replace('·', '').replace('•', '')
                if prev and len(prev) > 5:
                    # Check for project keywords
                    project_keywords = ['Project', 'Improvements', 'Repairs', 'Construction', 'Installation', 'Upgrades']
                    if any(kw.lower() in prev.lower() for kw in project_keywords):
                        spring_projects.add(prev)
                        break

# Match with funding data
matched = {}
for proj in spring_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
    else:
        # Try base name match
        for fproj, amt in funding_lookup.items():
            if proj.lower().split('(')[0].strip() == fproj.lower().split('(')[0].strip():
                matched[fproj] = amt
                break

# Calculate totals
total_projects = len(matched)
total_funding = sum(matched.values())

# Output results
result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'project_names': list(matched.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
