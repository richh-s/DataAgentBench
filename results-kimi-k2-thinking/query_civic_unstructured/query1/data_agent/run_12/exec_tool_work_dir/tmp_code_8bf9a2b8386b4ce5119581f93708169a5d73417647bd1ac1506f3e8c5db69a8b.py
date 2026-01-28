code = """import json

funding = json.load(open('var_functions.query_db:0', 'r'))
docs = json.load(open('var_functions.query_db:1', 'r'))

funding_lookup = {}
for item in funding:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name']] = amount

found_projects = set()

for doc in docs:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker not in text:
        continue
    start = text.find(marker) + len(marker)
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
        skip = False
        for skip_word in ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']:
            if skip_word in line:
                skip = True
                break
        if skip:
            continue
        if line in funding_lookup:
            found_projects.add(line)

count = len(found_projects)
total_funding = sum(funding_lookup.get(p, 0) for p in found_projects)

result = {
    'count': count,
    'projects': sorted(list(found_projects)),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
