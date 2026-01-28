code = """import json, re

funding_data = json.load(open(locals()['var_functions.query_db:0']))
civic_docs = json.load(open(locals()['var_functions.query_db:2']))

funding_map = {}
for r in funding_data:
    if int(r['Amount']) > 50000:
        funding_map[r['Project_Name']] = int(r['Amount'])

design_projects = set()

for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('Capital Improvement Projects')[0]
            for line in design_section.splitlines():
                line = line.strip()
                if not line or len(line) < 10 or not line[0].isupper():
                    continue
                if any(kw in line for kw in ['Project', 'Improvements', 'Repair']):
                    if line in funding_map:
                        design_projects.add(line)
                    else:
                        for funded in funding_map:
                            if line.startswith(funded) or funded.startswith(line.split('(')[0].strip()):
                                design_projects.add(funded)
                                break

print('__RESULT__:')
print(json.dumps(len(design_projects)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
