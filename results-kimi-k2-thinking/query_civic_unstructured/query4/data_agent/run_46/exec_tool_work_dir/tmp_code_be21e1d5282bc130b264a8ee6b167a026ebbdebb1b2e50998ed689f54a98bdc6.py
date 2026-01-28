code = """import json, re
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']
with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding = json.load(f)
print('Loaded docs:', len(civic_docs), 'funding records:', len(funding))
projects = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and 'Spring' in text:
        lines = text.split('\n')
        for i,line in enumerate(lines):
            line = line.strip()
            if '2022-Spring' in line or 'Spring 2022' in line:
                for j in range(i-1, max(-1, i-3), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) > 10 and not prev.startswith('cid:'):
                        clean = re.sub(r'^[\u2022\-]+\s*', '', prev)
                        clean = re.sub(r'^cid:\d+\s*', '', clean)
                        clean = ' '.join(clean.split())
                        if clean and 'Agenda' not in clean and len(clean) < 100:
                            projects.append(clean)
                            break
projects = list(dict.fromkeys(projects))
print('Spring 2022 projects:', projects)
funding_map = {}
for f in funding:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount
matched = []
total = 0
for proj in projects:
    if proj in funding_map:
        matched.append({'project': proj, 'funding': funding_map[proj]})
        total += funding_map[proj]
    else:
        for fname in funding_map:
            if proj in fname or fname in proj or re.sub(r'[^A-Za-z0-9]', '', proj) in re.sub(r'[^A-Za-z0-9]', '', fname):
                matched.append({'project': proj, 'funding': funding_map[fname], 'matched': fname})
                total += funding_map[fname]
                break
result = {'count': len(matched), 'total': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
