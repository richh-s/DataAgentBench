code = """import json
import re

f_file = var_functions.query_db:2
c_file = var_functions.query_db:6

with open(f_file, 'r') as file1:
    funding = json.load(file1)

with open(c_file, 'r') as file2:
    civic = json.load(file2)

fund_dict = {}
for item in funding:
    amt = float(item['Amount'])
    if amt > 50000:
        name = item['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_dict[name] = amt
        fund_dict[clean_name] = amt

design_projects = []
for doc in civic:
    text_content = doc.get('text', '')
    if 'Design' in text_content:
        lines = text_content.split('\n')
        for line in lines:
            stripped = line.strip()
            if len(stripped) > 15:
                if all(x not in stripped for x in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                    if all(x not in stripped.upper() for x in ['PAGE', 'AGENDA', 'RECOMMENDED']):
                        if all(x not in stripped for x in ['Updates:', 'Schedule:']):
                            design_projects.append(stripped)

count = 0
for project in design_projects:
    project_clean = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    if project in fund_dict or project_clean in fund_dict:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
