code = """import json

# Direct access to stored variables
funding_data = var_functions.query_db:90
docs = var_functions.query_db:6

# Get funded project names
funding_names = []
for item in funding_data:
    if isinstance(item, dict):
        funding_names.append(item['Project_Name'])

# Count design projects with funding > 50000
count = 0
for doc in docs:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            for line in text.split('\n'):
                line = line.strip()
                if len(line) > 10:
                    # Skip metadata
                    skip = False
                    for term in ['Page', 'Schedule:', 'Updates:', 'Item ', 'to:', 'Prepared by', 'Approved by', 'Subject:']:
                        if term in line:
                            skip = True
                            break
                    if skip:
                        continue
                    
                    proj = line.replace('•', '').replace('○', '').strip()
                    if len(proj) > 8 and len(proj) < 200:
                        proj_lower = proj.lower()
                        for funded in funding_names:
                            funded_lower = funded.lower()
                            if proj_lower in funded_lower or funded_lower in proj_lower:
                                if abs(len(proj) - len(funded)) < 35:
                                    count += 1
                                    break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
