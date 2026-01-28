code = """import json, re, os

# Load funding data
fund_path = '/root/shared_data/var_functions.query_db:50.json'
civic_path = '/root/shared_data/var_functions.query_db:72.json'

with open(fund_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    civic = json.load(f)

print('Loaded data')

# Find Spring 2022 projects
spring_names = []
for doc in civic:
    text = doc.get('text','')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for i,line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                for j in reversed(range(max(0,i-5),i)):
                    candidate = lines[j].strip()
                    if candidate and len(candidate)>15 and not candidate.startswith('('):
                        spring_names.append(candidate)
                        break
                break

print('Candidates:', len(spring_names))

# Match with funding
total=0
matched=set()
for fund in funding:
    fname=fund['Project_Name']
    amt=int(fund['Amount'])
    for proj in spring_names:
        if fname in proj or proj in fname or any(w in fname for w in proj.split() if len(w)>4):
            if fname not in matched:
                matched.add(fname)
                total+=amt
                break

result={'project_count':len(matched),'total_funding':total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
