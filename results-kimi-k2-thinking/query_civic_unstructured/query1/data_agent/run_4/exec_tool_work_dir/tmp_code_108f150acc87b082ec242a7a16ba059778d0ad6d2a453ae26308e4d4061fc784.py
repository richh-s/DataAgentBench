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
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Simple extraction of capital design projects using keyword matching
design_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Find sections with Capital Improvement Projects and Design
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Split into lines
        for line in text.split('\n'):
            line = line.strip()
            # Simple heuristics to identify project names
            if line and len(line) > 10:
                # Skip if contains these keywords
                skip = False
                for keyword in ['Updates:', 'Schedule:', 'Page', 'Agenda', 'cid:', 'RECOMMENDED', 'DISCUSSION', 'Staff', 'City', 'Spring', 'Summer', 'Fall', 'Winter', 'Complete Design', 'Advertise']:
                    if keyword in line:
                        skip = True
                        break
                if not skip and not line.startswith('(') and not line.startswith('Capital'):
                    # Clean name by removing parentheticals
                    import re
                    clean = re.sub(r'\s*\([^)]*\)$', '', line).strip()
                    if clean and len(clean) > 5:
                        design_project_names.add(clean)

# Count matches
matches = 0
for design_name in design_project_names:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matches += 1
            break

print('__RESULT__:')
print(str(matches))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
