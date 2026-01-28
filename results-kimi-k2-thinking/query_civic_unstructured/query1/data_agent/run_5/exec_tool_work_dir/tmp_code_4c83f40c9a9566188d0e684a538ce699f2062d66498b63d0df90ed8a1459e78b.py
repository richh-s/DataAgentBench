code = """import json

with open(locals()['var_functions.query_db:44']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

# Funding map
funding_dict = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

# Extract design projects
design_names = []
for doc in docs:
    txt = doc.get('text', '')
    if 'Design' in txt:
        lines = txt.split('\n')
        for line in lines:
            if 'Design' in line and 'Capital' in line:
                continue
            if line.strip() and len(line.strip()) > 10:
                if not line.strip().startswith('(') and not line.strip().startswith('•'):
                    if 'Updates' not in line and 'Schedule' not in line:
                        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
                            design_names.append(line.strip())

# Match
def clean(n):
    n2 = n.split('(')[0].strip().lower()
    n2 = n2.replace('project', '').strip()
    return n2

matched = 0
for dname in design_names:
    dclean = clean(dname)
    for fund_name in list(funding_dict.keys()):
        fclean = clean(fund_name)
        if dclean in fclean or fclean in dclean:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
