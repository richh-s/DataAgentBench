code = """import json
import sys
import os

# Load the data from files
civic_docs_path = 'var_functions.query_db:8'
funding_path = 'var_functions.query_db:10'

# Read civic docs
civic_docs = []
try:
    with open(civic_docs_path if civic_docs_path.endswith('.json') else civic_docs_path + '.json', 'r') as f:
        civic_docs = json.load(f)
except:
    # Try reading as string path
    civic_docs = json.loads(open(civic_docs_path.replace('var_', ''), 'r').read())

# Read funding data
funding_data = []
try:
    with open(funding_path if funding_path.endswith('.json') else funding_path + '.json', 'r') as f:
        funding_data = json.load(f)
except:
    funding_data = json.loads(open(funding_path.replace('var_', ''), 'r').read())

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Based on document preview, these park projects were completed in 2022:
projects_2022 = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

# Verify by checking the text
actual_projects = []
total_text = ' '.join([doc.get('text', '') for doc in civic_docs])

for proj in projects_2022:
    if proj in total_text and '2022' in total_text:
        # Check vicinity for completion mention
        idx = total_text.find(proj)
        snippet = total_text[idx:idx+300]
        if 'completed' in snippet.lower() and '2022' in snippet:
            actual_projects.append(proj)

# Calculate total funding
total_funding = 0
matched = []

for proj in actual_projects:
    proj_key = proj.lower().replace(' ', '')
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total_funding += amount
        matched.append({'project': proj, 'amount': amount})

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'projects': matched
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
