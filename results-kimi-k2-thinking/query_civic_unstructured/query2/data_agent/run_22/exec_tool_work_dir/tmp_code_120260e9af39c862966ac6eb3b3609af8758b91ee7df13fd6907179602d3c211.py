code = """import json, re

# Load data
civic_docs = json.load(open('/tmp/tmppk2n1y0f.json'))
funding_data = json.load(open('/tmp/tmpp8v2e1e3.json'))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completion patterns with Park names
    pattern = r'([A-Za-z\s]+Park[A-Za-z\s]*)[^\n]*Construction was completed[^\n]*2022'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    
    for m in matches:
        name = m.group(1).strip()
        if name and name not in park_projects:
            park_projects.append(name)

# Also check Broad Beach Road Water Quality Repair (park infrastructure)
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Broad Beach Road Water Quality' in text and '2022' in text and 'completed' in text.lower():
        if 'Broad Beach Road Water Quality Repair' not in park_projects:
            park_projects.append('Broad Beach Road Water Quality Repair')

# Match with funding
total = 0
for project in park_projects:
    pl = project.lower()
    for fund in funding_data:
        fl = fund['Project_Name'].lower()
        if pl == fl or fl.startswith(pl):
            total += int(fund['Amount'])

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': park_projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:70': {'files': [], 'civic_related': []}, 'var_functions.execute_python:72': {'civic_type': "<class 'NoneType'>", 'funding_type': "<class 'NoneType'>"}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
