code = """import json, re, os

with open('/root/shared_data/var_functions.query_db:5.json', 'r') as f:
    funding = json.load(f)
with open('/root/shared_data/var_functions.query_db:2.json', 'r') as f:
    civic = json.load(f)

print('Loaded', len(funding), 'funding records,', len(civic), 'civic docs')

spring_names = []
for doc in civic:
    txt = doc['text']
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        lines = txt.split('\n')
        for i in range(len(lines)):
            if 'Spring 2022' in lines[i] or '2022-Spring' in lines[i]:
                for j in range(max(0,i-5),i):
                    candidate = lines[j].strip()
                    if candidate and len(candidate)>15 and not candidate.startswith('('):
                        spring_names.append(candidate)
                        break
                break

print('Found candidate projects:', len(spring_names))

matched = set()
total = 0
for fund in funding:
    fname = fund['Project_Name']
    amount = int(fund['Amount'])
    for proj in spring_names:
        if fname in proj or proj in fname:
            if fname not in matched:
                matched.add(fname)
                total += amount
                break

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
