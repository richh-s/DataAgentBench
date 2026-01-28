code = """import json

# Get funding project names (already filtered for Amount > 50000)
funding_names_data = var_functions.query_db:90
funding_names = [item['Project_Name'] for item in funding_names_data]

# Get civic documents
civic_docs_data = var_functions.query_db:6

# Find design capital projects
design_projects = set()
for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for capital improvement projects with design status
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                # Skip non-project lines
                skip_terms = ['Page', 'Schedule', 'Updates:', 'Project Description', 'Staff is', 'City will', 'Consultant', 'Item ', '202']
                if not any(term in line for term in skip_terms):
                    clean_name = line.replace('•', '').replace('○', '').strip()
                    if len(clean_name) > 8:
                        design_projects.add(clean_name)

# Count matches
count = 0
for proj in design_projects:
    p_lower = proj.lower()
    for funded in funding_names:
        f_lower = funded.lower()
        # Check for name similarity
        if p_lower in f_lower or f_lower in p_lower:
            # Additional length check to avoid false matches
            if abs(len(proj) - len(funded)) < 40:
                count += 1
                break

# Output result as JSON
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
