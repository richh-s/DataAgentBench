code = """import json, re

civic_docs = var_functions.query_db:5
if isinstance(civic_docs, str): 
    civic_docs = json.load(open(civic_docs))

funding = var_functions.query_db:6
if isinstance(funding, str):
    funding = json.load(open(funding))

park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Park' in line and len(line) > 5:
            skip_words = ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date', 'Public Works', 'Commission']
            if any(word in line for word in skip_words): continue
            if line.startswith('('): continue
            
            next_text = ' '.join(lines[i:i+15])
            if 'completed' in next_text.lower() and '2022' in next_text:
                if re.search(r'completed.*2022|2022.*completed|november 2022|december 2022', next_text, re.I):
                    park_projects.append(line)

unique_projects = list(set(park_projects))
print('__RESULT__:')
print(json.dumps({'projects': unique_projects, 'count': len(unique_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
