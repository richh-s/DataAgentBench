code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:40']
with open(funding_path, 'r') as f:
    funding_d = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:5']
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_d = json.load(f)

# Count funded projects > 50000
count_50k = sum(1 for rec in funding_d if int(rec.get('Amount', 0)) > 50000)

# Extract project names from civic docs containing design section
design_names = set()
for doc in civic_d:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        idx = txt.find('Capital Improvement Projects (Design)')
        snippet = txt[idx:idx+2500]
        lines = snippet.split('\n')
        for ln in lines:
            s = ln.strip()
            if len(s) > 10 and 'Project' in s and 'fema' not in s.lower():
                design_names.add(s)

# Match and count
matched = set()
for rec in funding_d:
    if int(rec['Amount']) > 50000:
        name = rec['Project_Name']
        base = name.split('(')[0].strip() if '(' in name else name
        if base in design_names:
            matched.add(base)

# Output
result = {'count': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
