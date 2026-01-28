code = """import json
import re

# Load data files
f_path = locals()['var_functions.query_db:38']
d_path = locals()['var_functions.query_db:40']

with open(f_path) as f:
    funding = json.load(f)
with open(d_path) as f:
    docs = json.load(f)

# High funding projects (>50000)
high_funding = {}
for r in funding:
    amt = int(r['Amount'])
    if amt > 50000:
        high_funding[r['Project_Name']] = amt

# Extract design projects from documents
projects = []
for doc in docs:
    text = doc.get('text', '')
    if text.find('Capital Improvement Projects (Design)') > -1:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            for line in section.split('\n'):
                line = line.strip()
                if line and len(line) > 15:
                    if line[0] not in ['(', '-', '•']:
                        if 'Updates:' not in line and 'Schedule:' not in line:
                            clean = re.sub(r'^(cid:\d+)\s*', '', line)
                            if len(clean) > 15:
                                projects.append(clean)

# Find matches
matches = []
for p in projects:
    if p in high_funding:
        matches.append(p)

result = {
    'high_funding_total': len(high_funding),
    'design_projects_total': len(projects),
    'matching_count': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
