code = """import json
import re

# Read data
mongo_path = locals()['var_functions.query_db:14']
funding_path = locals()['var_functions.query_db:4']

mongo_docs = json.loads(open(mongo_path).read())
funding_records = json.loads(open(funding_path).read())

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

# Extract Spring 2022 projects
spring_projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        # Look for project schedule sections
        sections = re.split(r'\n\s*\n', text)
        for section in sections:
            if 'Begin Construction' in section and '2022' in section and 'Spring' in section:
                lines = section.split('\n')
                for i, line in enumerate(lines):
                    if 'Begin Construction' in line and 'Spring' in line:
                        # Look up to 5 lines back for project name
                        for j in range(max(0, i-5), i):
                            candidate = lines[j].strip()
                            if candidate and not candidate.startswith('(') and len(candidate) > 10:
                                spring_projects.append(candidate)
                                break

# Deduplicate
spring_projects = list(set(spring_projects))

# Match with funding data
result_projects = []
for proj in spring_projects:
    if proj in funding_lookup:
        result_projects.append({'name': proj, 'funding': funding_lookup[proj]})

# Calculate totals
total_count = len(result_projects)
total_funding = sum(p['funding'] for p in result_projects)

# Create output
output = 'Projects: ' + str(total_count) + ', Total Funding: $' + str(total_funding)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
