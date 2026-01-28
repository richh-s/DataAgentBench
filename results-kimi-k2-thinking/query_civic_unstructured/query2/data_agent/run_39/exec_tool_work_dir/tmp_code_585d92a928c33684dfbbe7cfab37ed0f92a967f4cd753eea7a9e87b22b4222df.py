code = """import json

# Load data
mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

# Build a map of funding amounts by project name for lookup
funding_map = {}
for rec in funding_recs:
    proj_name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_map[proj_name] = amount

# Look for specific park projects completed in 2022 based on the document preview
# From the preview, we know these were completed in 2022:
# - Bluffs Park Shade Structure (completed November 2022)
# - Broad Beach Road Water Quality Repair (completed November 2022)
# - Point Dume Walkway Repairs (completed November 2022)
# These mention parks or are in park-related contexts

park_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs',
    'Marie Canyon Green Streets',
]

# Check if these appear in funding data with different exact names
funding_project_names = list(funding_map.keys())
funding_total = 0
matched = []

for park in park_projects:
    park_lower = park.lower()
    for fund_name in funding_project_names:
        fund_lower = fund_name.lower()
        if park_lower == fund_lower or park_lower in fund_lower or fund_lower in park_lower:
            amount = funding_map[fund_name]
            funding_total += amount
            matched.append({'project': park, 'funding_name': fund_name, 'amount': amount})
            break

print('__RESULT__:')
print(json.dumps({'total_funding': funding_total, 'matched_projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}, 'var_functions.execute_python:58': {'mongo_docs_count': 19, 'funding_records_count': 500}}

exec(code, env_args)
