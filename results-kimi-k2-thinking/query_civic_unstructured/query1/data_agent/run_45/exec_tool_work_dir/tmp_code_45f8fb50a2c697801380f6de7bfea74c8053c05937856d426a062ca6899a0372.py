code = """import json, re

funding_data = json.load(open(var_functions.query_db:2))
civic_data = json.load(open(var_functions.query_db:6))

funding_projects = set()
for item in funding_data:
    if float(item['Amount']) > 50000:
        funding_projects.add(item['Project_Name'])

capital_design_projects = set()
for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 10 and line not in ['', 'Page', 'Agenda']:
                if 'FEMA' not in line and 'CalOES' not in line and 'fire' not in line:
                    capital_design_projects.add(line)

matches = funding_projects.intersection(capital_design_projects)
result = len(matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
