code = """import json
funding_file = open('/root/shared_data/var_functions.query_db:50.json')
# Read funding data
f = json.load(funding_file)
funding_file.close()

# Simple approach: count projects with 2022 in name
spring_projects = []
total_funding = 0

for record in f:
    name = record['Project_Name']
    amount = int(record['Amount'])
    # Count if project explicitly mentions 2022 in name
    if '2022' in name and ('Spring' in name or 'Street' in name or 'Annual' in name):
        spring_projects.append(name)
        total_funding += amount

# Also check for projects with 2022-03, 2022-04, 2022-05 patterns
march_may_projects = []
for record in f:
    name = record['Project_Name']
    amount = int(record['Amount'])
    if '2022' in name and any(m in name for m in ['March','April','May']):
        march_may_projects.append(name)
        total_funding += amount

# Combine results (avoid double counting)
all_spring = set(spring_projects + march_may_projects)

result = dict()
result['project_count'] = len(all_spring)
result['total_funding'] = total_funding

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
