code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Extract capital design projects from civic docs
projects = set()
for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt[txt.index('Capital Improvement Projects (Design)'):txt.index('Capital Improvement Projects (Design)') + 2000]
        for line in section.split('\n'):
            if line.strip() and len(line.strip()) > 10 and 'Project' in line and 'fema' not in line.lower():
                projects.add(line.strip())

# Count funded > 50000
funded = set()
for rec in funding_data:
    if int(rec['Amount']) > 50000:
        base = rec['Project_Name'].split('(')[0].strip()
        if base in projects:
            funded.add(base)

result = {'count': len(funded)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
