code = """import json

f1 = var_functions.query_db:0
f2 = var_functions.query_db:2

data1 = open(f1, 'r').read()
data2 = open(f2, 'r').read()

funding = json.loads(data1)
docs = json.loads(data2)

funded = {}
for r in funding:
    funded[r['Project_Name'].lower()] = int(r['Amount'])

design = []
for doc in docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1].split('Capital Improvement Projects (Construction)')[0]
        parts = section.split('\n')
        for line in parts:
            line = line.strip()
            if line and len(line) > 5:
                if 'Updates:' not in line and 'Project Schedule:' not in line:
                    if 'Page' not in line:
                        design.append(line.lower())

count = sum(1 for p in design if p in funded and funded[p] > 50000)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
