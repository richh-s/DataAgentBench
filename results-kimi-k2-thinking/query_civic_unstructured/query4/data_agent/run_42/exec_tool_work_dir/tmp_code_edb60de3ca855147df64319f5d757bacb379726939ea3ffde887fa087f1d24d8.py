code = """import json

# Load data from MongoDB query - file contains projects with Begin Construction dates
mongo_file = '/tmp/tmp9z4c2iv0.json'
funding_file = '/tmp/tmps9c7b2d8.json'

# Read data
mongo_docs = json.loads(open(mongo_file).read())
funding_recs = json.loads(open(funding_file).read())

# Build funding lookup dictionary
f = {rec['Project_Name']: int(rec['Amount']) for rec in funding_recs}

# Find Spring 2022 projects
spring = set()
for doc in mongo_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        if 'Begin Construction' in lines[i] and '2022' in lines[i]:
            for j in range(i-1, max(i-8, -1), -1):
                cand = lines[j].strip()
                if cand and cand[0] != '(' and 'Schedule' not in cand:
                    if len(cand) > 5:
                        spring.add(cand)
                        break

# Match and calculate
m = [{'name': p, 'funding': f[p]} for p in spring if p in f]
cnt = len(m)
total = sum(x['funding'] for x in m)

# Output exactly as required
result = "COUNT=" + str(cnt) + " TOTAL=$" + str(total)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
