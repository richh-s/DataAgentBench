code = """import json

# Load funding and civic documents data
funding = json.load(open('var_functions.query_db:0'))
docs = json.load(open('var_functions.query_db:1'))

# Create lookup for projects with funding > $50,000
funding_lookup = {}
for item in funding:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name']] = amount

# Find capital projects in design status
found_projects = set()

for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    start = text.find('Capital Improvement Projects (Design)') + 38
    section = text[start:]
    
    ends = []
    for boundary in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = section.find(boundary)
        if pos > 0:
            ends.append(pos)
    
    section_end = min(ends) if ends else len(section)
    section = section[:section_end]
    
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        if line.startswith('(') or line.startswith('-') or line.startswith('•'):
            continue
        
        skip_words = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']
        skip = False
        for word in skip_words:
            if word in line:
                skip = True
                break
        if skip:
            continue
        
        if line in funding_lookup:
            found_projects.add(line)

result = {
    'count': len(found_projects),
    'projects': sorted(list(found_projects))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
