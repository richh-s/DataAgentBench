code = """import json

# Load civic documents
civic_path = locals()['var_functions.query_db:60']
civic_docs = json.load(open(civic_path))
print('Loaded', len(civic_docs), 'civic documents')

# Load funding data
funding_path = locals()['var_functions.query_db:48']
funding_data = json.load(open(funding_path))
print('Loaded', len(funding_data), 'funding records')

# Create funding lookup map
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if name and amount > 0:
        funding_map[name] = amount
        base_name = name.split('(')[0].strip()
        if base_name not in funding_map:
            funding_map[base_name] = amount

# Find Spring 2022 projects in civic documents
spring_2022_projects = set()
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in civic_docs:
    text = doc.get('text', '')
    
    spring_document = False
    for pattern in spring_patterns:
        if pattern in text:
            spring_document = True
            break
    
    if not spring_document:
        continue
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        upper_count = sum(1 for c in line if c.isupper())
        total_alpha = sum(1 for c in line if c.isalpha())
        if total_alpha == 0:
            continue
        
        upper_ratio = upper_count / total_alpha
        
        line_upper = line.upper()
        if upper_ratio > 0.2 and ('PROJECT' in line_upper or 'IMPROVEMENTS' in line_upper or 'REPAIRS' in line_upper):
            spring_2022_projects.add(line)

# Match with funding data
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    if project in funding_map:
        amount = funding_map[project]
        matched_projects.append({'project_name': project, 'amount': amount})
        total_funding += amount
    else:
        base_project = project.split('(')[0].strip()
        if base_project in funding_map:
            amount = funding_map[base_project]
            matched_projects.append({'project_name': project, 'amount': amount})
            total_funding += amount

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects[:15]
}

print('Projects found:', len(matched_projects))
print('Total funding:', total_funding)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}]}

exec(code, env_args)
