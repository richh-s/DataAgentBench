code = """import json
import re

# Load the data from files
with open('/tmp/tmp_3z7x6gk.json', 'r') as funding_f:
    funding_data = json.load(funding_f)
    
with open('/tmp/tmp_2z4l8jq.json', 'r') as spring_f:
    spring_docs = json.load(spring_f)

print('Loaded funding and spring docs')

# Find Spring 2022 projects
spring_projects = []

for doc in spring_docs:
    text_lines = doc['text'].split('\n')
    for i in range(len(text_lines)):
        line = text_lines[i].strip()
        if line and 'Spring' in line and '2022' in line:
            low_line = line.lower()
            if 'construction' in low_line or 'advertise' in low_line or 'begin' in low_line:
                # Find project name
                for j in range(i-1, max(-1, i-10), -1):
                    prev = text_lines[j].strip()
                    if prev and not prev.startswith('(') and not prev.startswith('•'):
                        bad = ['update', 'schedule', 'status', 'description', 'project']
                        if not any(b in prev.lower() for b in bad):
                            if len(prev) < 200:
                                spring_projects.append(prev)
                                break

unique_projects = list(set(spring_projects))
print('Unique Spring 2022 projects count: %d' % len(unique_projects))

# Build funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Calculate total funding
total_funding_amount = 0
for proj in unique_projects:
    if proj in funding_dict:
        total_funding_amount += funding_dict[proj]
    else:
        for funded_name, amount in funding_dict.items():
            if proj in funded_name or funded_name in proj:
                total_funding_amount += amount
                break

print('Total funding amount: %d' % total_funding_amount)

result = {
    'spring_2022_project_count': len(unique_projects), 
    'total_funding': total_funding_amount
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
