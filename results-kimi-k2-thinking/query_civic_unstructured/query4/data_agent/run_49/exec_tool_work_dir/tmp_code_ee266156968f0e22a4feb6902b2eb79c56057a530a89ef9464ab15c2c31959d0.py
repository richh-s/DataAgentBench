code = """import json

civic_docs = json.load(open(var_functions.query_db:10))
funding_data = json.load(open(var_functions.query_db:7))

# Build funding dictionary
funding = {}
for rec in funding_data:
    funding[rec['Project_Name']] = int(rec['Amount'])

# Simple extraction - look for project names with 2022 in title
projects = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text):
        # Extract lines that look like project names
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 10 and any(word in line for word in ['Project', 'Improvements', 'Repairs', 'Drainage']):
                if line[0].isupper():
                    projects.append(line)

projects = list(set(projects))

# Match with funding
matched = []
for proj in projects:
    if proj in funding:
        matched.append({'name': proj, 'funding': funding[proj]})

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'total_funding': sum(p['funding'] for p in matched), 'projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
