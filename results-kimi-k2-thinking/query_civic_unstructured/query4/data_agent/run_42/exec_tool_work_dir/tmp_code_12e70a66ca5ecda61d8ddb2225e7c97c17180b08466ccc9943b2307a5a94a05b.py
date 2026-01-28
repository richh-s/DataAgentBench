code = """import json

# Load data from files
m_path = locals()['var_functions.query_db:42']
f_path = locals()['var_functions.query_db:4']

mongo_docs = json.loads(open(m_path).read())
funding_recs = json.loads(open(f_path).read())

# Build funding lookup
d = {}
for r in funding_recs:
    d[r['Project_Name']] = int(r['Amount'])

# Find Spring 2022 projects
spring = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line and 'Spring' in line:
                for j in range(i-1, max(i-8, -1), -1):
                    candidate = lines[j].strip()
                    if candidate and not candidate.startswith('(') and 'Schedule' not in candidate:
                        spring.add(candidate)
                        break

# Match projects with funding
results = []
for proj in spring:
    if proj in d:
        results.append({'name': proj, 'funding': d[proj]})

count = len(results)
total = sum(r['funding'] for r in results)

answer = 'Projects starting Spring 2022: ' + str(count) + ', Total funding: $' + str(total)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
