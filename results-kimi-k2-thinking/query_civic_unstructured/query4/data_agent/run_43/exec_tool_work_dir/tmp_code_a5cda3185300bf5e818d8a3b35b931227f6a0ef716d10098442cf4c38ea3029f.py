code = """import json

# Load data files
civic_path = locals()['var_functions.query_db:22']
funding_path = locals()['var_functions.query_db:19']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_list = json.load(f)

# Create funding dictionary
funding_dict = {}
for item in funding_list:
    funding_dict[item['Project_Name']] = int(item['Total_Amount'])

# Find projects with 2022 in text and extract names
project_names = set()
for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 15:
                if any(kw in line for kw in ['Project', 'Improvements', 'Repair']) and (line.istitle() or line.isupper()):
                    clean_line = ''.join(c for c in line if c.isalnum() or c.isspace() or c in '&-')
                    project_names.add(' '.join(clean_line.split()))

# Match and sum funding
total = 0
matched = []
for name in project_names:
    amount = funding_dict.get(name, 0)
    if amount == 0:
        base = name.split('(')[0].strip()
        amount = funding_dict.get(base, 0)
    if amount > 0:
        total += amount
        matched.append({'name': name, 'funding': amount})

# Return result
print('__RESULT__:')
print(json.dumps({'count': len(matched), 'total': total, 'projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
