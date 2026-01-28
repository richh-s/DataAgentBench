code = """import json

# Load data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k
funding_lookup = {}
for item in funding_data:
    if int(item['Amount']) > 50000:
        funding_lookup[item['Project_Name'].strip()] = int(item['Amount'])

# Simple extraction
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split into paragraphs
    paragraphs = text.split('\n\n')
    
    for para in paragraphs:
        if 'Capital Improvement Projects' in para and 'Design' in para:
            # Extract lines
            lines = para.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 10 and 'COMPLETE DESIGN' not in line.upper() and line.startswith('(') == False:
                    # Skip metadata
                    if 'Updates:' in line or 'Schedule:' in line or 'Page' in line or 'Agenda' in line:
                        continue
                    if line.startswith('Staff') or line.startswith('City'):
                        continue
                    if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                        continue
                    # Clean name
                    clean = line.split('(')[0].strip()
                    if clean and len(clean) > 5:
                        design_projects.append(clean)

design_set = set(design_projects)

# Count matches
matches = 0
for design_name in design_set:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matches += 1
            break

result = str(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
