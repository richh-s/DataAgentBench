code = """import json

# Get the stored results from the environment
funding_result = var_functions.query_db:90  # Already filtered for Amount > 50000
docs_result = var_functions.query_db:6

# Build list of funded project names
funding_names = []
for item in funding_result:
    funding_names.append(item['Project_Name'])

# Find design projects and count matches
matched = 0

for doc in docs_result:
    text = doc.get('text', '')
    # Check for capital improvement projects in design
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Extract individual project names
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10:
                # Skip metadata lines
                if any(x in line for x in ['Page', 'Schedule', 'Updates:', 'Item ']): 
                    continue
                # Clean and check the project name
                proj_clean = line.replace('•', '').replace('○', '').strip()
                if 10 < len(proj_clean) < 200:
                    # Try to match with funded names
                    proj_lower = proj_clean.lower()
                    for funded_name in funding_names:
                        f_lower = funded_name.lower()
                        if (proj_lower in f_lower) or (f_lower in proj_lower):
                            if abs(len(proj_clean) - len(funded_name)) < 40:
                                matched += 1
                                break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
