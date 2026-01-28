code = """import json, re

# Load data from file paths
civic_docs = json.load(open('tmpw8a01a0z.json', 'r'))
funding = json.load(open('tmptjtu3_1d.json', 'r'))

print('Loaded data')

# Look for park projects completed in 2022
projects = []
for doc in civic_docs:
    txt = doc.get('text', '')
    if 'completed' in txt.lower() and '2022' in txt and 'park' in txt.lower():
        lines = txt.split('\n')
        for line in lines:
            if 'completed' in line.lower() and '2022' in line and 'park' in line.lower():
                if len(line.strip()) > 10:
                    projects.append(line.strip())

print('Found', len(projects), 'projects')

# Check funding for park projects
funding_dict = {f['Project_Name'].lower(): int(f['Amount']) for f in funding}

total = 0
matched = []
for f in funding:
    name = f['Project_Name'].lower()
    amt = int(f['Amount'])
    if 'bluffs park' in name and 'shade' in name:
        total += amt
        matched.append((f['Project_Name'], amt))
    elif 'broad beach' in name and 'water quality' in name:
        total += amt
        matched.append((f['Project_Name'], amt))
    elif 'point dume' in name and 'walkway' in name:
        total += amt
        matched.append((f['Project_Name'], amt))

result = {'total': total, 'matched': matched, 'count': len(projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
