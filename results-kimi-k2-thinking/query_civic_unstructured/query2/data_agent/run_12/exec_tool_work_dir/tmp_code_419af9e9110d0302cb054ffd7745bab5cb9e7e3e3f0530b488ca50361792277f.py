code = """import json

funding_data = locals()['var_functions.query_db_66']
civic_docs_data = locals()['var_functions.query_db_65']

# Find park projects from civic docs
park_projects = []
for doc in civic_docs_data:
    text = doc.get('text','')
    txt = text.lower()
    if 'park' in txt and '2022' in text and 'completed' in txt:
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

# Simple matching: check if park name is in funding name
total_funding = 0
matched_projects = set()

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    if not fund_name or fund_amount == 0:
        continue
    
    name_lower = fund_name.lower()
    
    for park in park_projects:
        park_lower = park.lower()
        if (park_lower in name_lower) or (name_lower in park_lower):
            if fund_name not in matched_projects:
                total_funding = total_funding + fund_amount
                matched_projects.add(fund_name)
                break

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
