code = """import json, re

# Load the data
civic_docs_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:20']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding:
    name = item['Project_Name']
    amt = int(item['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amt

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc['text']
    if '2022' not in text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 80:
            continue
        
        if any(x in line for x in ['Projects (', 'Page', 'To:', 'From:', 'Subject:', 'Date:', 'Updates:', 'Schedule:']) or line.isupper():
            continue
        
        # Check surrounding context
        context = '\n'.join(lines[max(0,i-5):min(len(lines),i+10)])
        if '2022' in context and any(s in context.lower() for s in ['spring', 'march', 'april', 'may']):
            if 'Schedule:' in context or 'Updates:' in context:
                spring_projects.add(line)

# Match with funding
results = {}
for proj in spring_projects:
    proj_words = set(proj.lower().split())
    for funded in funding_lookup:
        funded_words = set(funded.lower().split())
        if len(proj_words.intersection(funded_words)) >= 2:
            results[proj] = funding_lookup[funded]
            break

total_projects = len(results)
total_funding = sum(results.values())

output = {'total_projects': total_projects, 'total_funding': total_funding, 'projects': results}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
