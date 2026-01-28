code = """import json

funding_path = locals()['var_functions.query_db:8']
civic_path = locals()['var_functions.query_db:34']

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic = json.load(f)

park = []
for doc in civic:
    if 'text' in doc and 'Construction was completed' in doc['text'] and '2022' in doc['text']:
        lines = doc['text'].split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if 'park' in line.lower() or 'playground' in line.lower():
                for j in range(i+1, min(i+4, len(lines))):
                    if 'construction was completed' in lines[j].lower() and '2022' in lines[j]:
                        if line and not line.startswith('(') and len(line) < 150:
                            park.append(line)
                        break

park = list(set(park))
matches = []
total = 0

for p in park:
    for f in funding:
        if p == f['Project_Name'] or p.lower() in f['Project_Name'].lower() or f['Project_Name'].lower() in p.lower():
            matches.append({'project': f['Project_Name'], 'amount': int(f['Amount'])})
            total += int(f['Amount'])
            break

result = json.dumps({'projects': park, 'funding': matches, 'total': total})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'has_funding': False, 'has_civic': False}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
