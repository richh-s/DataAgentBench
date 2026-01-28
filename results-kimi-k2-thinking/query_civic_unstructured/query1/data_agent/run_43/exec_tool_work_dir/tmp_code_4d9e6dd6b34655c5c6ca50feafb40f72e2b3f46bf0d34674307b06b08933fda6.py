code = """import json

funding = var_functions.query_db:90
civic = var_functions.query_db:6

names = [item['Project_Name'] for item in funding]

count = 0
for doc in civic:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not 'Page' in line:
                for name in names:
                    if line.lower() in name.lower() or name.lower() in line.lower():
                        if '•' not in line and len(line) < 200:
                            count += 1
                            break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
