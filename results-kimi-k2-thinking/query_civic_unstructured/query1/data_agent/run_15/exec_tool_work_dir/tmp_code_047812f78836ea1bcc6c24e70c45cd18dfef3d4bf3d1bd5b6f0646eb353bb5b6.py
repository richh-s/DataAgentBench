code = """import json

# Load the data files
f_path = locals()['var_functions.query_db:64']
d_path = locals()['var_functions.query_db:40']

with open(f_path) as f:
    funding = json.load(f)
with open(d_path) as f:
    docs = json.load(f)

# Get high funding projects
hf_set = set()
for r in funding:
    if int(r['Amount']) > 50000:
        hf_set.add(r['Project_Name'])

# Extract design projects
design_list = []
for d in docs:
    t = d.get('text', '')
    idx = t.find('Capital Improvement Projects (Design)')
    if idx > 0:
        start = idx + len('Capital Improvement Projects (Design)')
        end = t.find('Capital Improvement Projects (Construction)', start)
        if end < 0:
            end = len(t)
        s = t[start:end]
        for line in s.split('\n'):
            line = line.strip()
            if 15 < len(line) < 200:
                if line[0] not in ['(', '-']:
                    if 'Updates' not in line and 'Schedule' not in line:
                        design_list.append(line)

# Find matches
design_set = set(design_list)
matches = hf_set.intersection(design_set)

result = {'hf_count': len(hf_set), 'design_count': len(design_set), 'match_count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
