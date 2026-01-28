code = """import json
import re

# Read MongoDB data
mongo_file = open('/tmp/tmp9z4c2iv0.json', 'r')
mongo_docs = json.load(mongo_file)
mongo_file.close()

# Read funding data
funding_file = open('/tmp/tmps9c7b2d8.json', 'r')
funding_recs = json.load(funding_file)
funding_file.close()

# Create funding lookup dictionary
d = {}
for rec in funding_recs:
    d[rec['Project_Name']] = int(rec['Amount'])

# Find Spring 2022 projects
spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line:
                for j in range(i-1, max(i-8, -1), -1):
                    cand = lines[j].strip()
                    if cand and cand[0] != '(' and 'Schedule' not in cand:
                        if len(cand) > 5:
                            spring_projects.add(cand)
                            break

# Match with funding data
matches = []
for proj in spring_projects:
    if proj in d:
        matches.append({'name': proj, 'funding': d[proj]})

count = len(matches)
total = sum(m['funding'] for m in matches)

result = {'project_count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
