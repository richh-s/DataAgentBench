code = """import json, re

with open('/tmp/tmp_3z7x6gk.json', 'r') as f:
    funding = json.load(f)

with open('/tmp/tmp_2z4l8jq.json', 'r') as f:
    spring = json.load(f)

print('Funding:', len(funding))
print('Spring docs:', len(spring))

projects = []
for doc in spring:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring' in line and '2022' in line:
            low = line.lower()
            if 'construction' in low or 'advertise' in low:
                name = None
                for j in range(i-1, max(-1, i-10), -1):
                    prev = lines[j].strip()
                    if prev and not prev.startswith('(') and not prev.startswith('•'):
                        if len(prev) < 200:
                            bad = ['update', 'schedule', 'status']
                            if not any(w in prev.lower() for w in bad):
                                name = prev
                                break
                if name and name not in projects:
                    projects.append(name)

print('Projects starting Spring 2022:', len(projects))

funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding}

total = 0
matched = 0
for proj in projects:
    if proj in funding_dict:
        total += funding_dict[proj]
        matched += 1
    else:
        for f_name, amt in funding_dict.items():
            if proj in f_name or f_name in proj:
                total += amt
                matched += 1
                break

print('Matched:', matched)
print('Total funding:', total)

result = {'project_count': len(projects), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
