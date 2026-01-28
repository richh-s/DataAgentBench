code = """import json

# Load data
funding_file = 'var_functions.query_db:0'
civic_file = 'var_functions.query_db:1'

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Filter funding > 50000
funding_map = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_map[item['Project_Name']] = amount

# Find capital design projects
projects = set()
for doc in civic_docs_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)') + 38
        section = text[start:]
        
        ends = []
        for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
            pos = section.find(marker)
            if pos > 0:
                ends.append(pos)
        
        cutoff = min(ends) if ends else len(section)
        section = section[:cutoff]
        
        for line in section.split('\n'):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            if line[0] in '(-•':
                continue
            if any(word in line for word in ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Capital Improvement', 'Project Description']):
                continue
            if line in funding_map:
                projects.add(line)

result = json.dumps({'count': len(projects), 'projects': sorted(list(projects))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
