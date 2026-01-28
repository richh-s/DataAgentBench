code = """import json
civic_docs_file = str(locals()['var_functions.query_db:5'])
funding_file = str(locals()['var_functions.query_db:30'])

with open(civic_docs_file) as f:
    docs = json.load(f)

with open(funding_file) as f:
    funding = json.load(f)

funded = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

capital_design = set()

for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1]
        section = section.split('Capital Improvement Projects (Construction)')[0]
        for line in section.split('\n'):
            clean = line.strip()
            if clean in funded:
                capital_design.add(clean)

for proj_name in funded:
    if proj_name in capital_design or 'fema' in proj_name.lower():
        continue
    
    for doc in docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            pos = txt.find(proj_name)
            snippet = txt[pos-200 if pos > 200 else 0 : pos+len(proj_name)+200]
            if 'design' in snippet.lower():
                capital_design.add(proj_name)
                break

print('__RESULT__:')
print(str(len(capital_design)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
