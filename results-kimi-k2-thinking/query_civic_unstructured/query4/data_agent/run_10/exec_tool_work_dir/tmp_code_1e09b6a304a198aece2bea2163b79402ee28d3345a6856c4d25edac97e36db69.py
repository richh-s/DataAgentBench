code = """import json

funding_path = locals()['var_functions.query_db:8']
civic_path = locals()['var_functions.query_db:4']

with open(funding_path, 'r') as f:
    funding_items = json.load(f)

with open(civic_path, 'r') as f:
    civic_items = json.load(f)

funding_dict = {}
for item in funding_items:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[name] = funding_dict.get(name, 0) + amount

spring_candidates = set()
for doc in civic_items:
    text = doc.get('text', '')
    t = text.lower()
    if 'spring 2022' in t or '2022-spring' in t:
        for line in text.split('\n'):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 15:
                low = line.lower()
                if 'project' in low or 'improvement' in low or 'repair' in low:
                    spring_candidates.add(line)

matched = {}
for proj in spring_candidates:
    if proj in funding_dict:
        matched[proj] = funding_dict[proj]
    else:
        for funded in funding_dict:
            if proj.lower() in funded.lower():
                matched[funded] = funding_dict[funded]
                break

count = len(matched)
total = sum(matched.values())

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
