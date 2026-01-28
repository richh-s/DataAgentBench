code = """import json

funding_file = var_functions.query_db:5
civic_file = var_functions.query_db:6

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding}

found = 0
for doc in docs:
    text = doc.get('text', '')
    if 'Capital' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and line[0].isalpha():
                for funded in funding_dict:
                    if funding_dict[funded] > 50000:
                        p = line.lower()
                        f = funded.lower()
                        if p.find(f) >= 0 or f.find(p) >= 0:
                            if abs(len(line) - len(funded)) < 30:
                                found += 1
                                break

print('__RESULT__:')
print(json.dumps({'count': found}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
