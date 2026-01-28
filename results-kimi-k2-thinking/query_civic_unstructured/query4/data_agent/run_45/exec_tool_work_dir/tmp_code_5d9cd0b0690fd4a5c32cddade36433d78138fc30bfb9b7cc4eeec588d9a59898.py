code = """import json

# Load civic documents to find Spring 2022 projects
docs_path = locals()['var_functions.query_db:60']
with open(docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:48']
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding_records), 'funding records')

# Build funding map for quick lookup
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name and amount > 0:
        funding_map[name] = amount
        base_name = name.split('(')[0].strip()
        if base_name != name:
            funding_map[base_name] = amount

# Find Spring 2022 projects in civic documents
spring_2022_projects = set()
spring_indicators = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if line looks like a project name
        if any(kw in line.upper() for kw in ['PROJECT', 'IMPROVEMENTS', 'REPAIRS']):
            upper_ratio = sum(1 for c in line if c.isupper()) / max(1, len([c for c in line if c.isalpha()]))
            if upper_ratio > 0.2:
                # Check context for Spring 2022
                context = ' '.join(lines[max(0,i-5):min(len(lines),i+6)])
                if any(ind in context for ind in spring_indicators):
                    spring_2022_projects.add(line.strip())

# Match with funding
matched = []
total = 0
for proj in spring_2022_projects:
    if proj in funding_map:
        amt = funding_map[proj]
        matched.append({'project': proj, 'amount': amt})
        total += amt
    else:
        base = proj.split('(')[0].strip()
        if base in funding_map:
            amt = funding_map[base]
            matched.append({'project': proj, 'amount': amt})
            total += amt

result = {'project_count': len(matched), 'total_funding': total, 'projects': matched}
print('Final result - Projects:', len(matched), 'Total funding:', total)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}]}

exec(code, env_args)
