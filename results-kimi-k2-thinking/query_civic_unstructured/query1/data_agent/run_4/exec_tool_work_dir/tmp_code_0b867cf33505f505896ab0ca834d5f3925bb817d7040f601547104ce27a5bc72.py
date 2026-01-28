code = """import json

# Load data files
f_path = locals()['var_functions.execute_python:2']
c_path = locals()['var_functions.query_db:8']

with open(f_path, 'r') as f:
    funding = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding set for > $50k
funding_set = set()
for item in funding:
    if int(item['Amount']) > 50000:
        funding_set.add(item['Project_Name'].strip())

# Extract capital design projects by looking for pattern matches
# Using a conservative approach

# Use the funding project names that appear to be capital design projects
# Based on common patterns in the data

capital_design_patterns = [
    'Project', 'Improvements', 'Park', 'Road', 'Center',
    'Skate', 'Walkway', 'Bridge', 'Drainage', 'Signals'
]

count = 0
for fund_name in funding_set:
    # Skip FEMA/CalOES projects (disaster type)
    if '(FEMA' in fund_name or 'CalOES' in fund_name or 'CalJPIA' in fund_name:
        continue
    # Check if it matches capital design patterns
    has_pattern = any(pattern in fund_name for pattern in capital_design_patterns)
    if has_pattern:
        count += 1

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7}

exec(code, env_args)
