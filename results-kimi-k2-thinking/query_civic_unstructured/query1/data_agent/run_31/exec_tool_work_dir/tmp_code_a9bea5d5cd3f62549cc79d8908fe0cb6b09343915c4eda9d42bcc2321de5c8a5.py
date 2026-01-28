code = """import json
import re

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:5

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) < 80 and 'Updates:' not in line:
                if 'Schedule:' not in line:
                    line_lower = line.lower()
                    if 'road' in line_lower or 'park' in line_lower:
                        clean_name = re.sub(r'^[\d\.\s\-]+', '', line)
                        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
                        if len(clean_name) > 5:
                            design_projects.append(clean_name)

unique_design = list(set(design_projects))

funding_dict = {}
for f in funding_data:
    if int(f['Amount']) > 50000:
        funding_dict[f['Project_Name']] = int(f['Amount'])

def normalize(name):
    if not name:
        return ''
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'\([^\)]+\)', '', name)
    name = re.sub(r'[^a-z0-9\s]', '', name)
    return name.strip()

count = 0
for proj in unique_design:
    proj_norm = normalize(proj)
    if proj_norm:
        for funding_name, amount in funding_dict.items():
            fund_norm = normalize(funding_name)
            if proj_norm in fund_norm or fund_norm in proj_norm:
                count = count + 1
                break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
