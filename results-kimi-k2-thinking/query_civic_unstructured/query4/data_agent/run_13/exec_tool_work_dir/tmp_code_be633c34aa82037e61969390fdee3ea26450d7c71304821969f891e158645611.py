code = """import json
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding = json.load(f)
projects = []
for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    text_lower = text.lower()
    if 'spring 2022' in text_lower or '2022-spring' in text_lower or ('2022' in text_lower and ('mar' in text_lower or 'apr' in text_lower or 'may' in text_lower)):
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if len(line_clean) > 15 and line_clean[0].isupper() and not line_clean.startswith('Page') and not line_clean.startswith('Item'):
                projects.append({'name': line_clean, 'doc': filename})
spring_count = len(projects)

funding_matches = []
total_amount = 0
for fund in funding:
    fund_name = fund['Project_Name'].lower()
    for proj in projects:
        if proj['name'].lower() in fund_name or fund_name in proj['name'].lower():
            funding_matches.append(fund)
            total_amount += int(fund['Amount'])
            break

result = {'spring_2022_projects': spring_count, 'funding_matches': len(funding_matches), 'total_funding': total_amount}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
