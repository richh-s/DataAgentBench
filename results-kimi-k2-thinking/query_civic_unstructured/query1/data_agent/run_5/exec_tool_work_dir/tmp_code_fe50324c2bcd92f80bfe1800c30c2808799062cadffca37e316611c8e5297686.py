code = """import json

# load data
funding = json.load(open(locals()['var_functions.query_db:72']))
civic = json.load(open(locals()['var_functions.query_db:2']))

# funding projects set
funding_names = set()
for rec in funding:
    funding_names.add(rec['Project_Name'])

# extract design projects
design = []
for doc in civic:
    txt = doc.get('text', '')
    idx = txt.find('Projects (Design)')
    if idx > 0:
        section = txt[idx:idx+3000]
        parts = section.split('\n\n')
        for part in parts:
            part = part.strip()
            if part and len(part) > 20 and 'Design)' not in part:
                line = part.split('\n')[0].strip()
                if line and 'Updates' not in line and len(line) > 5:
                    design.append(line)

# count matches
matched = 0
for dname in design:
    dclean = dname.split('(')[0].lower()
    dclean = dclean.replace('project', '').strip()
    for fund in list(funding_names):
        fclean = fund.split('(')[0].lower()
        fclean = fclean.replace('project', '').strip()
        if dclean in fclean or fclean in dclean:
            matched += 1
            funding_names.discard(fund)
            break

output = {'count': matched}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
