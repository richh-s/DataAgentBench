code = """import json

f_path = locals()['var_functions.query_db:64']
d_path = locals()['var_functions.query_db:40']

with open(f_path) as f:
    funding = json.load(f)
with open(d_path) as f:
    docs = json.load(f)

hf = set()
for r in funding:
    if int(r['Amount']) > 50000:
        hf.add(r['Project_Name'])

projects = []
for d in docs:
    text = d.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start >= 0:
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end < 0: end = len(text)
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and line[0] not in ['(', '-', '•']:
                if 'Updates' not in line and 'Schedule' not in line and 'Page' not in line:
                    clean = line.replace('(cid:190)', '').replace('(cid:131)', '')
                    clean = clean.replace('\xcid', '')
                    if len(clean) > 15:
                        projects.append(clean)

matches = [p for p in projects if p in hf]
result = {'hf': len(hf), 'design': len(projects), 'match': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
