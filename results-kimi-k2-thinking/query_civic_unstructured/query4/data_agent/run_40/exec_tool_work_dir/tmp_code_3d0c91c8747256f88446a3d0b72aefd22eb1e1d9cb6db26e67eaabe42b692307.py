code = """import json, re, os

# Load data files
with open('/root/shared_data/var_functions.query_db:5.json') as f:
    funding = json.load(f)
    
with open('/root/shared_data/var_functions.query_db:2.json') as f:
    civic = json.load(f)

print('Data loaded:', len(funding), 'funding records,', len(civic), 'civic docs')

# Extract Spring 2022 projects from civic documents
spring_names = []
for doc in civic:
    txt = doc['text']
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        lines = txt.split('\n')
        for i,line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backwards up to 5 lines for project name
                start = max(0,i-5)
                for j in range(i-1,start-1,-1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate)>15 and not candidate.startswith('('):
                        spring_names.append(candidate)
                        break
                break

print('Found candidate projects:', len(spring_names))

# Match with funding
total = 0
matched = set()
for fund in funding:
    fname = fund['Project_Name']
    amt = int(fund['Amount'])
    for proj in spring_names:
        if fname in proj or proj in fname:
            if fname not in matched:
                matched.add(fname)
                total += amt
                break

result = json.dumps({'project_count': len(matched), 'total_funding': total})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
