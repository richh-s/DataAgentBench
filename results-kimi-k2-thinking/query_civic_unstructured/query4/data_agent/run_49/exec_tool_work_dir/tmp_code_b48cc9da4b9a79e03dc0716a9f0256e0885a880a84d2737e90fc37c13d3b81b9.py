code = """import json

# Get the data from storage
cdata = var_functions.query_db:10
data = var_functions.query_db:7

# Load data if they are file paths
if type(cdata) == str and cdata.endswith('.json'):
    with open(cdata, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cdata

if type(data) == str and data.endswith('.json'):
    with open(data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = data

# Build funding dictionary
funding_dict = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amt = int(rec.get('Amount', 0))
    funding_dict[name] = amt

# Find Spring 2022 projects
projects = []

# Check each document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Spring 2022 in text
    found_spring = False
    check_terms = ['2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May']
    for term in check_terms:
        if term in text:
            found_spring = True
            break
    
    if found_spring:
        # Extract project names from text
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Simple filter for project-like names
            if len(line) > 10 and any(word in line for word in ['Project', 'Improvements', 'Repairs', 'Drainage']):
                if line[0].isupper():
                    projects.append(line)

# Remove duplicates
projects = list(set(projects))

# Match with funding
matched = []
for proj in projects:
    if proj in funding_dict:
        matched.append({'name': proj, 'funding': funding_dict[proj]})

# Sum funding
total = sum(p['funding'] for p in matched)

result = {'count': len(matched), 'total': total, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
