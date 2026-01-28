code = """import json, re, os

# Load funding records from file
f_path = var_functions.query_db_84
funding = json.load(open(f_path))

# Load civic documents
s_path = var_functions.query_db_88
spring_docs = json.load(open(s_path))

# Build funding map
funding_map = {r['Project_Name']:int(r['Amount']) for r in funding}

# Spring 2022 project extraction
projects_found = set()

for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'Spring 2022' in line:
            for j in range(i-1, max(0, i-4), -1):
                prev = lines[j].strip().replace('•', '')
                if prev and 5 < len(prev) < 150:
                    keywords = ['project', 'improvements', 'repairs']
                    if any(k in prev.lower() for k in keywords):
                        projects_found.add(prev)
                        break

# Match projects
matched = {}
for proj in projects_found:
    if proj in funding_map:
        matched[proj] = funding_map[proj]
    else:
        base = proj.split('(')[0].strip().lower()
        for fproj, amt in funding_map.items():
            fbase = fproj.split('(')[0].strip().lower()
            if base == fbase:
                matched[fproj] = amt
                break

# Results
result = {'count': len(matched), 'funding': sum(matched.values())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)
