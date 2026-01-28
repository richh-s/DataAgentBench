code = """import json, re
civic_docs_file = var_functions.query_db:0
civic_docs = json.load(open(civic_docs_file))
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'park' in line.lower() and len(line) > 5:
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j].strip().lower()
                if 'construction was completed' in next_line and '2022' in next_line:
                    m = re.search(r'(\w+\s+2022)', next_line, re.IGNORECASE)
                    if m:
                        projects.append({'name': line, 'date': m.group(1)})
                        break

unique = []
seen = set()
for p in projects:
    if p['name'] not in seen:
        unique.append(p)
        seen.add(p['name'])

print('__RESULT__:')
print(json.dumps({'count': len(unique), 'projects': unique[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
