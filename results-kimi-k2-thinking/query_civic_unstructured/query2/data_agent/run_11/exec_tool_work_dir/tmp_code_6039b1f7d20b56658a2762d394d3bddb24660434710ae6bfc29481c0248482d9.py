code = """import json

# Load data
civic_docs = json.load(open(var_functions.query_db:60))
funding = json.load(open(var_functions.query_db:48))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    if 'Park' in text and '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        for line in text.split('\n'):
            line = line.strip()
            if 'Park' in line and len(line) > 10:
                skip_words = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:']
                if not any(word in line for word in skip_words):
                    if not line.startswith('('):
                        park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Match with funding
funding_total = 0
matches = []

for proj in unique_projects:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            amount = int(rec.get('Amount',0))
            funding_total += amount
            matches.append([proj, name, amount])

result = {'project_count': len(unique_projects), 'total_funding': funding_total, 'projects': unique_projects, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
