code = """import json
import re

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:5

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    if 'text' in doc:
        text = doc['text']
        if 'Capital' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) < 80 and 'Updates' not in line and 'Schedule' not in line:
                    lower = line.lower()
                    if ('road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower or 'bridge' in lower):
                        name = re.sub(r'^[\d\.\-\s]+', '', line)
                        name = re.sub(r'\s+', ' ', name).strip()
                        if len(name) > 5:
                            extracted_projects.append(name)

unique_projects = list(set(extracted_projects))

funding_filtered = {}
for f in funding_data:
    amt = int(f['Amount'])
    if amt > 50000:
        funding_filtered[f['Project_Name']] = amt

def normalize(name):
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'\([^\)]+\)', '', name)
    name = re.sub(r'[^a-z0-9\s]', '', name)
    return name.strip()

count = 0
for proj in unique_projects:
    proj_norm = normalize(proj)
    if proj_norm:
        for fund_name, amount in funding_filtered.items():
            fund_norm = normalize(fund_name)
            if proj_norm in fund_norm or fund_norm in proj_norm:
                count = count + 1
                break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
