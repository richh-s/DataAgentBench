code = """import json

civic_docs_file = var_functions.query_db:0
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

all_park_projects = []
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'park' in text and '2022' in text and 'complet' in text:
        # Extract lines containing park
        for line in doc.get('text', '').split('\n'):
            if 'park' in line.lower():
                all_park_projects.append(line.strip())

unique_projects = []
seen = set()
for proj in all_park_projects:
    if proj not in seen:
        unique_projects.append(proj)
        seen.add(proj)

result = json.dumps({'count': len(unique_projects), 'projects': unique_projects[:20]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
