code = """import json

# Load funding data
funding_data = json.load(open(locals()['var_functions.query_db:44']))
civic_data = json.load(open(locals()['var_functions.query_db:2']))

# Get projects with funding > $50k
funding_names = set([rec['Project_Name'] for rec in funding_data])
print('Funding count', len(funding_names))

# Extract design projects
design_names = []
for doc in civic_data:
    txt = doc.get('text', '')
    dstart = txt.find('Capital Improvement Projects (Design)')
    if dstart < 0:
        continue
    cstart = txt.find('Capital Improvement Projects (Construction)', dstart)
    if cstart < 0:
        cstart = len(txt)
    section = txt[dstart:cstart]
    parts = section.split('\n\n')
    for blk in parts:
        blk = blk.strip()
        if blk and 'Design)' not in blk and len(blk) > 20:
            lines = [L.strip() for L in blk.split('\n') if L.strip()]
            if lines:
                first = lines[0]
                if first and 'Updates' not in first and 'Schedule' not in first and not first.isupper():
                    design_names.append(first)

print('Design count', len(design_names))

# Match
matched = 0
for dname in design_names:
    dclean = dname.split('(')[0].strip().lower()
    dclean = dclean.replace('project', '').strip()
    for fname in list(funding_names):
        fclean = fname.split('(')[0].strip().lower()
        fclean = fclean.replace('project', '').strip()
        if dclean in fclean or fclean in dclean:
            matched += 1
            funding_names.discard(fname)
            break

print('Matched', matched)
result = json.dumps({'count': matched})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
