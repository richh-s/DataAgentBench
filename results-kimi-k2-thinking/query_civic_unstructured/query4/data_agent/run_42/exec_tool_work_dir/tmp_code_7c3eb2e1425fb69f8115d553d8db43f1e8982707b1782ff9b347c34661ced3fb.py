code = """import json
import re

# Get file paths from locals
mongo_path = locals()['var_functions.query_db:14']
funding_path = locals()['var_functions.query_db:4']

# Load data
with open(mongo_path) as f:
    mongo_docs = json.load(f)
with open(funding_path) as f:
    funding = json.load(f)

print('Mongo docs:', len(mongo_docs))
print('Funding records:', len(funding))

# Extract project names
spring_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Find occurrences of Spring 2022
    if 'Spring 2022' in text:
        # Split by lines and look for patterns
        for line in text.split('\n'):
            if 'Begin Construction' in line and '2022' in line:
                # Find project name in previous lines
                idx = text.split('\n').index(line)
                for i in range(idx-1, max(0, idx-10), -1):
                    prev = text.split('\n')[i].strip()
                    if prev and not prev.startswith('(') and len(prev) > 5:
                        spring_projects.append(prev)
                        break

# Remove duplicates
spring_projects = list(set(spring_projects))
print('Spring projects:', spring_projects)

# Get funding amounts
funding_dict = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

results = []
total_funding = 0
for proj in spring_projects:
    if proj in funding_dict:
        amt = funding_dict[proj]
        results.append({'project': proj, 'funding': amt})
        total_funding += amt

print('Results:', results)
print('Total funding:', total_funding)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
