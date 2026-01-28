code = """import json, re

# Load funding data
f1 = var_functions.query_db:0
f2 = var_functions.query_db:2

with open(f1, 'r') as file1:
    funding = json.load(file1)

with open(f2, 'r') as file2:
    docs = json.load(file2)

# Build funded projects lookup
funded = {}
for rec in funding:
    key = rec['Project_Name'].strip().lower()
    funded[key] = int(rec['Amount'])

# Extract design projects
design = []
for doc in docs:
    text = doc.get('text', '')
    
    # Look for the design section
    if 'Capital Improvement Projects (Design)' in text:
        # Get section between Design and Construction
        parts = text.split('Capital Improvement Projects (Design)', 1)
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)', 1)[0]
            lines = section.split('\n')
            
            for i, line in enumerate(lines):
                line = line.strip()
                if line and len(line) > 5 and '▪' not in line:
                    if 'Updates:' not in line and 'Project Schedule:' not in line:
                        if 'Capital Improvement' not in line and 'Page' not in line and 'RECOMMENDED' not in line:
                            if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                                design.append(line.lower())

# Count projects funded > 50000
count = sum(1 for p in set(design) if p in funded and funded[p] > 50000)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
