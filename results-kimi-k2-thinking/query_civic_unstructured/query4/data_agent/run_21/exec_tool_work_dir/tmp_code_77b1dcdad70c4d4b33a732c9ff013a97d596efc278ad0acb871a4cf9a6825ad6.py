code = """import json, os, re

# Load funding data directly
funding_file = var_functions.query_db_48
funding_data = json.load(open(funding_file))

# Build funding lookup
funding_lookup = dict((r['Project_Name'], int(r['Amount'])) for r in funding_data)

# Open civic documents file
spring_file = var_functions.query_db_74
spring_docs = json.load(open(spring_file))

# Find projects
found_projects = set()

for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        if 'Spring 2022' in lines[i]:
            for j in range(i-1, max(0, i-3), -1):
                prev = lines[j].strip()
                prev_clean = prev.replace('•', '').replace('·', '')
                if prev_clean and 5 < len(prev_clean) < 150:
                    kws = ['project', 'improvements', 'repairs', 'installation']
                    if any(k in prev_clean.lower() for k in kws):
                        found_projects.add(prev_clean)
                        break

# Match projects with funding
matched = dict()
for proj in found_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
    else:
        base_proj = proj.split('(')[0].strip().lower()
        for fund, amt in funding_lookup.items():
            base_fund = fund.split('(')[0].strip().lower()
            if base_proj == base_fund:
                matched[fund] = amt
                break

# Calculate results
total_proj = len(matched)
total_fund = sum(matched.values())

print('__RESULT__:', json.dumps({'count': total_proj, 'funding': total_fund, 'projects': list(matched.keys())[:20]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
