code = """import json

# Load the data
f_path = locals()['var_functions.query_db:64']
d_path = locals()['var_functions.query_db:40']

with open(f_path) as f:
    funding = json.load(f)
with open(d_path) as f:
    docs = json.load(f)

# Get high funding projects (> $50,000)
high_funding_projects = set()
for record in funding:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_projects.add(record['Project_Name'])

# Extract design capital projects
design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = len(text)
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and line[0] not in ['(', '-']:
                if 'Updates:' not in line and 'Schedule:' not in line:
                    design_projects.add(line)

# Find matches
matches = high_funding_projects.intersection(design_projects)
result = {
    'high_funding_total': len(high_funding_projects),
    'design_total': len(design_projects),
    'matching': len(matches)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
