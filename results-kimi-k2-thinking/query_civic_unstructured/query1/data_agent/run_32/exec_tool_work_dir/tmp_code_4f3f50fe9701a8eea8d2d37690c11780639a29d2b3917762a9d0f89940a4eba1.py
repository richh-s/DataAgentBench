code = """import json

civic_docs_path = locals()['var_functions.query_db:5']
funding_path = locals()['var_functions.query_db:30']

with open(civic_docs_path) as f:
    docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

# Map project names to amounts
funded = {}
for rec in funding:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funded[name] = amount

capital_design = set()

for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1]
        section = section.split('Capital Improvement Projects (Construction)')[0]
        lines = section.split('\n')
        for line in lines:
            clean = line.strip()
            if clean and clean in funded:
                capital_design.add(clean)

for proj_name in funded:
    if proj_name in capital_design:
        continue
    if 'fema' in proj_name.lower():
        continue
    
    for doc in docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            idx = txt.find(proj_name)
            snippet = txt[max(0, idx-200):min(len(txt), idx+len(proj_name)+200)]
            if 'design' in snippet.lower():
                capital_design.add(proj_name)
                break

print('__RESULT__:')
print(str(len(capital_design)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
