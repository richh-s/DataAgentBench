code = """import json

funding_key = 'var_functions.query_db:6'
funding_data = locals()[funding_key]

if type(funding_data) is str and funding_data.endswith('.json'):
    with open(funding_data) as f:
        funding_data = json.load(f)

civic_key = 'var_functions.query_db:8'
civic_docs = locals()[civic_key]

if type(civic_docs) is str and civic_docs.endswith('.json'):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
                projects_2022.append(line)

unique_projects = list(set(projects_2022))

total = 0
for proj in unique_projects:
    if proj in funding_map:
        total += funding_map[proj]

result = {"total_funding": total}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
