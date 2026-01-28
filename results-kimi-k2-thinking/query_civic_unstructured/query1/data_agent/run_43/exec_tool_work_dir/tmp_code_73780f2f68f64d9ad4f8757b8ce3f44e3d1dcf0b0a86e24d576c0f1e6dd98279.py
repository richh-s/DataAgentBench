code = """import json

funding_path = var_functions.query_db:5
civic_path = var_functions.query_db:6

funding_data = json.load(open(funding_path))
civic_docs = json.load(open(civic_path))

funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                if line[0].isalpha():
                    design_projects.add(line)

count = 0
for proj in design_projects:
    for funded in funding_dict:
        if funding_dict[funded] > 50000:
            p = proj.lower()
            f = funded.lower()
            if p in f or f in p:
                if abs(len(p) - len(f)) < 30:
                    count = count + 1
                    break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
