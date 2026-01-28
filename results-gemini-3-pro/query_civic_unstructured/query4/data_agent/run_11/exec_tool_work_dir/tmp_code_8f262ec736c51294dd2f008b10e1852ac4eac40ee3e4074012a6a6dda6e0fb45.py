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
    lines = doc['text'].split(chr(10))
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Check markers
        is_marker = False
        if 'Updates:' in line: is_marker = True
        if 'Project Description:' in line: is_marker = True
        
        if is_marker:
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
        
        if current_project:
            low_line = line.lower()
            if 'begin construction' in low_line:
                # find the part after the colon
                parts = line.split(':')
                if len(parts) > 1:
                    current_start_date = parts[1].strip()

    if current_project:
        projects.append({'name': current_project, 'start': current_start_date})

# Deduplicate by name, prioritizing the one with a start date if multiple
unique_projects = {}
for p in projects:
    name = p['name']
    start = p['start']
    if name not in unique_projects:
        unique_projects[name] = start
    else:
        # If we already have one, keep it unless it's None and new one is not
        if unique_projects[name] is None and start is not None:
            unique_projects[name] = start

target_dates = ['spring 2022', 'march 2022', 'april 2022', 'may 2022']
matched = []
for name, start in unique_projects.items():
    if start:
        s = start.lower()
        if any(t.lower() in s for t in target_dates):
            matched.append(name)

total = 0.0
found_list = []
missing_list = []

for m in matched:
    if m in funding_map:
        total += funding_map[m]
        found_list.append(m)
    else:
        # Check stripping?
        # Check funding_map keys
        if m.strip() in funding_map:
             total += funding_map[m.strip()]
             found_list.append(m)
        else:
             missing_list.append(m)

print('__RESULT__:')
debug_info = [p for p in projects if p['start']] # Show projects with start dates found
print(json.dumps({
    'count': len(found_list),
    'total_funding': total,
    'matched_projects': found_list,
    'missing_projects': missing_list,
    'debug_sample': debug_info[:5]
}))"""

env_args = {'var_function-call-6849361195335581804': 'file_storage/function-call-6849361195335581804.json', 'var_function-call-6849361195335584623': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13662082539617429622': 'file_storage/function-call-13662082539617429622.json', 'var_function-call-13662082539617429133': 'file_storage/function-call-13662082539617429133.json', 'var_function-call-15203628633396000415': {'count': 0, 'total_funding': 0.0, 'matched_projects': []}}

exec(code, env_args)
