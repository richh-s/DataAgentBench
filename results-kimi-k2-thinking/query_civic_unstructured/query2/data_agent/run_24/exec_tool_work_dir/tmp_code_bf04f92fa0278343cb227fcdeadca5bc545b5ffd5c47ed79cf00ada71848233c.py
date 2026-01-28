code = """import json, re
c_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Loaded data')

# Find park projects completed in 2022
projects = []
for doc in c_docs:
    text = doc.get('text', '')
    if '2022' in text and 'park' in text.lower():
        for line in text.split('\n'):
            if 'completed' in line.lower() and '2022' in line and 'park' in line.lower():
                if len(line.strip()) > 10:
                    projects.append(line.strip())

print('Found', len(projects), 'projects')

# Check for these specific park projects in funding
total = 0
matched = []
for f in funding:
    name = f['Project_Name'].lower()
    amt = int(f['Amount'])
    
    # Check specific park projects
    if 'bluffs park shade structure' == name:
        total += amt
        matched.append((f['Project_Name'], amt))
    elif 'marie canyon green streets' == name:
        total += amt
        matched.append((f['Project_Name'], amt))
    elif 'broad beach road water quality repair' == name:
        total += amt
        matched.append((f['Project_Name'], amt))
    elif 'point dume walkway repairs' == name:
        total += amt
        matched.append((f['Project_Name'], amt))

out = {'total': total, 'matched': matched, 'found_count': len(projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
