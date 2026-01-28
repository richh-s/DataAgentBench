code = """import json, re

f_path = locals()['var_functions.query_db:22']
c_path = locals()['var_functions.query_db:20']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(c_path, 'r') as f:
    civic = json.load(f)

design_set = set()
for doc in civic:
    txt = doc.get('text', '')
    if not txt:
        continue
    match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|$)', txt, re.DOTALL | re.IGNORECASE)
    if match:
        section = match.group(1)
        for line in section.splitlines():
            line = line.strip()
            if len(line) > 5 and not line[0] in '(-•' and not line.isupper() and 'cid:' not in line:
                if not any(term in line.lower() for term in ['updates', 'schedule', 'page', 'commission']):
                    if line.lower() not in ['design', 'construction']:
                        design_set.add(line)

print('Design projects count:', len(design_set))

results = []
for item in funding:
    if int(item['Amount']) > 50000 and item['Project_Name'] in design_set:
        results.append({'name': item['Project_Name'], 'amount': int(item['Amount'])})

print('Matching projects:', len(results))
print(json.dumps({'count': len(results), 'projects': results}))
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:18': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
