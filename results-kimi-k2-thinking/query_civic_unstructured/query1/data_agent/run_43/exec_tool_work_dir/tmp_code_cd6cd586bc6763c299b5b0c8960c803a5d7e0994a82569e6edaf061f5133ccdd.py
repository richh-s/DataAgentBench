code = """import json

# Get stored results
funding_result = locals()['var_functions.query_db:90']
docs_result = locals()['var_functions.query_db:6']

# Build funding names list
funding_names = []
for item in funding_result:
    funding_names.append(item['Project_Name'])

# Find design projects and count matches
count = 0
for doc in docs_result:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 10 and not any(x in line for x in ['Page', 'Schedule', 'Updates:', 'Item ']):
                proj_clean = line.replace('•', '').replace('○', '').strip()
                proj_lower = proj_clean.lower()
                for funded in funding_names:
                    f_lower = funded.lower()
                    if proj_lower in f_lower or f_lower in proj_lower:
                        if abs(len(proj_clean) - len(funded)) < 40:
                            count += 1
                            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
