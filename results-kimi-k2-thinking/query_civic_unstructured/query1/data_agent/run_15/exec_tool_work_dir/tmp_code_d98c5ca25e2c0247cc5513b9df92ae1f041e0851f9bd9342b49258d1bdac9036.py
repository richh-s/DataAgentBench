code = """import json

# Load data
with open(locals()['var_functions.query_db:38']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:40']) as f:
    docs = json.load(f)

# High funding > 50000
high_funding = set()
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.add(r['Project_Name'])

# Extract design projects
design = []
for doc in docs:
    text = doc.get('text', '')
    if text.find('Capital Improvement Projects (Design)') > -1:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            for line in section.split('\n'):
                line = line.strip()
                if line and len(line) > 15 and line[0] != '(':
                    if 'Updates:' not in line and 'Schedule:' not in line:
                        clean = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                        if len(clean) > 15:
                            design.append(clean)

# Count matches
matches = [p for p in design if p in high_funding]

result = {
    'high_funding_count': len(high_funding),
    'design_count': len(design),
    'match_count': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
