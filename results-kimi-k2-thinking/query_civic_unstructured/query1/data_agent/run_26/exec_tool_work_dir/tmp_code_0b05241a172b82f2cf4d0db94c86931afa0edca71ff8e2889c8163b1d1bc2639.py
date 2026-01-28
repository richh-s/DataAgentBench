code = """import json

with open('var_functions.query_db:0') as f:
    funding = json.load(f)

with open('var_functions.query_db:2') as f:
    docs = json.load(f)

funded = {}
for rec in funding:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

design = []
for doc in docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        s = text.split('Capital Improvement Projects (Design)')[1]
        s = s.split('Capital Improvement Projects (Construction)')[0]
        for line in s.split('\n'):
            line = line.strip()
            if line and len(line) > 5 and '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line:
                if 'Capital Improvement' not in line and 'Page' not in line and 'RECOMMENDED' not in line:
                    design.append(line.lower())

count = sum(1 for p in design if p in funded and funded[p] > 50000)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
