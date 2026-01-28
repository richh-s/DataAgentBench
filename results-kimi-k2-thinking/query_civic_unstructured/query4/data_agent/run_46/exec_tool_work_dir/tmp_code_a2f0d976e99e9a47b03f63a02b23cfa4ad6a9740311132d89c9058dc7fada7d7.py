code = """import json, re

civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding = json.load(f)

print('Documents:', len(civic_docs), 'Funding records:', len(funding))

# Extract projects from text using simpler pattern matching
project_candidates = []

for doc in civic_docs:
    text = doc['text']
    # Look for sections with project names followed by schedule info
    blocks = re.findall(r'([A-Z][A-Za-z0-9 &\-]+?)(?=\n.*?Complete Design:\s*([A-Za-z0-9\- ]+))', text, re.DOTALL)
    for proj_name, date in blocks:
        proj_name = proj_name.strip()
        date = date.strip()
        if '2022' in date and ('Spring' in date or 'Mar' in date or 'Apr' in date or 'May' in date):
            clean_name = re.sub(r'^[\u2022-]+\s*', '', proj_name)
            clean_name = re.sub(r'^cid:\d+\s*', '', clean_name)
            clean_name = ' '.join(clean_name.split())
            if clean_name and 'Agenda' not in clean_name and len(clean_name) < 100:
                project_candidates.append(clean_name)

# Remove duplicates
spring_projects = list(dict.fromkeys(project_candidates))
print('Spring 2022 projects found:', len(spring_projects))
for p in spring_projects:
    print(' ', p)

# Build funding map
funding_map = {}
for f in funding:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

# Match projects with funding
matched = []
total_funding = 0

for proj in spring_projects:
    direct_match = None
    for fund_name in funding_map:
        if proj == fund_name or proj in fund_name or fund_name in proj:
            direct_match = fund_name
            break
    
    if direct_match:
        matched.append({'project': proj, 'funding': funding_map[direct_match]})
        total_funding += funding_map[direct_match]
    else:
        # Try cleaning names for match
        proj_clean = re.sub(r'[^A-Za-z0-9]', '', proj).lower()
        for fund_name, amount in funding_map.items():
            fund_clean = re.sub(r'[^A-Za-z0-9]', '', fund_name).lower()
            if proj_clean in fund_clean or fund_clean in proj_clean:
                matched.append({'project': proj, 'funding': amount, 'matched_to': fund_name})
                total_funding += amount
                break

print('Matched projects:', len(matched))
print('Total funding:', total_funding)

result = {'count': len(matched), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
