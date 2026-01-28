code = """import json

# Load funding data
funding_file = open(var_functions.query_db:90)
funding_names = [item['Project_Name'] for item in json.load(funding_file)]
funding_file.close()

# Load civic documents
civic_file = open(var_functions.query_db:6)
civic_docs = json.load(civic_file)
civic_file.close()

# Find design projects
all_design = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and not any(x in line for x in ['Page', 'Schedule']):
                all_design.add(line.replace('•','').strip())

# Count matches
count = 0
for proj in all_design:
    p_lower = proj.lower()
    for funded in funding_names:
        f_lower = funded.lower()
        if p_lower in f_lower or f_lower in p_lower:
            if abs(len(proj) - len(funded)) < 40:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
