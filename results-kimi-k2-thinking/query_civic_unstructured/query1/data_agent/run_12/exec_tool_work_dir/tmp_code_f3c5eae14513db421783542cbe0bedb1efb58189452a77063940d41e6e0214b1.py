code = """import json

# Load data
funding = json.load(open('var_functions.query_db:0', 'r'))
docs = json.load(open('var_functions.query_db:1', 'r'))

# Build funding lookup
funding_lookup = {}
for item in funding:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Find design projects
projects = set()
for doc in docs:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker in text:
        section = text[text.find(marker) + len(marker):]
        boundaries = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
        end = min([p for p in [section.find(b) for b in boundaries] if p > 0] or [len(section)])
        section = section[:end]
        for line in section.split('\n'):
            line = line.strip()
            if not line or len(line) < 5: continue
            if line.startswith('(') or line.startswith('-') or line.startswith('•'): continue
            skip = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']
            if any(s in line for s in skip): continue
            if line in funding_lookup: projects.add(line)

result = json.dumps({'count': len(projects), 'projects': sorted(list(projects))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
