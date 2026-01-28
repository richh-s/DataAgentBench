code = """import json, re

# Load data
m_path = locals()['var_functions.query_db:42']
f_path = locals()['var_functions.query_db:4']

with open(m_path) as f:
    mongo_docs = json.load(f)
with open(f_path) as f:
    funding_recs = json.load(f)

# Create funding lookup
d = {r['Project_Name']: int(r['Amount']) for r in funding_recs}

# Extract projects starting Spring 2022
spring = set()

for doc in mongo_docs:
    text = doc.get('text','')
    lines = text.split('\n')
    for i in range(len(lines)):
        if 'Begin Construction' in lines[i] and 'Spring' in lines[i] and '2022' in lines[i]:
            for j in range(i-1, max(i-10, -1), -1):
                line = lines[j].strip()
                if line and not line.startswith('(') and 'Schedule' not in line:
                    spring.add(line)
                    break

# Match with funding
matches = [{"name": p, "funding": d[p]} for p in spring if p in d]

result = json.dumps({
    "count": len(matches),
    "total_funding": sum(m["funding"] for m in matches),
    "projects": matches
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
