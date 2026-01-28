code = """import json

# Get file paths
civic_file = str(var_functions.query_db:42)
funding_file = str(var_functions.query_db:18)

# Load data
with open(civic_file, 'r') as f:
    docs = json.load(f)

with open(funding_file, 'r') as f:
    funds = json.load(f)

# Find Spring 2022 projects
spring_set = set()
for doc in docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and ('March' in line or 'April' in line or 'May' in line):
            for j in range(max(0, i-5), i):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and prev[0].isupper():
                    if 'Updates:' not in prev:
                        spring_set.add(prev)
                        break

# Calculate funding
matches = []
total = 0
for proj in spring_set:
    for f in funds:
        name = f['Project_Name']
        if proj.lower() == name.lower() or name.lower() in proj.lower():
            amt = int(f['Amount'])
            total += amt
            matches.append([proj, name, amt])
            break

result_str = json.dumps({'count': len(spring_set), 'total': total, 'matches': len(matches)})
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
