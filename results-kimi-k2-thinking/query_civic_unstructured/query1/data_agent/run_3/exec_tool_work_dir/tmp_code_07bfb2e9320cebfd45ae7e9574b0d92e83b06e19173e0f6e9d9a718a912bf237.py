code = """import json, re

# Load the data
funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Find design projects
projects = set()
for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Design' in txt:
        idx = txt.find('Capital Improvement Projects (Design)')
        if idx > -1:
            sec = txt[idx:]
            for line in sec.split('\n'):
                line2 = line.strip()
                if line2 and len(line2) > 10 and 'Project' in line2 and 'fema' not in line2.lower():
                    projects.add(line2)

# Match funding > 50000
funded = set()
for rec in funding_data:
    amt = int(rec['Amount'])
    if amt > 50000:
        base = rec['Project_Name'].split('(')[0].strip()
        if base in projects:
            funded.add(base)

result = {'count': len(funded)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
