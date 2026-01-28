code = """import json

# Load data from temp files
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Data loaded')

# Find park projects from 2022 in civic docs
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'completed' in text.lower() and '2022' in text and 'park' in text.lower():
        for line in text.split('\n'):
            line_lower = line.lower()
            if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
                if len(line) > 10:
                    projects.append(line.strip())

# Check funding for park projects
total = 0
found = []
for record in funding:
    name = record['Project_Name'].lower()
    if 'park' in name:
        if 'bluffs park shade' in name:
            total += int(record['Amount'])
            found.append(record['Project_Name'])
        elif 'marie canyon green' in name:
            total += int(record['Amount'])
            found.append(record['Project_Name'])
        elif 'broad beach' in name and 'water quality' in name:
            total += int(record['Amount'])
            found.append(record['Project_Name'])
        elif 'point dume' in name:
            total += int(record['Amount'])
            found.append(record['Project_Name'])

result = {'total': total, 'count': len(found), 'projects': found}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
