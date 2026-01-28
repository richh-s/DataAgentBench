code = """import json
import re

# Load data
with open('var_functions.query_db:0', 'r') as f:
    funding = json.load(f)
with open('var_functions.query_db:1', 'r') as f:
    docs = json.load(f)

# Build funding lookup for amounts > 50000
funding_lookup = {}
for item in funding:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name']] = amount

# Find capital projects with design status
design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)') + 38
        section = text[start:]
        
        # Find end markers
        end_pos = float('inf')
        markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
        for marker in markers:
            pos = section.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
        
        if end_pos != float('inf'):
            section = section[:int(end_pos)]
        
        # Look for project names
        for line in section.split('\n'):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            if line[0] == '(' or line.startswith('-') or line.startswith('•'):
                continue
            skip_words = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']
            if any(word in line for word in skip_words):
                continue
            if line in funding_lookup:
                design_projects.add(line)

result = json.dumps({'count': len(design_projects), 'projects': sorted(list(design_projects))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
