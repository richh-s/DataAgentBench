code = """import json

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding for projects > $50000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract design project names from civic documents
design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Find sections mentioning capital projects in design
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Look for lines that appear to be project names
        for line in text.split('\n'):
            line = line.strip()
            # Basic heuristic: skip empty, short lines and metadata
            if line and len(line) > 5:
                skip = False
                # Skip known metadata patterns
                if line.startswith('(') or line.startswith('cid:') or line.startswith('Page') or line.startswith('Agenda'):
                    skip = True
                if 'Updates:' in line or 'Schedule:' in line or 'RECOMMENDED' in line or 'DISCUSSION' in line:
                    skip = True
                if line.startswith('Staff') or line.startswith('City'):
                    skip = True
                if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                    skip = True
                if 'COMPLETE DESIGN' in line.upper() or 'ADVERTISE' in line.upper():
                    skip = True
                
                if not skip:
                    # Clean name by removing parentheticals
                    import re
                    clean_name = re.sub('\s+', ' ', line).strip()
                    clean_name = re.sub('\s*\([^)]*\)$', '', clean_name)
                    if clean_name:
                        design_names.append(clean_name)

# Remove duplicates
design_set = set(design_names)

# Match with funding data
matches = 0
for design_name in design_set:
    for fund_name in funding_lookup.keys():
        # Direct match or design name is prefix of funding name
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matches += 1
            break
        elif fund_name.startswith(design_name + '('):
            matches += 1
#print('result:', matches)

result = str(matches)

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
