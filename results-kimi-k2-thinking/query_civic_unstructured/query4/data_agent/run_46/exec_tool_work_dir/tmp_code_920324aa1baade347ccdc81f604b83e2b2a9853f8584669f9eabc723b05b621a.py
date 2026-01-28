code = """import json, re, os

# Access file paths from storage
civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

print(f'Documents: {len(civic_docs)}, Funding records: {len(funding)}')

# Simple approach: Look for Spring 2022 in the text and extract project names
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project blocks that mention Spring 2022
    # Projects are often followed by schedule info
    
    # Find all potential project names followed by schedule with 2022-Spring
    pattern = r'([A-Z][A-Za-z0-9 &\-]+?(?:Project|Improvements|Repairs|Drainage|Structure))[^\n]*\n[^\n]*2022[-\s]?(?:Spring|Mar|Apr|May)'
    
    matches = re.findall(pattern, text)
    for proj_name in matches:
        proj_name = proj_name.strip()
        if len(proj_name) > 10 and 'Agenda' not in proj_name:
            spring_projects.append(proj_name)

# Remove duplicates while preserving order
unique_spring_projects = []
for p in spring_projects:
    if p not in unique_spring_projects:
        unique_spring_projects.append(p)

print(f'Found {len(unique_spring_projects)} unique Spring 2022 projects')
for p in unique_spring_projects:
    print(f'  {p}')

# Build funding lookup - sum amounts for each project name
funding_lookup = {}
for record in funding:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

print(f'Funding lookup has {len(funding_lookup)} project names')

# Match projects with funding
matched = []
total_funding = 0

for project in unique_spring_projects:
    # Direct match
    if project in funding_lookup:
        matched.append({
            'project': project,
            'funding': funding_lookup[project]
        })
        total_funding += funding_lookup[project]
    else:
        # Try substring match
        for fund_name, amount in funding_lookup.items():
            if project in fund_name or fund_name in project:
                matched.append({
                    'project': project,
                    'funding': amount,
                    'matched_with': fund_name
                })
                total_funding += amount
                break

print(f'Matched {len(matched)} projects with funding')
print(f'Total funding: ${total_funding:,}')

result = {
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

output = json.dumps(result)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}}

exec(code, env_args)
