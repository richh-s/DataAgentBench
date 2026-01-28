code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for capital improvement projects in design section
    if 'Capital Improvement Projects' in text and 'Design' in text:
        sections = re.split('\n\s*\n', text)
        for section in sections:
            if 'Capital Improvement Projects' in section and 'Design' in section:
                # Extract project names from this section
                in_proj_section = False
n                for line in section.split('\n'):
                    line = line.strip()
                    if not line:
                        continue
                    if 'Capital Improvement Projects' in line and 'Design' in line:
                        in_proj_section = True
                        continue
                    if in_proj_section and (line.startswith('Capital') or line.startswith('DISASTER')):
                        break
                    if in_proj_section and line and len(line) > 5:
                        # Skip metadata
                        if any(k in line for k in ['Updates:', 'Schedule:', 'RECOMMENDED', 'DISCUSSION', 'cid:', 'Page', 'Agenda']):
                            continue
                        if any(season in line for season in ['Spring', 'Summer', 'Fall', 'Winter']):
                            continue
                        if line.startswith('Staff') or line.startswith('City'):
                            continue
                        # Clean and add
                        clean = re.sub('\s*\([^)]*\)$', '', line).strip()
                        if clean and 'COMPLETE DESIGN' not in clean.upper() and 'ADVERTISE' not in clean.upper():
                            design_projects.add(clean)

# Match with funding data
count = 0
for proj in design_projects:
    for fund in funding_lookup.keys():
        if proj == fund or fund.startswith(proj + ' ') or fund.startswith(proj + '('):
            count += 1
            break

print('__RESULT__:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
