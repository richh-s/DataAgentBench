code = """import json

funding_data = var_functions.query_db:90
civic_docs = var_functions.query_db:6

# Build funding names list
funding_names = []
for item in funding_data:
    funding_names.append(item['Project_Name'])

# Find design projects
count = 0
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                # Skip non-project lines
                skip = False
                for term in ['Page', 'Schedule:', 'Updates:', 'Item ']:
                    if term in line:
                        skip = True
                        break
                if skip:
                    continue
                
                proj = line.replace('•', '').strip()
                proj_lower = proj.lower()
                for funded in funding_names:
                    funded_lower = funded.lower()
                    if proj_lower in funded_lower or funded_lower in proj_lower:
                        if abs(len(proj) - len(funded)) < 40:
                            count += 1
                            break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
