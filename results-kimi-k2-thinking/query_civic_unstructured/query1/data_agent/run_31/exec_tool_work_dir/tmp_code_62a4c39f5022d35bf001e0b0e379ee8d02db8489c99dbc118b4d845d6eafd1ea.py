code = """import json

funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:5

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) < 80 and 'Updates' not in line and 'Schedule' not in line:
                lower = line.lower()
                if 'road' in lower or 'park' in lower or 'canyon' in lower or 'project' in lower or 'storm' in lower:
                    design_project_names.append(line)

unique_names = []
seen = set()
for name in design_project_names:
    if name not in seen:
        seen.add(name)
        unique_names.append(name)

funding_over_50k = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_over_50k[item['Project_Name']] = amount

def simple_normalize(name):
    name = name.lower()
    name = name.replace('(', '').replace(')', '')
    name = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in name)
    name = ' '.join(name.split())
    return name

count = 0
for proj in unique_names:
    proj_clean = simple_normalize(proj)
    if proj_clean:
        for fund_name, amount in funding_over_50k.items():
            fund_clean = simple_normalize(fund_name)
            if proj_clean in fund_clean or fund_clean in proj_clean:
                count += 1
                break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
