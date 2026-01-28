code = """import json
import re

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding = json.load(f)

# Load civic documents  
with open('var_functions.query_db:2', 'r') as f:
    docs = json.load(f)

# Build funding lookup
funded = {}
for r in funding:
    funded[r['Project_Name'].lower()] = int(r['Amount'])

# Extract design capital projects
capital_design_projects = []
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        start = text.index('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        section = text[start:end] if end != -1 else text[start:]
        lines = [l.strip() for l in section.split('\n') if l.strip()]
        for i, line in enumerate(lines):
            if len(line) > 5 and '▪' not in line and 'Updates:' not in line:
                if 'Project Schedule:' not in line and 'Page' not in line:
                    if 'Capital Improvement' not in line and 'RECOMMENDED' not in line:
                        if i+1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                            capital_design_projects.append(line.lower())

# Count projects with funding > 50000
unique_projects = list(set(capital_design_projects))
count = 0
for p in unique_projects:
    if p in funded and funded[p] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
