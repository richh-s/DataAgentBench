code = """import json

# Load data
funding_file = locals()['var_functions.query_db:42']
civic_file = locals()['var_functions.query_db:52']

with open(funding_file) as f:
    funding_data = json.load(f)
with open(civic_file) as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_dict = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if name:
        amount = int(str(rec.get('Amount', 0)))
        funding_dict[name] = funding_dict.get(name, 0) + amount

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022' in text and ('spring' in text or 'march' in text or 'april' in text or 'may' in text):
        # Simple heuristic: project names are uppercase lines
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isupper() and len(line) < 80:
                # Skip headers
                if all(x not in line.lower() for x in ['page', 'agenda', 'item', 'commission', 'public works']):
                    spring_projects.append(line)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match funding
count = 0
total = 0
for proj in spring_projects:
    if proj in funding_dict:
        count += 1
        total += funding_dict[proj]
    else:
        # Try partial match for variants
        proj_base = proj.split(' (')[0]
        for funded in funding_dict:
            if funded.startswith(proj_base):
                count += 1
                total += funding_dict[funded]
                break

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'funding_records': 500, 'civic_documents': 5, 'status': 'data_loaded'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'civic_docs_loaded': 5, 'funding_records_loaded': 500, 'status': 'ready_to_process'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 3}, 'var_functions.list_db:50': ['civic_docs'], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
