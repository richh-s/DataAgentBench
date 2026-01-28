code = """park_projects = []
for doc in civic_docs_data:
    for line in doc.get('text','').split('\n'):
        line_clean = line.strip()
        if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
            park_projects.append(line_clean)

print('Found', len(park_projects), 'lines with park')

# Simple matching
matched_records = []
for fund in funding_data:
    fund_name = fund.get('Project_Name','').lower()
    for park in park_projects:
        if 'park' in fund_name and '2022' in fund.get('Project_Name',''):
            matched_records.append(int(fund.get('Amount',0)))

result = {'total_funding': sum(matched_records)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
