code = """import json

funding = json.load(open(locals()['var_functions.query_db:44']))
civic = json.load(open(locals()['var_functions.query_db:2']))

funding_set = set()
for rec in funding:
    funding_set.add(rec['Project_Name'])

print('Funding projects:', len(funding_set))

design_list = []
for doc in civic:
    txt = doc.get('text', '')
    if 'Projects (Design)' in txt:
        parts = txt.split('Projects (Design)')
        section = parts[1].split('Projects (Construction)')[0]
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if block and len(block) > 15:
                lines = [L.strip() for L in block.split('\n') if L.strip()]
                if lines and 'Updates' not in lines[0] and 'Schedule' not in lines[0]:
                    design_list.append(lines[0])

print('Design projects:', len(design_list))

matches = 0
unused = set(funding_set)
for dname in design_list:
    d_clean = dname.split('(')[0].lower()
    for fund in list(unused):
        f_clean = fund.split('(')[0].lower()
        if d_clean in f_clean or f_clean in d_clean:
            matches += 1
            unused.discard(fund)
            break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
