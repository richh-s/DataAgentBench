code = """import json
import re

# Load data
docs_file = locals()['var_functions.query_db:22']
funding_file = locals()['var_functions.query_db:14']

with open(docs_file, 'r') as f:
    documents = json.load(f)
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create mapping of project names to funding amounts
funding_map = {}
for record in funding_records:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

print("Number of unique funded projects:", len(funding_map))

# Find disaster-related projects with 2022 start dates
disaster_indicators = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']
alldisaster_projects = []

for doc in documents:
    text = doc['text']
    filename = doc['filename']
    
    # Check if document mentions 2022
    has202 = '2022' in text or '2022' in filename
    
    if has_2022:
        for indicator in disaster_indicators:
            if indicator in text:
                # Extract lines with disaster projects
                lines = text.split('\n')
                for line in lines:
                    if indicator in line:
                        clean_name = line.strip()
                        if len(clean_name) > 0:
                            alldisaster_projects.append(clean_name)

# Get unique disaster projects
disaster_projects = list(set(alldisaster_projects))
print("Unique disaster projects:", len(disaster_projects))

# Calculate funding for these projects
total_funding = 0
matched_projects = []

for proj in disaster_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
        matched_projects.append({'name': proj, 'amount': funding_map[proj]})

print("Total funding:", total_funding)
print("Matched projects:", len(matched_projects))

# Return result
result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'doc_count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
