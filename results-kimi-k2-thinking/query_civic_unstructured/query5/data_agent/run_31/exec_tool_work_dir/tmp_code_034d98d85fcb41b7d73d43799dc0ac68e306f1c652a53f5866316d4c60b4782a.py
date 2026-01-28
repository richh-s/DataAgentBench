code = """import json
import re

# Load documents
docs_file = locals()['var_functions.query_db:12']
with open(docs_file, 'r') as f:
    documents = json.load(f)

print("Civic documents loaded:", len(documents))

# Load funding data
funding_file = locals()['var_functions.query_db:14']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print("Funding records loaded:", len(funding_records))

# Simplified parsing - look for disaster-related projects
# We'll use a simpler approach without complex regex

disaster_projects = []

for doc in documents:
    text = doc['text']
    filename = doc['filename']
    
    # Look for FEMA, CalOES, CalJPIA projects with 2022 in the text or filename
    if '(FEMA Project)' in text or '(CalOES Project)' in text or '(CalJPIA Project)' in text:
        if '2022' in text or '2022' in filename:
            # Extract lines containing these projects
            lines = text.split('\n')
            for line in lines:
                if '(FEMA Project)' in line or '(CalOES Project)' in line or '(CalJPIA Project)' in line:
                    project_name = line.strip()
                    disaster_projects.append({
                        'Project_Name': project_name,
                        'source': filename
                    })

print("\nDisaster projects found:", len(disaster_projects))

for i, proj in enumerate(disaster_projects[:15]):
    print(f"{i+1}. {proj['Project_Name'][:80]}...")

# Now get funding for these projects
project_names = [proj['Project_Name'] for proj in disaster_projects]

total_funding = 0
funded_projects = []

for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    
    for disaster_proj in disaster_projects:
        if disaster_proj['Project_Name'] == project_name:
            total_funding += amount
            funded_projects.append({
                'project': project_name,
                'amount': amount,
                'source': record['Funding_Source']
            })

print(f"\nTotal funding for disaster projects: ${total_funding:,}")
print(f"Number of funded projects: {len(funded_projects)}")

# Return result
result = {
    'total_funding': total_funding,
    'project_count': len(funded_projects),
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'doc_count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'filename': 'malibucity_agenda_03222023-2060.txt'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
