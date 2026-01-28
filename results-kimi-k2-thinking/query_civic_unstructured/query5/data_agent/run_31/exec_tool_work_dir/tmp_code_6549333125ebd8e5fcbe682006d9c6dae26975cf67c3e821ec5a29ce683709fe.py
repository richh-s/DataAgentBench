code = """import json

# Load all data
docs_file = locals().get('var_functions.query_db:22', locals().get('var_functions.query_db:12'))
funding_file = locals()['var_functions.query_db:14']
funding_sum_result = locals()['var_functions.query_db:26']

with open(docs_file, 'r') as f:
    documents = json.load(f)
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Get disaster project names from funding data
disaster_project_names = []
for record in funding_records:
    name = record['Project_Name']
    if '(FEMA Project)' in name or '(CalOES Project)' in name or '(CalJPIA Project)' in name:
        disaster_project_names.append(name)

print('Disaster projects in funding data:', len(disaster_project_names))

# Look for projects with 2022 start dates in civic documents
projects_with_2022 = []

for doc in documents:
    text = doc['text']
    filename = doc['filename']
    has_2022 = '2022' in text or '2022' in filename
    
    if has_2022:
        for proj_name in disaster_project_names:
            if proj_name in text:
                projects_with_2022.append(proj_name)

# Get unique projects
unique_projects = list(set(projects_with_2022))
print('Disaster projects with 2022 refs:', len(unique_projects))

# Sum funding for these projects
total_funding = 0
for proj in unique_projects:
    for record in funding_records:
        if record['Project_Name'] == proj:
            total_funding += int(record['Amount'])

print('Total funding:', total_funding)

result = {'total_funding_2022': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'doc_count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'Total_Funding': '845000'}]}

exec(code, env_args)
