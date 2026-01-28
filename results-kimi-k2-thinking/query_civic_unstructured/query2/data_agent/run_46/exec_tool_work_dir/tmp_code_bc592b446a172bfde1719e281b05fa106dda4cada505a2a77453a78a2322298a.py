code = """import json
import re

# Load the data
civic_docs_file = '../var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = '../var_functions.query_db:10'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Look specifically for projects mentioned as completed in 2022 in the text
# From the preview, I saw:
# - Bluffs Park Shade Structure - completed November 2022
# - Broad Beach Road Water Quality Repair - completed November 2022
# - Point Dume Walkway Repairs - completed November 2022  
# - Marie Canyon Green Streets - completed January 2023 (but notice filed Jan 2023, so likely completed late 2022)

potential_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

# Check which of these are in the funding data and sum amounts
total_amount = 0
matched = []

for proj in potential_projects:
    proj_key = proj.lower().replace(' ', '')
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total_amount += amount
        matched.append({
            'project': proj,
            'amount': amount
        })

print('__RESULT__:')
result = {
    'total_funding': total_amount,
    'projects': matched
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
