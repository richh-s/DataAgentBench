code = """import json

# Load the data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    docs = json.load(f)

# Simple count: funding projects > $50k
fund_count = len([x for x in funding if int(x['Amount']) > 50000])

# Sample a few project names from docs that mention design
sample_design = []
for doc in docs[:1]:
    text = doc.get('text', '')
    if 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 5 and not line.startswith('(') and 'Updates:' not in line:
                if 'COMPLETE' not in line.upper() and 'Schedule:' not in line:
                    if 'Spring' not in line and 'Summer' not in line:
                        sample_design.append(line)

print('__RESULT__:', 'Funding:', fund_count, 'Sample design lines:', len(sample_design))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
