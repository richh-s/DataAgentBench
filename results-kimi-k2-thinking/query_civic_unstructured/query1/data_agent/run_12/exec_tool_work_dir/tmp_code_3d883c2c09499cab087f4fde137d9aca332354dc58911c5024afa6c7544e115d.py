code = """import json
funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:1

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    docs = json.load(f)

funding_map = {}
for item in funding:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_map[item['Project_Name']] = amt

found = set()
for doc in docs:
    txt = doc.get('text', '')
    key = 'Capital Improvement Projects (Design)'
    if key in txt:
        sub = txt[txt.index(key)+len(key):]
        ends = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
        cut = len(sub)
        for e in ends:
            pos = sub.find(e)
            if pos > 0 and pos < cut:
                cut = pos
        sub = sub[:cut]
        for line in sub.split('\n'):
            line = line.strip()
            if not line or len(line) < 5: continue
            if line[0] in '(-•': continue
            if 'Updates' in line or 'Schedule' in line or 'Capital Improvement' in line: continue
            if line in funding_map:
                found.add(line)

print('__RESULT__:')
print(json.dumps({'count': len(found), 'projects': sorted(list(found))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
