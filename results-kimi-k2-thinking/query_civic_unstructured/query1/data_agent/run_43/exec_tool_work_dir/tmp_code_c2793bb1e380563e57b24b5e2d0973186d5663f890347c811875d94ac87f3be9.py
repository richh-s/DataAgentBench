code = """import json

funding_file = var_functions.query_db:60
civic_file = var_functions.query_db:6

with open(funding_file) as f:
    funding = json.load(f)
with open(civic_file) as f:
    docs = json.load(f)

funding_names = [item['Project_Name'] for item in funding]
count = 0
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 8:
                for funded in funding_names:
                    if funded.lower().find(line.lower()) >= 0 or line.lower().find(funded.lower()) >= 0:
                        if len(line) > 8 and 'Page' not in line:
                            count += 1
                            break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
