code = """import json

civic_docs = var_functions.query_db:5
if isinstance(civic_docs, str):
    civic_docs = json.load(open(civic_docs))

funding = var_functions.query_db:6
if isinstance(funding, str):
    funding = json.load(open(funding))

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for completed park projects in 2022
    if 'Park' in text and 'completed' in text.lower() and '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if 'Park' in line and len(line) > 5:
                # Skip headers and metadata
                if any(word in line for word in ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda']):
                    continue
                if line.startswith('('):
                    continue
                # Check completion status in following lines
                next_lines = '\n'.join(lines[i:i+10])
                if 'completed' in next_lines.lower() and '2022' in next_lines:
                    park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Try to find funding for these projects
total_funding = 0
funded_projects = []

for project_name in unique_projects:
    for fund_record in funding:
        # Check for exact or partial match
        fund_name = fund_record.get('Project_Name', '')
        if project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower():
            amount = int(fund_record.get('Amount', 0))
            total_funding += amount
            funded_projects.append({
                'project': project_name,
                'funded_as': fund_name,
                'amount': amount
            })

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': unique_projects,
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'funded_projects': funded_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
