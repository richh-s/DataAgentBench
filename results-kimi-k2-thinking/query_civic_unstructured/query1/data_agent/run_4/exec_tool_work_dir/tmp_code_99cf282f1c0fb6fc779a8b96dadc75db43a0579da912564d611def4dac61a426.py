code = """import json

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50,000
funding_over_50k = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        project_name = item['Project_Name'].strip()
        funding_over_50k[project_name] = amount

# Extract design status projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for capital projects in design status
    # Pattern: find sections mentioning design
    if 'Design' in text and 'Capital' in text:
        # Split by sections to find design portion
        sections = text.split('\n\n')
        for section in sections:
            if 'Capital Improvement Projects' in section and 'Design' in section:
                # Extract lines that are likely project names
                for line in section.split('\n'):
                    line = line.strip()
                    # Filter out metadata
                    if line and len(line) > 5 and not any(x in line for x in ['Updates:', 'Schedule:', 'cid:', 'Page', 'Staff', 'City']) and not line.startswith('Capital') and 'Design' not in line:
                        if not re.search('Spring|Summer|Fall|Winter', line):
                            clean = line.strip()
                            if clean and 'COMPLETE DESIGN' not in clean.upper():
                                # Remove parenthetical suffixes for base name
                                base_name = re.sub(r'\s*\([^)]*\)$', '', clean)
                                design_projects.append(base_name)

# Remove duplicates
unique_design = list(set(design_projects))

# Match with funding data
count = 0
for design_name in unique_design:
    for fund_name in funding_over_50k.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            count += 1
            break

print('RESULT:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
