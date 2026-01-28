code = """import json

# Get funding records (already filtered for amount > 50000)
funding_data = var_functions.query_db:90

# Get civic documents
civic_data = var_functions.query_db:6

# Build funding names list
funding_names = [item['Project_Name'] for item in funding_data]

# Find design capital projects in civic documents
project_names = set()
for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.splitlines()
        for line in lines:
            line = line.strip()
            if line and len(line) > 5:
                # Skip non-project lines
                if 'Page' in line or 'Schedule' in line:
                    continue
                if line.startswith('202') or line.startswith('Item'):
                    continue
                clean = line.replace('•', '').replace('○', '').strip()
                if 10 < len(clean) < 200:
                    project_names.add(clean)

# Count matches
matched = 0
for proj in project_names:
    p = proj.lower()
    for funded in funding_names:
        f = funded.lower()
        if p in f or f in p:
            if abs(len(proj) - len(funded)) < 40:
                matched += 1
                break

result = json.dumps({'count': matched})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
