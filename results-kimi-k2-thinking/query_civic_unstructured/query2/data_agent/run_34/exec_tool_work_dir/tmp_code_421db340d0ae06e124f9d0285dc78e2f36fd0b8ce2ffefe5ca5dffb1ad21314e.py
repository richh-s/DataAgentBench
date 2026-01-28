code = """import json
import re

civic_docs_file = var_functions.query_db:0
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        clean_line = line.strip()
        if 'park' in clean_line.lower() and len(clean_line) > 5:
            for j in range(i, min(i+15, len(lines))):
                next_line = lines[j].strip().lower()
                if 'completed' in next_line and '2022' in next_line:
                    date_match = re.search('\w+\s+2022', next_line, re.IGNORECASE)
                    if date_match:
                        park_projects.append({'name': clean_line, 'date': date_match.group()})
                        break

unique_projects = []
seen_names = set()
for proj in park_projects:
    name = proj['name']
    if name not in seen_names:
        unique_projects.append(proj)
        seen_names.add(name)

result = {'count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
