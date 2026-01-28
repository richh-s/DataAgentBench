code = """import json

# Open files directly
with open('/tmp/tmp1i3q6xjc.json') as f:
    funding_data = json.load(f)

with open('/tmp/tmp6v8h4l_u.json') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amt = int(item['Amount'])
    funding_lookup[name] = funding_lookup.get(name, 0) + amt

# Count Spring 2022 projects and calculate funding
project_count = 0
total_funding = 0
matched_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Count this as a Spring 2022 project document
        project_count += 1
        # Add up all funding as approximation
        for proj_name, amount in funding_lookup.items():
            if proj_name in text:
                total_funding += amount
                matched_projects.append(proj_name)

result = {
    'count': project_count,
    'total_funding': total_funding,
    'matched_projects': len(set(matched_projects))
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}, 'var_functions.execute_python:38': 500, 'var_functions.execute_python:48': {'funding_count': 500, 'civic_count': 5}, 'var_functions.list_db:60': ['civic_docs'], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:84': {'spring_2022_docs': 4, 'funding_projects': 500}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.execute_python:98': {'found_spring': True, 'matched_funding': 8868000}, 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.query_db:112': 'file_storage/functions.query_db:112.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:122': 'file_storage/functions.query_db:122.json', 'var_functions.execute_python:126': {'funding_projects': 500, 'spring_references': 4}}

exec(code, env_args)
