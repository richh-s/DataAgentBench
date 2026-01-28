code = """import json

# Simple approach - look for 2022-Spring directly in text
civic_file = locals()['var_functions.query_db:88']
funding_file = locals()['var_functions.query_db:90']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Build simple funding map
funding_map = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name and amount > 0:
        funding_map[name] = amount

# Count documents mentioning Spring 2022
doc_count = 0
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022-spring' in text or '2022-march' in text or '2022-april' in text or '2022-may' in text:
        doc_count += 1

print('Documents mentioning Spring 2022:', doc_count)

# Check for obvious project with Spring 2022 start
likely_spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Look for Spring 2022
    if '2022-spring' in lower_text or '2022-march' in lower_text:
        # Look for project names that contain years or are capitalized
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and ('2022' in line or (sum(1 for c in line if c.isupper()) > len(line) * 0.2)):
                if 'project' in line.lower() or 'improvements' in line.lower() or 'repairs' in line.lower():
                    if len(line) > 20:  # Likely a project name
                        likely_spring_projects.append(line)

print('Potential Spring 2022 projects:', len(set(likely_spring_projects)))

# Try finding funding matches
total_funding = 0
matched_count = 0

for proj in set(likely_spring_projects):
    # Exact match
    if proj in funding_map:
        total_funding += funding_map[proj]
        matched_count += 1
    else:
        # Base name match
        base = proj.split('(')[0].strip()
        if base in funding_map:
            total_funding += funding_map[base]
            matched_count += 1

print('Matched projects:', matched_count)
print('Total funding:', total_funding)
print('__RESULT__:')
print(json.dumps({'project_count': matched_count, 'total_funding': total_funding}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}], 'var_functions.list_db:82': ['civic_docs'], 'var_functions.list_db:84': ['civic_docs'], 'var_functions.query_db:86': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
