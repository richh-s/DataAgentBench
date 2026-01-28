code = """import json

# Load funding data
f_path = locals()['var_functions.query_db:10']
with open(f_path, 'r') as f:
    funding = json.load(f)

# Load civic docs  
c_path = locals()['var_functions.query_db:11']
with open(c_path, 'r') as f:
    civic = json.load(f)

# Get park projects from funding data
park_funding = []
for item in funding:
    if 'park' in item['Project_Name'].lower():
        park_funding.append({
            'name': item['Project_Name'],
            'amount': int(item['Amount'])
        })

# Find park projects completed in 2022 from civic documents
doc_text = civic[0]['text']
lines = doc_text.splitlines()

completed_2022 = []
for line in lines:
    line_lower = line.lower()
    if 'park' in line_lower and '2022' in line_lower and ('completed' in line_lower or 'completion' in line_lower):
        completed_2022.append(line.strip())

# Match projects and calculate total
total_funding = 0
for fund in park_funding:
    for proj in completed_2022:
        if fund['name'] in proj:
            total_funding += fund['amount']

print('__RESULT__:')
print(total_funding)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
