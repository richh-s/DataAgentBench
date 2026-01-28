code = """import json, re

with open('/tmp/tmp_3z7x6gk.json', 'r') as f:
    funding_data = json.load(f)

with open('/tmp/tmp_2z4l8jq.json', 'r') as f:
    spring_docs = json.load(f)

print('Funding records count:', len(funding_data))

spring_projects = []
for doc in spring_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring' in line and '2022' in line and 'construction' in line.lower():
            for j in range(i-1, max(-1, i-10), -1):
                prev = lines[j].strip()
                if prev and not prev.startswith('(') and not prev.startswith('•') and len(prev) < 150:
                    bad_words = ['update', 'schedule', 'status', 'description', 'begin construction']
                    if not any(w in prev.lower() for w in bad_words):
                        spring_projects.append(prev)
                        break

unique = list(set(spring_projects))
print('Spring 2022 projects count:', len(unique))

funding_lookup = {item['Project_Name']: int(item['Amount']) for item in funding_data}

total = 0
for proj in unique:
    if proj in funding_lookup:
        total += funding_lookup[proj]
    else:
        # partial match
        for funded_name, amount in funding_lookup.items():
            if proj in funded_name or funded_name in proj:
                total += amount
                break

result = {'spring_2022_project_count': len(unique), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
