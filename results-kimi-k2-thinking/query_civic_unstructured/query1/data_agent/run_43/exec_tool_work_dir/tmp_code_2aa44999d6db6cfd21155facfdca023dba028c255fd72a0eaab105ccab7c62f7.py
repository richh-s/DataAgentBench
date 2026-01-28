code = """import json

funding_file = var_functions.query_db:5
civic_file = var_functions.query_db:6

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}

design_set = set()
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 8 and not any(word in line.lower() for word in ['page', 'schedule', 'updates']):
                design_set.add(line)

count = 0
for proj in design_set:
    for funded in funding_map:
        if funding_map[funded] > 50000:
            p = proj.lower()
            f = funded.lower()
            if p in f or f in p:
                if abs(len(p) - len(f)) < 30:
                    count += 1
                    break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
