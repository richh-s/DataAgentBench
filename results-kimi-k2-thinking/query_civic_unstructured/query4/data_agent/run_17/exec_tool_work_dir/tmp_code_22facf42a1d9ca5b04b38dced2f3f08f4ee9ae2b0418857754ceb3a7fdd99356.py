code = """import json

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:5']))
funding = json.load(open(locals()['var_functions.query_db:20']))

# Simple check for Spring 2022 in text
spring_2022_projects = []
for doc in civic_docs:
    text = doc['text']
    if 'Spring' in text and '2022' in text:
        # Extract lines around Spring 2022 mentions
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line and 'Spring' in line:
                # Look backward for project name
                for j in range(i-1, max(-1, i-10), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) < 80 and not any(x in prev for x in ['Schedule:', 'Updates:', 'Page']):
                        spring_2022_projects.append(prev)
                        break

# Get unique projects
unique_projects = list(set(spring_2022_projects))

# Build funding dict
funding_dict = {}
for item in funding:
    name = item['Project_Name']
    amt = int(item['Amount'])
    if name in funding_dict:
        funding_dict[name] += amt
    else:
        funding_dict[name] = amt

# Match projects
matched = {}
for proj in unique_projects:
    proj_lower = proj.lower()
    for fund_name in funding_dict:
        if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
            matched[proj] = funding_dict[fund_name]
            break

result = {
    'project_count': len(matched),
    'total_funding': sum(matched.values()),
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'num_civic_docs': 5, 'num_funding_records': 500}}

exec(code, env_args)
