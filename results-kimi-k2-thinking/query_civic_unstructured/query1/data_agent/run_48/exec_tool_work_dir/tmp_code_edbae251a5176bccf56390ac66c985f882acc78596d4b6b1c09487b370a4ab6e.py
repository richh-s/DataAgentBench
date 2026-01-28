code = """import json

# Load funding data
funding_file = open('funding_data.json', 'w')
funding_path = var_functions.query_db:70
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = open('civic_docs.json', 'w')
civic_path = var_functions.query_db:2
with open(civic_path) as f:
    civic_docs = json.load(f)

# Process data
high_funding = set()
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding.add(f['Project_Name'])

design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        design_projects.append(text)

# Return simple count
result = len(design_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
