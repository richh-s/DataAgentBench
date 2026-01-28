code = """import json
f = open('/tmp/tmpyq7d3x4g.json', 'r')
civic_docs = json.load(f)
f.close()

f = open('/tmp/tmp8j8x8g9f.json', 'r')
funding = json.load(f)
f.close()

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    txt = text.lower()
    i = 0
    while True:
        i = txt.find('spring 2022', i)
        if i == -1:
            break
        start = max(0, i - 400)
        context = text[start:i]
        lines = context.split('\n')
        for line in reversed(lines):
            line = line.strip()
            if line and len(line) > 8 and not line.startswith('(') and 'Page' not in line and 'Capital Improvement' not in line and 'Project Schedule' not in line and 'Estimated Schedule' not in line:
                projects.append(line[:200])
                break
        i += 1

unique = []
seen = set()
for p in projects:
    if p not in seen:
        seen.add(p)
        unique.append(p)

total = 0
for project in unique:
    pl = project.lower()
    for f in funding:
        fn = f['Project_Name'].lower()
        if pl in fn or fn in pl:
            total += int(f['Amount'])
            break

print('__RESULT__:')
print(json.dumps({'count': len(unique), 'funding': total}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
