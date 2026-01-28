code = """import json
import re

# Load data files
civic_docs_path = locals()['var_functions.query_db:5']
funding_path = locals()['var_functions.query_db:20']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding dictionary
funding_dict = {}
for r in funding_data:
    name = r['Project_Name']
    amt = int(r['Amount'])
    funding_dict[name] = funding_dict.get(name, 0) + amt

# Extract projects with Spring 2022 dates
spring_2022_names = set()

for doc in civic_docs:
    txt = doc['text']
    lines = txt.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if len(line) == 0 or len(line) > 100:
            i += 1
            continue
        
        # Skip headers
        if any(x in line for x in ['Projects (', 'Page', 'To:', 'From:', 'Subject:', 'Date:', 'Updates:', 'Schedule:']) or line.isupper():
            i += 1
            continue
        
        # Look ahead for context
        context = ' '.join(lines[max(0,i-3):min(len(lines),i+12)])
        
        # Check if this is Spring 2022
        has_2022 = '2022' in context
        has_spring = any(s in context.lower() for s in ['spring', 'march', 'april', 'may'])
        
        if has_2022 and has_spring:
            # Verify it's a project by checking for project indicators nearby
            if 'Project Schedule:' in context or 'Updates:' in context or '(cid:' in context:
                spring_2022_names.add(line)
        
        i += 1

# Match projects to funding
matched = {}
for proj in spring_2022_names:
    proj_lower = proj.lower()
    for funded in funding_dict:
        funded_lower = funded.lower()
        # Match if project name appears in funded name or vice versa
        if proj_lower in funded_lower or funded_lower in proj_lower:
            matched[proj] = funding_dict[funded]
            break
        # Or match if they share key terms
        proj_words = [w for w in proj_lower.split() if len(w) > 4]
        for word in proj_words:
            if word in funded_lower and len(word) > 5:
                matched[proj] = funding_dict[funded]
                break
        if proj in matched:
            break

# Calculate totals
total_count = len(matched)
total_funds = sum(matched.values())

output = {
    'total_projects': total_count,
    'total_funding': total_funds,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
