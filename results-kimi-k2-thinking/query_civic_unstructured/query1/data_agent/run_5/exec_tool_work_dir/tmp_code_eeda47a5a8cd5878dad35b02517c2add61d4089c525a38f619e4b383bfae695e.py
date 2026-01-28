code = """import json

f = json.load(open(locals()['var_functions.query_db:44']))
d = json.load(open(locals()['var_functions.query_db:2']))

funding = set([rec['Project_Name'] for rec in f])
design = []

for doc in d:
    txt = doc.get('text', '')
    a = txt.find('Capital Improvement Projects (Design)')
    if a > 0:
        b = txt.find('Capital Improvement Projects (Construction)', a)
        if b < 0:
            b = len(txt)
        c = txt[a:b]
        blocks = c.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 20 and 'Design)' not in block:
                lines = [L.strip() for L in block.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    if name and 'Updates' not in name and 'Schedule' not in name and not name.isupper():
                        design.append(name)

cnt = 0
for dname in design:
    dclean = dname.split('(')[0].strip().lower().replace('project', '').strip()
    for fname in funding:
        fclean = fname.split('(')[0].strip().lower().replace('project', '').strip()
        if dclean in fclean or fclean in dclean:
            cnt += 1
            funding.discard(fname)
            break

print('__RESULT__:')
print(json.dumps({'count': cnt}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
