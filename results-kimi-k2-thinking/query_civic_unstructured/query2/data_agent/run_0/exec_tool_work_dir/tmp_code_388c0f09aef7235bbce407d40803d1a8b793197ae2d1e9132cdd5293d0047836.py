code = """import json

# Load civic documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Find projects that mention park, completion, and 2022 in the same document
park_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    # Look for park-related projects
    if 'park' in text.lower():
        # Split into lines and look for completion markers near park project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 0:
                # Check if this might be a project name with park in it
                if 'park' in line.lower() and len(line) < 100:
                    # Look ahead for completion status
                    for j in range(i, min(i+10, len(lines))):
                        ahead_line = lines[j].strip().lower()
                        if 'completed' in ahead_line and '2022' in ahead_line:
                            park_projects_2022.append(line)
                            break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Load funding records
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Match funding records
total_funding = 0
matched = []

for project in park_projects_2022:
    proj_lower = project.lower()
    for fund in funding_records:
        fund_name = fund['Project_Name'].lower()
        # Match if project name is contained in funding name or vice versa
        if proj_lower in fund_name or fund_name in proj_lower:
            amount = int(fund['Amount'])
            total_funding += amount
            matched.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': amount
            })

result = {
    'total_funding': total_funding,
    'matched_projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
