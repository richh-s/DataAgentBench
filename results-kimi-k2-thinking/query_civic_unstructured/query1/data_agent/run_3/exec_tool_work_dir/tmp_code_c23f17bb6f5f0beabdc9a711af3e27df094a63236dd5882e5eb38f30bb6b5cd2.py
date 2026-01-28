code = """import json
import re

# Load data
funding_records = json.loads(open(locals()['var_functions.query_db:40']).read())
civic_documents = json.loads(open(locals()['var_functions.query_db:5'], encoding='utf-8').read())

# Find capital design projects
design_projs = set()
for doc in civic_documents:
    text = doc.get('text', '')
    idx = text.find('Capital Improvement Projects (Design)')
    if idx >= 0:
        # Get a chunk of text from that point
        chunk = text[idx:idx+2500]
        # Look for project titles (lines containing "Project" and not too short)
        for line in chunk.split('\n'):
            line = line.strip()
            if len(line) > 10 and 'Project' in line and 'fema' not in line.lower():
                design_projs.add(line)

# Match funding > 50000
matched = set()
for rec in funding_records:
    amt = int(rec['Amount'])
    if amt > 50000:
        name = rec['Project_Name']
        base = re.sub(r'\s*\([^)]*\)$', '', name).strip()
        if base in design_projs:
            matched.add(base)

result = {'count': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
