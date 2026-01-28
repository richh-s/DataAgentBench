code = """import json

funding = json.load(open(locals()['var_functions.query_db:72']))

with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

funding_names = set([r['Project_Name'] for r in funding])

print('Funding records:', len(funding_names))

design_names = []
for d in docs:
    t = d.get('text', '')
    if 'Design' in t:
        i = t.find('Capital Improvement Projects (Design)')
        if i > 0:
            j = t.find('Capital Improvement Projects (Construction)', i)
            if j < 0:
                j = len(t)
            s = t[i:j]
            blocks = s.split('\n\n')
            for b in blocks:
                b = b.strip()
                if b and len(b) > 10 and 'Design)' not in b:
                    lines = b.split('\n')
                    if lines:
                        name = lines[0].strip()
                        if len(name) > 5 and name and 'Updates' not in name:
                            design_names.append(name)

print('Design names:', len(design_names))

matches = 0
for dn in design_names:
    dclean = dn.split('(')[0].strip().lower()
    dclean = dclean.replace('project', '').strip()
    for fn in list(funding_names):
        fclean = fn.split('(')[0].strip().lower()
        fclean = fclean.replace('project', '').strip()
        if dclean in fclean or fclean in dclean:
            matches += 1
            funding_names.discard(fn)
            break

print('Result count:', matches)
result = json.dumps({'count': matches, 'sample_design': design_names[:5]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
