code = """import json, re

# Load the civic documents
civic_docs_path = var_functions.query_db:5
civic_docs = json.load(open(civic_docs_path))

# Load the funding data
funding_path = var_functions.query_db:6
funding = json.load(open(funding_path))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) > 5 and not line.startswith('('):
                if 'Subject' not in line and 'Page' not in line and 'Item' not in line:
                    park_projects.append(line)

unique_parks = list(set(park_projects))

# Find funding for these projects
total_funding = 0
funding_matches = []

for proj in unique_parks:
    for rec in funding:
        name = rec.get('Project_Name', '')
        # Check for exact match or partial match
        if proj.lower() == name.lower() or proj.lower() in name.lower():
            amount = int(rec.get('Amount', 0))
            total_funding += amount
            funding_matches.append({'project': proj, 'funding_record': name, 'amount': amount})

print('__RESULT__:')
print(json.dumps({
    'projects': unique_parks,
    'count': len(unique_parks),
    'total_funding': total_funding,
    'funding_details': funding_matches
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
