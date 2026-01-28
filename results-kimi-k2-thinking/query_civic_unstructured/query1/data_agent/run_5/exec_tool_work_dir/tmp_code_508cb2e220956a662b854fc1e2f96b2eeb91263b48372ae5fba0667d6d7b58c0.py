code = """import json

# Load funding data > $50k
with open(locals()['var_functions.query_db:44']) as f:
    funding = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

funding_names = set()
funding_dict = {}
for rec in funding:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funding_names.add(name)
    funding_dict[name] = amt

print('Funding count:', len(funding_names))

# Extract design projects
design_list = []
for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        parts = txt.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            blocks = section.split('\n\n')
            for block in blocks:
                block = block.strip()
                if block and 'Design)' not in block and len(block) > 20:
                    lines = block.split('\n')
                    if lines:
                        name = lines[0].strip()
                        if name and 'Updates' not in name and 'Schedule' not in name and not name.isupper():
                            design_list.append(name)

print('Design list count:', len(design_list))

# Match projects
def clean(n):
    n2 = n.split('(')[0].strip().lower()
    n2 = n2.replace('project', '').strip()
    return n2

matched = 0
for dname in design_list:
    dclean = clean(dname)
    for fund_name in list(funding_names):
        fclean = clean(fund_name)
        if dclean in fclean or fclean in dclean:
            matched += 1
            funding_names.discard(fund_name)
            break

result = {'total_capital_design_projects_with_funding_over_50k': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
