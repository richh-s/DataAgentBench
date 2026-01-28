code = """import json

# Load civic documents from file
docs_file = locals()['var_functions.query_db:12']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Load funding data from file
funding_file = locals()['var_functions.query_db:14']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Documents:', len(documents))
print('Funding records:', len(funding_records))

# Find disaster-related projects mentioned in documents with 2022 references
disaster_keywords = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']
disaster_projects = []

for doc in documents:
    text = doc['text']
    filename = doc['filename']
    
    for keyword in disaster_keywords:
        if keyword in text:
            if '2022' in text or '2022' in filename:
                lines = text.split('\n')
                for line in lines:
                    if keyword in line:
                        project_name = line.strip()
                        if len(project_name) > 0:
                            disaster_projects.append(project_name)

print('Disaster projects with 2022:', len(disaster_projects))

# Get unique project names
unique_disaster_projects = list(set(disaster_projects))
print('Unique projects:', len(unique_disaster_projects))

# Find funding for these projects
funded_projects = []
total_amount = 0

for proj_name in unique_disaster_projects:
    for record in funding_records:
        if record['Project_Name'] == proj_name:
            amount = int(record['Amount'])
            total_amount += amount
            funded_projects.append({
                'name': proj_name,
                'amount': amount
            })

print('Total funding:', total_amount)
print('Funded projects count:', len(funded_projects))

# Return result
result = {'total_funding': total_amount}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'doc_count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
