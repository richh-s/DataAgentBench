code = """import json

civic_docs_file = locals()['var_functions.query_db:5']
funding_50k_file = locals()['var_functions.query_db:30']

with open(civic_docs_file) as fp:
    docs = json.load(fp)

with open(funding_50k_file) as fp:
    funding = json.load(fp)

# Map names to amounts
amounts = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

projects = set()

# Look in design sections
for doc in docs:
    txt = doc.get('text', '')
    pos = txt.find('Capital Improvement Projects (Design)')
    if pos != -1:
        end_pos = txt.find('Capital Improvement Projects (Construction)', pos)
        if end_pos != -1:
            section = txt[pos:end_pos]
            for line in section.split('\n'):
                clean = line.strip()
                if clean and clean in amounts:
                    projects.add(clean)

# Broad search
for proj_name in amounts:
    if proj_name in projects:
        continue
    if 'fema' in proj_name.lower():
        continue
    
    for doc in docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            pos = txt.find(proj_name)
            snippet = txt[max(0, pos-200):min(len(txt), pos+len(proj_name)+200)]
            if 'design' in snippet.lower():
                projects.add(proj_name)
                break

print('__RESULT__:')
print(str(len(projects)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
