code = """import json

# Load data from files
f_path = locals()['var_functions.query_db:22']
c_path = locals()['var_functions.query_db:20']

with open(f_path) as f:
    funding = json.load(f)

with open(c_path) as f:
    civic = json.load(f)

# Get design projects
design_names = []
import re
for doc in civic:
    txt = doc.get('text', '')
    if not txt:
        continue
    m = re.search('Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|$)', txt, re.DOTALL | re.IGNORECASE)
    if m:
        section = m.group(1)
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 5 and line[0] not in '(-' and not line.isupper() and 'cid:' not in line and 'PROJECTS' not in line.upper():
                low = line.lower()
                if not any(x in low for x in ['updates', 'schedule', 'description', 'page', 'public works', 'commission', 'agenda']):
                    if low not in ['design', 'construction', 'not started']:
                        design_names.append(line)

design_names = list(set(design_names))
print('Design projects found:', len(design_names))

# Check funding
matches = []
for f in funding:
    amt = int(f['Amount'])
    if amt > 50000 and f['Project_Name'] in design_names:
        matches.append({'Project_Name': f['Project_Name'], 'Amount': amt})

print('Projects meeting criteria:', len(matches))
for m in matches:
    print(m['Project_Name'], ':', m['Amount'])

result = json.dumps({'count': len(matches), 'projects': matches})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
