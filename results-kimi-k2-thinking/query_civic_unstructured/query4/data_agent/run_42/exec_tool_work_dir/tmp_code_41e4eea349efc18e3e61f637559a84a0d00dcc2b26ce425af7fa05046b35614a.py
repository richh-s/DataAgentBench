code = """import json

# Load from variables
mongo_result = var_functions.query_db:42
funding_result = var_functions.query_db:4

# Read MongoDB data
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result

# Read funding data
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_recs = json.load(f)
else:
    funding_recs = funding_result

# Build funding lookup
d = {r['Project_Name']: int(r['Amount']) for r in funding_recs}

# Extract Spring 2022 projects
spring = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text and 'Begin Construction' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line:
                for j in range(i-1, max(i-6, -1), -1):
                    cand = lines[j].strip()
                    if cand and cand[0] != '(' and 'Schedule' not in cand:
                        spring.add(cand)
                        break

# Match projects
matches = [{"name": p, "funding": d[p]} for p in spring if p in d]

count = len(matches)
total = sum(m["funding"] for m in matches)

# Print in exact format required
print('__RESULT__:')
print(json.dumps({"project_count": count, "total_funding": total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
