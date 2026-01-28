code = """import json
civic_path = locals()['var_functions.query_db:5']
funding_path = locals()['var_functions.query_db:22']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)

disaster_names = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10 and (line.find('(FEMA Project)') >= 0 or line.find('(CalOES Project)') >= 0 or line.find('(CalJPIA Project)') >= 0):
            for j in range(i, min(i+4, len(lines))):
                if lines[j].find('2022') >= 0:
                    disaster_names.append(line)
                    break

total = 0
for item in funding:
    pname = item['Project_Name']
    for dname in disaster_names:
        base = dname.split('(')[0].strip()
        if pname.startswith(base):
            total += int(item['Amount'])

print('__RESULT__:')
print(json.dumps({'total_funding': total}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json'], 'var_functions.execute_python:16': {'funding_type': "<class 'list'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'funding_count': 10, 'civic_is_file_path': 'yes'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_count': 10}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'funding_records': 500, 'civic_documents': 5}}

exec(code, env_args)
