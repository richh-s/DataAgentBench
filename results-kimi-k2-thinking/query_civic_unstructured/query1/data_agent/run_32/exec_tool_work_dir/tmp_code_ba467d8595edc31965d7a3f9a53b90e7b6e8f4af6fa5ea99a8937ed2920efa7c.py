code = """import json, re

with open(var_functions.query_db:5) as f:
    docs = json.load(f)

with open(var_functions.query_db:30) as f:
    funding_records = json.load(f)

funded = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

projects = set()

for doc in docs:
    txt = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' in txt:
        pos = txt.find('(Design)')
        start = txt.find('(', txt.find('Capital Improvement Projects', pos))
        if pos != -1:
            section = txt[pos:start] if pos < start else txt[pos:]
            end = txt.find('Capital Improvement Projects (Construction)')
            if end != -1:
                section = txt[pos:end]
            
            for line in section.split('\n'):
                clean = line.strip()
                if clean in funded:
                    projects.add(clean)

result = len(projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
