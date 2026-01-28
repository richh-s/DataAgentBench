code = """import json
import re

# Load data
civic_docs = json.load(open('/tmp/tmp1.json'))
funding_data = json.load(open('/tmp/tmp2.json'))

# Build funding map
funding_lookup = {}
for f in funding_data:
    funding_lookup[f['Project_Name']] = int(f['Amount'])

# Look for project schedules with Spring 2022
projects_2022_spring = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Find sequences like "Complete Design: Spring 2022" or similar
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and 'Spring' in line:
            # Look backward for project name
            proj_name = None
            for j in range(i-1, max(-1, i-4), -1):
                candidate = lines[j].strip()
                if candidate and len(candidate) > 10:
                    bad_markers = ['(', 'cid:', 'Updates:', 'Schedule:', 'Complete Design:', 'Begin Construction:']
                    if not any(m in candidate for m in bad_markers):
                        proj_name = candidate
                        break
            if proj_name:
                projects_2022_spring.append(proj_name)

# Remove duplicates
unique = list(dict.fromkeys(projects_2022_spring))

# Find matching funding
total = 0
matched = []
for proj in unique:
    if proj in funding_lookup:
        amt = funding_lookup[proj]
        total += amt
        matched.append({'name': proj, 'funding': amt})

result = {'count': len(matched), 'total_funding': total, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
