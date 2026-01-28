code = """import json

# Load the data
civic_docs_path = 'var_functions.query_db:46'
funding_path = 'var_functions.query_db:48'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Build funding map
funding = {}
for rec in funding_recs:
    funding[rec['Project_Name']] = int(rec['Amount'])

# Find park projects completed in 2022 based on the documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for park projects with 2022 completion date
    if 'Bluffs Park Shade Structure' in text and '2022' in text:
        park_projects_2022.append('Bluffs Park Shade Structure')
    
    if 'Broad Beach Road Water Quality Repair' in text and '2022' in text and ('park' in text.lower() or 'Park' in text):
        park_projects_2022.append('Broad Beach Road Water Quality Repair')
    
    # Check for other park projects
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if len(line) > 10:
            lower = line.lower()
            if 'park' in lower and ('completed' in lower or 'completion' in lower):
                if '2022' in lower:
                    clean_name = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                    park_projects_2022.append(clean_name)

# Remove duplicates
unique = list(set(park_projects_2022))

# Calculate total funding for these projects
total = 0
for proj in unique:
    if proj in funding:
        total += funding[proj]

result = '$' + str(total)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:44': [{'total_funding': '1033000'}], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
