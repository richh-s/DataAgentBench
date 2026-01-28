code = """import json
import re

# Load funding data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Create lookup for funded projects
funded = {}
for rec in funding_data:
    key = rec['Project_Name'].strip().lower()
    funded[key] = int(rec['Amount'])

# Extract design capital projects
design = []
for doc in civic_docs:
    text = doc['text']
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[-1].split('Capital Improvement Projects (Construction)')[0]
            
            for line in design_section.split('\n'):
                line = line.strip()
                if line and len(line) > 5 and 'Updates:' not in line:
                    if 'Project Schedule:' not in line and 'Page' not in line:
                        if 'Capital Improvement' not in line:
                            design.append(line.lower())

# Count projects with funding > 50000
count = 0
for p in design:
    if p in funded and funded[p] > 50000:
        count = count + 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
