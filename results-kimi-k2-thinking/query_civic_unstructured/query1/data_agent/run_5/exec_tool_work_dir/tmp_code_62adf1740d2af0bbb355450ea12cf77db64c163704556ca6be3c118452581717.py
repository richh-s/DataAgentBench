code = """import json

with open(locals()['var_functions.query_db:0']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

# Funding > $50k
funding_map = {}
for rec in funding:
    if int(rec['Amount']) > 50000:
        funding_map[rec['Project_Name']] = int(rec['Amount'])

print('Funding count:', len(funding_map))

# Extract design projects
design_names = []

for doc in docs:
    txt = doc.get('text', '')
    
    # Find design section
    dstart = txt.find('Capital Improvement Projects (Design)')
    if dstart > 0:
        cstart = txt.find('Capital Improvement Projects (Construction)', dstart)
        if cstart < 0:
            cstart = len(txt)
        section = txt[dstart:cstart]
        
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if len(block) > 20:
                lines = [L.strip() for L in block.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    if (name and 'Updates' not in name and 'Schedule' not in name
                        and not name.startswith('(') and not name.startswith('•')
                        and not name.isupper() and len(name) > 10):
                        design_names.append(name)

print('Design count:', len(design_names))

# Match
def clean(n):
    n = n.split('(')[0]
    n = n.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return n.strip().lower()

matched = []
used = set()

for dname in design_names:
    d_clean = clean(dname)
    for fund_name in funding_map:
        if fund_name in used:
            continue
        f_clean = clean(fund_name)
        if d_clean in f_clean or f_clean in d_clean:
            matched.append({'project': fund_name, 'amount': funding_map[fund_name]})
            used.add(fund_name)

print('Matched:', len(matched))

for i, p in enumerate(matched[:10]):
    print(f"{i+1}. {p['project']} - ${p['amount']}")

result = {'count': len(matched), 'projects': matched[:15]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
