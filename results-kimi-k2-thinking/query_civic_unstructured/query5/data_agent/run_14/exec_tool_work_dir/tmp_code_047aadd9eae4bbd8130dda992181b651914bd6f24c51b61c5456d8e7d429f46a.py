code = """import json
import re

f_path = locals()['var_functions.query_db:10']
d_path = locals()['var_functions.query_db:2']

with open(f_path) as f:
    funding = json.load(f)

with open(d_path) as f:
    docs = json.load(f)

for r in funding:
    r['Amount'] = int(r['Amount'])

found = []
for doc in docs:
    lines = doc['text'].split('\n')
    for i,line in enumerate(lines):
        line=line.strip()
        if not line: continue
        if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
            name=line
            check_lines=lines[max(0,i-10):min(len(lines),i+20)]
            for cl in check_lines:
                if '2022' in cl:
                    low=cl.lower()
                    if any(k in low for k in ['begin','start','advertise','complete design','spring','summer','fall','winter']):
                        found.append(name)
                        break

found=list(set(found))

print('__RESULT__:')
print(json.dumps({'count':len(found),'projects':found}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:24': {'fund_count': 500, 'doc_count': 5}}

exec(code, env_args)
