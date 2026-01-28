code = """import json

# Get file paths from stored results
funding_path = locals()['var_functions.query_db:90']
civic_path = locals()['var_functions.query_db:6']

# Load funding data (already filtered for Amount > 50000)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract funded project names
funding_names = [item['Project_Name'] for item in funding_data]

# Find capital projects with design status from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for capital improvement projects in design phase
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            # Skip empty lines and those that are too short
            if not line or len(line) < 5:
                continue
            
            # Skip non-project lines
            if any(skip in line for skip in ['Page', 'Schedule:', 'Updates:', 'Item ', '202']):
                continue
            
            # If line is reasonable length and starts with capital letter or bullet
            if len(line) < 200 and (line[0].isupper() or line.startswith('•') or line.startswith('○')):
                clean_name = line.replace('•', '').replace('○', '').strip()
                if len(clean_name) > 8:
                    design_projects.add(clean_name)

# Count matches between design projects and funded projects
matched_count = 0
for design_proj in design_projects:
    d_lower = design_proj.lower()
    for funded_name in funding_names:
        f_lower = funded_name.lower()
        # Check if names are similar (substring match)
        if d_lower in f_lower or f_lower in d_lower:
            # Additional length check to avoid false matches
            if abs(len(design_proj) - len(funded_name)) < 40:
                matched_count += 1
                break

result = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
