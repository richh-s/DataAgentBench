code = """import json, re, os

f = open('/root/shared_data/var_functions.query_db:5.json', 'r')
funding = json.load(f)
f.close()

c = open('/root/shared_data/var_functions.query_db:2.json', 'r')
civic = json.load(c)
c.close()

print('Loaded data')

spring_projs = []
for doc in civic:
    txt = doc['text']
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        lines = txt.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                for j in reversed(range(max(0,i-5), i)):
                    name = lines[j].strip()
                    if name and len(name) > 15 and not name.startswith('('):
                        spring_projs.append(name)
                        break
                break

matched = set()
total = 0
for fund in funding:
    fname = fund['Project_Name']
    for proj in spring_projs:
        if fname in proj or proj in fname:
            if fname not in matched:
                matched.add(fname)
                total += int(fund['Amount'])
                break

result = json.dumps({'project_count': len(matched), 'total_funding': total})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
