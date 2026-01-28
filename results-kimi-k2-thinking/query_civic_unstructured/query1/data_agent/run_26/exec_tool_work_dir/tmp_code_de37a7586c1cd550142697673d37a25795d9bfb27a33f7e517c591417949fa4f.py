code = """import json

# Load data from the files
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Create lookup for funded projects
funded = {}
for rec in funding_data:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Find design projects from civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        start = text.index('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = len(text)
        section = text[start:end]
        lines = section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) > 5 and '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line and 'Page' not in line and 'Capital Improvement' not in line:
                if i+1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                    design_projects.append(line.lower())

# Count matches with funding > 50000
count = sum(1 for proj in design_projects if proj in funded and funded[proj] > 50000)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
