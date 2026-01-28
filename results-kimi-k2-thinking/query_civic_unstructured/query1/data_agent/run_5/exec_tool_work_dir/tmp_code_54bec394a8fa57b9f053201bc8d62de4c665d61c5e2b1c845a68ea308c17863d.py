code = """import json

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:44']))
civic_docs = json.load(open(locals()['var_functions.query_db:2']))

# Get funded projects > $50k
funding_set = set([r['Project_Name'] for r in funding_data])
print('Funding projects:', len(funding_set))

# Extract design projects
design_names = []
for doc in civic_docs:
    txt = doc.get('text', '')
    dstart = txt.find('Capital Improvement Projects (Design)')
    if dstart < 0:
        continue
    cstart = txt.find('Capital Improvement Projects (Construction)', dstart)
    if cstart < 0:
        cstart = len(txt)
    section = txt[dstart:cstart]
    items = section.split('\n\n')
    for item in items:
        item = item.strip()
        if item and len(item) > 20:
            lines = [L.strip() for L in item.split('\n') if L.strip()]
            if lines:
                name = lines[0]
                if name and 'Updates' not in name and 'Schedule' not in name and not name.isupper():
                    design_names.append(name)

print('Design names:', len(design_names))

# Count matches
matched = 0
for dname in design_names:
    dclean = dname.split('(')[0].strip().lower()
    dclean = dclean.replace('project', '').strip()
    for fname in list(funding_set):
        fclean = fname.split('(')[0].strip().lower()
        fclean = fclean.replace('project', '').strip()
        if dclean in fclean or fclean in dclean:
            matched += 1
            funding_set.discard(fname)
            break

out = json.dumps({'count': matched})
print('__RESULT__:')
print(out)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
