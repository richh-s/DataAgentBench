code = """import json

f_path = locals()['var_functions.query_db:10']
p_path = locals()['var_functions.query_db:36']

with open(f_path) as f:
    funding = json.load(f)

with open(p_path) as f:
    docs = json.load(f)

for r in funding:
    r['Amount'] = int(r['Amount'])

names = set()
for doc in docs:
    txt = doc['text']
    if '2022' in txt:
        lines = txt.split('\n')
        for line in lines:
            line = line.strip()
            if line and ('(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line):
                names.add(line)

matched = []
for name in names:
    base = name.split('(')[0].strip()
    for f in funding:
        if name in f['Project_Name'] or f['Project_Name'].startswith(base):
            matched.append(f)

seen = {}
for f in matched:
    seen[f['Funding_ID']] = f

total = sum(f['Amount'] for f in seen.values())

print('__RESULT__:')
print(json.dumps({'total': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:24': {'fund_count': 500, 'doc_count': 5}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
