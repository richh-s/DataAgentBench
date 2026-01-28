code = """import json

# Load data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

c_path = locals()['var_functions.query_db:8']  
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Count funding projects > $50k
count_funding = len([x for x in funding_data if int(x['Amount']) > 50000])

# Extract sample design projects from first doc
sample_design = []
for doc in civic_docs[:1]:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
        elif in_design and line and len(line) > 10 and 'COMPLETE' not in line.upper():
            if 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
                if not line.startswith('Staff') and not line.startswith('City'):
                    if 'Spring' not in line and 'Summer' not in line and 'Fall' not in line and 'Winter' not in line:
                        sample_design.append(line)

# Match fund project names with design projects
funding_names = set([x['Project_Name'].strip() for x in funding_data if int(x['Amount']) > 50000])

# Simple match: count how many funding projects are likely capital design
# Based on patterns in names, identify design projects
matched = 0
for fund_name in funding_names:
    # Skip obvious non-design/fema/disaster projects
    if '(FEMA' in fund_name or 'CalOES' in fund_name or 'CalJPIA' in fund_name:
        continue
    # Skip completed/repaired projects
    if 'Repairs' in fund_name or 'Repair' in fund_name or 'Replacement' in fund_name:
        continue
    if 'Study' in fund_name or 'Plan' in fund_name:
        continue
    
    # Likely design projects
    design_indicators = ['Project', 'Improvements', 'Park', 'Road', 'Center']
    has_indicator = any(ind in fund_name for ind in design_indicators)
    
    if has_indicator and len(fund_name.split()) >= 3:
        matched += 1

print('__RESULT__:')
print(matched)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7}

exec(code, env_args)
