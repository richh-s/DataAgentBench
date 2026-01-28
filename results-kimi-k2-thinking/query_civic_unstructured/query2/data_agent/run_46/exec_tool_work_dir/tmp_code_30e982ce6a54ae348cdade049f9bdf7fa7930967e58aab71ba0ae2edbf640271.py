code = """import json, re

# Load civic documents
civic_docs file = '../var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = '../var_functions.query_db:10'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract projects from text
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for patterns indicating completed park projects in 2022
    
    # Bluffs Park Shade Structure - completed Nov 2022
    if 'Bluffs Park Shade Structure' in text and 'completed November 2022' in text:
        projects.append({
            'name': 'Bluffs Park Shade Structure',
            'status': 'completed',
            'year': '2022',
            'topics': 'park'
        })

# Get all fundings as lookup
funding_lookup = {}
for item in funding_data:
    name = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[name] = int(item['Amount'])

# Find matches
total = 0
matched = []

for proj in projects:
    proj_key = proj['name'].lower().replace(' ', '')
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total += amount
        matched.append({
            'project': proj['name'],
            'amount': amount
        })

print('__RESULT__:')
print(json.dumps({
    'total_funding': total,
    'projects': matched
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
