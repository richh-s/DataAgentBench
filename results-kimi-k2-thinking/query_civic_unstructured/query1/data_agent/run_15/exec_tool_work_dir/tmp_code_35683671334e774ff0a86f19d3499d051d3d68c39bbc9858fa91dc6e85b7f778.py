code = """import json
f_path = locals()['var_functions.query_db:64']
with open(f_path) as f:
    funding = json.load(f)

c_path = locals()['var_functions.query_db:40']
with open(c_path) as f:
    docs = json.load(f)

high = set()
for r in funding:
    if int(r['Amount']) > 50000:
        high.add(r['Project_Name'])

design = []
for d in docs:
    t = d.get('text', '')
    if 'Capital Improvement Projects (Design)' in t:
        s = t.split('Capital Improvement Projects (Design)')[1].split('Capital Improvement Projects (Construction)')[0]
        for line in s.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('('):
                if 'Updates:' not in line and 'Schedule:' not in line:
                    clean = line.strip()
                    if len(clean) > 15:
                        design.append(clean)

matches = [p for p in design if p in high]
result = {'high': len(high), 'design': len(design), 'matches': len(matches)}
print('__RESULT__:' )
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
