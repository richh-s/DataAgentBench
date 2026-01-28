code = """import json

# Load the civic documents to extract Spring 2022 projects
civic_file = locals()['var_functions.query_db:60']
funding_file = locals()['var_functions.query_db:48']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create funding lookup map
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name and amount > 0:
        funding_map[name] = amount
        # Store base name
        base = name.split('(')[0].strip()
        if base not in funding_map:
            funding_map[base] = amount

# Find Spring 2022 projects
spring_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Spring 2022 indicators
    if '2022-Spring' not in text and '2022-March' not in text and '2022-April' not in text and '2022-May' not in text:
        continue
        
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Check if line looks like project name
        if 'PROJECT' not in line.upper() and 'IMPROVEMENTS' not in line.upper() and 'REPAIRS' not in line.upper():
            continue
            
        # Check uppercase ratio
        upper = sum(1 for c in line if c.isupper())
        alpha = sum(1 for c in line if c.isalpha())
        if alpha > 0 and upper / alpha > 0.2:
            spring_2022_projects.add(line)

# Match with funding
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    if project in funding_map:
        amt = funding_map[project]
        matched_projects.append({'project': project, 'amount': amt})
        total_funding += amt
    else:
        base = project.split('(')[0].strip()
        if base in funding_map:
            amt = funding_map[base]
            matched_projects.append({'project': project, 'amount': amt})
            total_funding += amt

# Prepare final answer
project_count = len(matched_projects)
total_funding_amount = total_funding

print('PROJECTS_FOUND:', project_count)
print('TOTAL_FUNDING:', total_funding_amount)

result = {'project_count': project_count, 'total_funding': total_funding_amount, 'sample_projects': matched_projects[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}]}

exec(code, env_args)
