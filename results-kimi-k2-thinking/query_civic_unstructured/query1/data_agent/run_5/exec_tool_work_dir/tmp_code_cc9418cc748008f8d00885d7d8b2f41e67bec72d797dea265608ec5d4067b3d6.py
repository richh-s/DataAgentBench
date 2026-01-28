code = """import json

# Load data
with open(locals()['var_functions.query_db:0']) as f:
    funding_recs = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Filter funding > 50000
funding = {rec['Project_Name']: int(rec['Amount']) for rec in funding_recs if int(rec['Amount']) > 50000}

print('Funded projects count:', len(funding))

# Extract design status projects
design_names = []

for doc in civic_docs:
    txt = doc.get('text', '')
    
    # Find design section
    dstart = txt.find('Capital Improvement Projects (Design)')
    if dstart >= 0:
        cstart = txt.find('Capital Improvement Projects (Construction)', dstart)
        if cstart <0:
            cstart = len(txt)
        section = txt[dstart:cstart]
        
        blocks = section.split('\n\n')
        for block in blocks:
            block = block.strip()
            if len(block) > 20 and 'Design)' not in block:
                lines = [L.strip() for L in block.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    if name and 'Updates' not in name and 'Schedule' not in name and len(name) > 10:
                        design_names.append(name)

print('Design projects count:', len(design_names))

# Match projects
def clean(n):
    n2 = n.split('(')[0]
    n2 = n2.replace('Project', '').replace('Improvements', '').replace('Repairs', '')
    return n2.strip().lower()

matched = []
used = set()

for dname in design_names:
    dclean = clean(dname)
    for fund_name in funding:
        if fund_name in used:
            continue
        fclean = clean(fund_name)
        if dclean in fclean or fclean in dclean:
            matched.append({'project': fund_name, 'amount': funding[fund_name]})
            used.add(fund_name)

print('Final matched count:', len(matched))

result = {'count': len(matched), 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
