code = """import json

# Load data
cpath = locals()['var_functions.query_db:44']
fpath = locals()['var_functions.query_db:31']

cdocs = json.load(open(cpath))
fdocs = json.load(open(fpath))

# Build funding map
funding = {}
for r in fdocs:
    n = r['Project_Name']
    a = int(r['Amount'])
    funding[n] = funding.get(n, 0) + a

# Find projects mentioning Spring 2022
projects = []
for doc in cdocs:
    t = doc.get('text', '')
    if '2022' in t:
        for line in t.split('\n'):
            line = line.strip()
            if '2022' in line and 'Spring' in line:
                projects.append(line)

deduped = list(dict.fromkeys(projects))

# Count matching projects
count = 0
total = 0
for proj in deduped:
    if proj in funding:
        count += 1
        total += funding[proj]

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
