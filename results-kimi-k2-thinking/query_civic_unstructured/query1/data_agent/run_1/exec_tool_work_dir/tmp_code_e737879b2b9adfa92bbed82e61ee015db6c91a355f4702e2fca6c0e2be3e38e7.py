code = """import json, re

funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

funding_map = {}
for r in funding_data:
    if int(r['Amount']) > 50000:
        funding_map[r['Project_Name']] = int(r['Amount'])

projects = set()

for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        design_start = text.index('Capital Improvement Projects (Design)') + len('Capital Improvement Projects (Design)')
        remaining = text[design_start:]
        design_section = remaining.split('Capital Improvement Projects')[0]
        
        for line in design_section.split('\n'):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 10:
                if 'Project' in line or 'Improvements' in line or 'Repair' in line:
                    if line in funding_map:
                        projects.add(line)
                    else:
                        for funded in funding_map:
                            if line.startswith(funded) or funded.startswith(line.split('(')[0].strip()):
                                projects.add(funded)
                                break

result = len(projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
