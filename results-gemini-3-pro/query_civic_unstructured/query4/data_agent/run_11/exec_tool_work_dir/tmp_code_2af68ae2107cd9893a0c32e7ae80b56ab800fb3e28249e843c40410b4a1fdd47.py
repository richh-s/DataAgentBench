code = """import json

funding_file = locals()['var_function-call-13662082539617429622']
docs_file = locals()['var_function-call-13662082539617429133']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(docs_file, 'r') as f:
    docs_data = json.load(f)

funding_map = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

projects = []
current_project = None
current_start_date = None

for doc in docs_data:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check for marker
        # Using single quotes
        if 'Updates:' in line or 'Project Description:' in line:
            # Find name
            j = i - 1
            while j >= 0:
                prev = lines[j].strip()
                if prev:
                    if current_project:
                        projects.append({'name': current_project, 'start': current_start_date})
                    current_project = prev
                    current_start_date = None
                    break
                j -= 1
        
        if current_project and 'Begin Construction:' in line:
            parts = line.split(':')
            if len(parts) > 1:
                current_start_date = parts[1].strip()

    if current_project:
        projects.append({'name': current_project, 'start': current_start_date})

target_dates = ['Spring 2022', 'March 2022', 'April 2022', 'May 2022']
matched = []
for p in projects:
    if p['start']:
        s = p['start'].lower()
        if any(t.lower() in s for t in target_dates):
            matched.append(p['name'])

total = 0
found = []
missing = []
for m in matched:
    if m in funding_map:
        total += funding_map[m]
        found.append(m)
    else:
        missing.append(m)

print('__RESULT__:')
print(json.dumps({'count': len(found), 'total_funding': total, 'projects': found, 'missing': missing}))"""

env_args = {'var_function-call-6849361195335581804': 'file_storage/function-call-6849361195335581804.json', 'var_function-call-6849361195335584623': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13662082539617429622': 'file_storage/function-call-13662082539617429622.json', 'var_function-call-13662082539617429133': 'file_storage/function-call-13662082539617429133.json'}

exec(code, env_args)
