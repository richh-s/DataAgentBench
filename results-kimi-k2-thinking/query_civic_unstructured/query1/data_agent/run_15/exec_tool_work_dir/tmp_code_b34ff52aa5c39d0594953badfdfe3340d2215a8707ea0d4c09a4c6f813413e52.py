code = """import json

# Load data without using string replacement that could cause encoding issues
f_path = locals()['var_functions.query_db:64']
d_path = locals()['var_functions.query_db:40']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(d_path, 'r') as f:
    docs = json.load(f)

# Get high funding projects
high_funding = set()
for r in funding:
    amount = int(r['Amount'])
    if amount > 50000:
        high_funding.add(r['Project_Name'])

# Extract design projects
all_design = []
for d in docs:
    text = d.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker in text:
        start = text.find(marker) + len(marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1: end = len(text)
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and line[0] not in ['(', '-', '•', 'P']:
                if 'Updates' not in line and 'Schedule' not in line:
                    clean = line.strip()
                    if len(clean) > 15:
                        all_design.append(clean)

# Find matches
design_set = set(all_design)
matches = high_funding.intersection(design_set)

result = {'high': len(high_funding), 'design': len(design_set), 'matches': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
