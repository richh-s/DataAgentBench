code = """import json, re

# Load funding data
funding_file = locals()['var_functions.query_db:96']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:40']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

high_funding = set(rec['Project_Name'] for rec in funding_data)

design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start < 0:
        continue
    end = text.find('Capital Improvement Projects (Construction)', start)
    if end < 0:
        end = len(text)
    design_section = text[start:end]
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
            clean = re.sub(r'^(cid:\d+)\s*', '', line)
            if len(clean) > 10:
                design_projects.add(clean)

exact_matches = high_funding.intersection(design_projects)
match_count = len(exact_matches)

if match_count == 0:
    norm_funding = {name.lower().strip() for name in high_funding}
    for project in design_projects:
        if project.lower().strip() in norm_funding:
            match_count += 1

result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:94': ['Funding'], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json'}

exec(code, env_args)
