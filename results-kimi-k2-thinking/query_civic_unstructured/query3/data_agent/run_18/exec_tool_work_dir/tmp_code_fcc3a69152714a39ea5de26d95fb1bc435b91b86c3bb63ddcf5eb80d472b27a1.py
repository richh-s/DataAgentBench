code = """import json, os

funding_path = locals()['var_functions.query_db:2']
docs_path = locals()['var_functions.query_db:0']

with open(funding_path) as f:
    funding_recs = json.load(f)
with open(docs_path) as f:
    civic_docs = json.load(f)

results = []
emergency_funding = []

for rec in funding_recs:
    name_lc = rec['Project_Name'].lower()
    if 'emergency' in name_lc or 'fema' in name_lc:
        emergency_funding.append(rec)

project_status = {}
for doc in civic_docs:
    doc_text = doc['text'].lower()
    lines = doc['text'].split('\n')
    for line in lines:
        clean_line = line.strip()
        if clean_line:
            lc_line = clean_line.lower()
            if 'emergency' in lc_line or 'fema' in lc_line or 'warning' in lc_line or 'siren' in lc_line:
                st = 'not started'
                if 'under construction' in doc_text and lc_line in doc_text:
                    st = 'completed'
                elif 'design' in doc_text and 'complete design' not in doc_text:
                    st = 'design'
                project_status[clean_line] = st

for pf in emergency_funding:
    pn = pf['Project_Name']
    st = project_status.get(pn, 'not started')
    pt = 'disaster' if 'fema' in pn.lower() else 'capital'
    results.append({
        'Project_Name': pn,
        'Funding_Source': pf['Funding_Source'],
        'Amount': pf['Amount'],
        'Status': st,
        'Type': pt
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}}

exec(code, env_args)
