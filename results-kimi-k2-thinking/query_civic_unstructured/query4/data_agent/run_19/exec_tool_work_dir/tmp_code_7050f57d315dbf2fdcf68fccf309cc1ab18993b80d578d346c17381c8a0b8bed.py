code = """import json

# Load data from files
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)
with open('/tmp/tmp8j8x8g9f.json', 'r') as f:
    funding_data = json.load(f)

project_names = set()

# Find Spring 2022 project names
for doc in civic_docs:
    text = doc.get('text', '').lower()
    pos = 0
    while True:
        pos = text.find('spring 2022', pos)
        if pos == -1:
            break
        context = doc.get('text', '')[max(0,pos-500):pos]
        for line in reversed(context.split('\n')):
            line = line.strip()
            if line and len(line)>10 and not line.startswith('(') and 'Page' not in line:
                if 'Capital Improvement' not in line and 'Project Schedule' not in line:
                    if not line.startswith('cid:') and 'Project Description' not in line:
                        project_names.add(line)
                        break
        pos += 1

# Calculate total funding
total = 0
for project in project_names:
    p = project.lower()
    for f in funding_data:
        if p in f['Project_Name'].lower() or f['Project_Name'].lower() in p:
            total += int(f['Amount'])
            break

result = {'project_count': len(project_names), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
