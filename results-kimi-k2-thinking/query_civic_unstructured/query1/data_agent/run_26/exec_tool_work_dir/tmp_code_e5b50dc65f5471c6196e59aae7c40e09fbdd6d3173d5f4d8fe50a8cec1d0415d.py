code = """import json, re

# Load funding data from the stored file
with open('var_functions.query_db:0') as f1:
    funding = json.load(f1)

# Load civic documents from the stored file  
with open('var_functions.query_db:2') as f2:
    docs = json.load(f2)

# Create a dictionary mapping project names to funding amounts
funded_amounts = {}
for rec in funding:
    name = rec['Project_Name'].strip().lower()
    funded_amounts[name] = int(rec['Amount'])

# Extract capital design projects from the documents
design_projects = []
for doc in docs:
    text = doc.get('text', '')
    
    # Find the design section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('(Design)', 1)
        if len(parts) > 1:
            section = parts[1].split('(Construction)')[0]
            lines = section.replace('▪', '').replace('•', '').split('\n')
            
            for i, line in enumerate(lines):
                line = line.strip()
                # Look for project names (not control lines)
                if line and len(line) > 10 and 'Updates:' not in line:
                    if 'Project Schedule:' not in line and 'Page' not in line:
                        if 'Capital Improvement' not in line and 'RECOMMENDED' not in line:
                            if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                                design_projects.append(line.lower())

# Count unique design projects with funding > $50000
seen = set()
count = 0
for proj in design_projects:
    if proj not in seen:
        seen.add(proj)
        if proj in funded_amounts and funded_amounts[proj] > 50000:
            count = count + 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}, 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
