code = """import json
import re

civic_path = locals()['var_function-call-2424790631309893722']
funding_path = locals()['var_function-call-2424790631309895007']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

projects = []
bullet = chr(190)

for doc in civic_docs:
    text = doc['text']
    parts = text.split(bullet)
    
    for i in range(1, len(parts)):
        details = parts[i]
        prev_chunk = parts[i-1].strip()
        if not prev_chunk:
            continue
            
        lines = prev_chunk.split('\n')
        project_name = None
        for line in reversed(lines):
            line = line.strip()
            if not line:
                continue
            if 'Capital Improvement Projects' in line:
                continue
            if 'Agenda Item' in line:
                continue
            if line.startswith('Page'):
                continue
            if line.endswith(':'):
                line = line[:-1]
            project_name = line
            break
        
        if not project_name:
            continue
            
        start_date = None
        # Use simple string find or simple regex without r-string if possible
        # Begin Construction:
        match = re.search('Begin Construction:\\s*(.*)', details, re.IGNORECASE)
        if match:
            start_date = match.group(1).strip()
            
        if start_date:
            projects.append({'name': project_name, 'date': start_date})

unique_projects = {}
for p in projects:
    unique_projects[p['name']] = p['date']

target_names = []
spring_keywords = ['March', 'April', 'May', 'Spring']

for name, date_str in unique_projects.items():
    if '2022' in date_str:
        is_spring = False
        for kw in spring_keywords:
            if kw.lower() in date_str.lower():
                is_spring = True
                break
        if is_spring:
            target_names.append(name)

total_funding = 0
count = 0
matched = []
unmatched = []

funding_map = {}
for rec in funding_data:
    p_name = rec['Project_Name'].strip()
    amt = int(rec['Amount'])
    if p_name in funding_map:
        funding_map[p_name] += amt
    else:
        funding_map[p_name] = amt

for name in target_names:
    if name in funding_map:
        total_funding += funding_map[name]
        count += 1
        matched.append(name)
    else:
        unmatched.append(name)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'total_funding': total_funding,
    'matched': matched,
    'unmatched': unmatched
}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json'}

exec(code, env_args)
