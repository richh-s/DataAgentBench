code = """import json

# Load the data files
with open('/tmp/tmp_query_result_46b1b2a4.json') as f:
    funding = json.load(f)
with open('/tmp/tmp_query_result_e3c5f8a1.json') as f:
    docs = json.load(f)

# Projects with funding > 50000
hf = set()
for r in funding:
    if int(r['Amount']) > 50000:
        hf.add(r['Project_Name'])

# Extract design project names
design = []
for d in docs:
    text = d.get('text', '')
    idx1 = text.find('Capital Improvement Projects (Design)')
    idx2 = text.find('Capital Improvement Projects (Construction)', idx1)
    if idx1 >= 0:
        if idx2 < 0:
            idx2 = len(text)
        section = text[idx1:idx2]
        for line in section.splitlines():
            line = line.strip()
            if len(line) > 15 and line[0] not in ['(', '-', 'P', '•']:
                if 'Updates:' not in line and 'Schedule:' not in line:
                    design.append(line)

# Count matches
design_set = set(design)
matches = hf.intersection(design_set)

print('__RESULT__:', json.dumps({'matches': len(matches)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
