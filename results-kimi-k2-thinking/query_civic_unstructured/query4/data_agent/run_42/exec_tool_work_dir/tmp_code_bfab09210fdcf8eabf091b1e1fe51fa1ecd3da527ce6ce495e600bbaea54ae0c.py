code = """import json, re

# Load data from the stored query results
mongo_dict = locals()['var_functions.query_db:42']
funding_dict = locals()['var_functions.query_db:4']

# Read the JSON files
with open(mongo_dict, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_dict, 'r') as f:
    funding_recs = json.load(f)

# Build funding lookup
d = {rec['Project_Name']: int(rec['Amount']) for rec in funding_recs}

# Find Spring 2022 projects
spring = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line:
                # Look back for project name
                for j in range(i-1, max(i-6, -1), -1):
                    cand = lines[j].strip()
                    if cand and cand[0] != '(' and 'Schedule' not in cand:
                        if len(cand) > 5:
                            spring.add(cand)
                            break

# Match with funding
matches = [{'name': p, 'funding': d[p]} for p in spring if p in d]

count = len(matches)
total_funding = sum(m['funding'] for m in matches)

result = json.dumps({'project_count': count, 'total_funding': total_funding, 'projects': matches})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
