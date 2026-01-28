code = """import json
import re

mongo_file = open(var_functions.query_db:14, 'r')
mongo_docs = json.load(mongo_file)
mongo_file.close()

funding_file = open(var_functions.query_db:4, 'r')
funding_records = json.load(funding_file)
funding_file.close()

print('Loaded data')

# Extract projects starting in Spring 2022
spring_projects = []

key_phrases = ['Spring 2022', 'Spring/Summer 2022', 'Begin Construction: Spring 2022']

for doc in mongo_docs:
    text = doc.get('text')
    if not text:
        continue
        
    for phrase in key_phrases:
        if phrase in text:
            lines = text.splitlines()
            for i, line in enumerate(lines):
                if phrase in line:
                    # Look back for project name
                    for j in range(i-1, max(i-10, -1), -1):
                        prev = lines[j].strip()
                        if prev and not prev.startswith('(') and not prev.startswith('Page'):
                            if len(prev) > 5 and 'Schedule' not in prev:
                                spring_projects.append(prev)
                                break

print('Unique projects found: ' + str(len(set(spring_projects))))
print(list(set(spring_projects)))

# Get funding amounts
funding_dict = {r['Project_Name']: int(r['Amount']) for r in funding_records}

funded = []
for proj in set(spring_projects):
    if proj in funding_dict:
        funded.append({'name': proj, 'amount': funding_dict[proj]})

print('With funding: ' + str(len(funded)))
print(funded)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
