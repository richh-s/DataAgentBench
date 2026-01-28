code = """import json
import re

# Load data
high_funding_file = locals()['var_functions.query_db:50']
civic_docs_file = locals()['var_functions.query_db:8']

with open(high_funding_file, 'r') as f:
    high_funding = json.load(f)

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_names = set()
for f in high_funding:
    name = f['Project_Name'].lower().strip()
    funding_names.add(name)
    # Also add base name without suffix
    base = re.sub(r'\s*\([^)]*\)$', '', name)
    funding_names.add(base)

# Extract design projects
design_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        if 'Capital Improvement Projects (Construction)' in section:
            section = section.split('Capital Improvement Projects (Construction)')[0]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                checks = ['Updates', 'Schedule', 'Design', 'Advertise', 'Construction', 'Page ', 'Agenda Item', '(cid:']
                if not any(c in line for c in checks):
                    design_names.append(line.lower())

# Count unique matches
count = 0
seen = set()
for name in design_names:
    if name in funding_names and name not in seen:
        count += 1
        seen.add(name)

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
