code = """import json
import re

# Load data
with open('var_functions.query_db:0', 'r') as f:
    funding = json.load(f)
with open('var_functions.query_db:1', 'r') as f:
    docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Find projects
projects = set()
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)') + 38
        section = text[start:]
        
        # Find section boundary
        boundary = min([i for i in [section.find('Capital Improvement Projects (Construction)'), 
                             section.find('Capital Improvement Projects (Not Started)'),
                             section.find('Disaster Recovery Projects')] if i > 0] or [len(section)])
        section = section[:boundary]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) < 5: continue
            if line[0] in '(-•' or line.startswith('('): continue
            if any(x in line for x in ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']): continue
            if line in funding_lookup:
                projects.add(line)

result = json.dumps({'count': len(projects), 'projects': sorted(list(projects))})
print('__RESULT__')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
