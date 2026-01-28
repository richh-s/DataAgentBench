code = """import json

# Load funding data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Count design projects with >$50k funding
matched = 0

for doc in civic_docs:
    text = doc.get('text', '')
    # Use simple search
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        design_section = False
        for line in lines:
            line = line.strip()
            if 'Capital Improvement Projects' in line and 'Design' in line:
                design_section = True
                continue
            if design_section and line.startswith('Capital'):
                design_section = False
                continue
            if design_section and line and len(line) > 10:
                if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line and 'Agenda' not in line:
                    if not line.startswith('Staff') and not line.startswith('City'):
                        if 'COMPLETE DESIGN' not in line.upper() and 'COMPLETE' not in line:
                            if 'Spring' not in line and 'Summer' not in line and 'Fall' not in line and 'Winter' not in line:
                                clean_name = line
                                if '(' in clean_name:
                                    clean_name = clean_name.split('(')[0].strip()
                                clean_name = clean_name.strip()
                                if clean_name and len(clean_name) > 5:
                                    # Check if this matches funding
                                    for fund_name in funding_lookup.keys():
                                        if clean_name == fund_name or fund_name.startswith(clean_name + ' '):
                                            matched += 1
                                            break

result = str(matched)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
