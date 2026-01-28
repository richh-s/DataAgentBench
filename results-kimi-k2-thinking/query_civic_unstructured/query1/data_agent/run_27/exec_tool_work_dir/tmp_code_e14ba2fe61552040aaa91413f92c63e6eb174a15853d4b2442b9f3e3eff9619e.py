code = """import json

civic_docs = locals()['var_functions.query_db:2']
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

funding_data = locals()['var_functions.query_db:6']
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

funded_map = {}
for f in funding_data:
    amount = int(f['Amount'])
    if amount > 50000:
        funded_map[f['Project_Name']] = amount

count = 0
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1][:3000]
        for line in section.split('\n'):
            clean = line.strip()
            if clean and len(clean) > 15:
                bad = any(x in clean for x in ['Updates', 'Schedule', 'Page', 'To:', 'From:'])
                if not bad and not clean.startswith('('):
                    is_disaster = any(x in clean for x in ['(FEMA', '(CalOES', '(CalJPIA'])
                    if not is_disaster and clean in funded_map:
                        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
