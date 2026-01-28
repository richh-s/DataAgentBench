code = """import json, re

# Load data
with open('/tmp/tmp_2z4l8jq.json', 'r') as f:
    spring_docs = json.load(f)

# Extract project names
projects = []
for doc in spring_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring' in line and '2022' in line and 'construction' in line.lower():
            name = None
            for j in range(i-1, max(-1, i-10), -1):
                prev = lines[j].strip()
                if prev and not prev.startswith('(') and not prev.startswith('•'):
                    bad = ['update', 'schedule', 'status', 'description']
                    if not any(w in prev.lower() for w in bad):
                        name = prev
                        break
            if name:
                projects.append(name)

unique = list(set(projects))
print('Projects:', len(unique))

# Load funding
with open('/tmp/tmp_3z7x6gk.json', 'r') as f:
    funding = json.load(f)

funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding}

total = 0
for proj in unique:
    if proj in funding_dict:
        total += funding_dict[proj]
    else:
        for funded_name, amount in funding_dict.items():
            if proj in funded_name or funded_name in proj:
                total += amount
                break

result = {'project_count': len(unique), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
