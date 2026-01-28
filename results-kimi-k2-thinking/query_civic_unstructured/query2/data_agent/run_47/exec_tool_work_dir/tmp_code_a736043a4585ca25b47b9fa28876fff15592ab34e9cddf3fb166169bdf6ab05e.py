code = """import json

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:6']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Simple manual extraction based on visible patterns
park_projects = [
    {'name': 'Bluffs Park Shade Structure', 'completion': 'November 2022'},
    {'name': 'Malibu Bluffs Park South Walkway Repairs', 'completion': None},  # Design phase
    {'name': 'Trancas Canyon Park Playground', 'completion': None},  # Design phase
    {'name': 'Legacy Park Benches and Arbors Renovation', 'completion': None},  # No date visible
    {'name': 'Legacy Park Paver Repair Project', 'completion': None}  # No date visible
]

# Find projects actually completed in 2022
completed_2022 = []
for doc in civic_docs:
    text = doc['text']
    # Look for park projects with 2022 completion
    if 'park' in text.lower() and '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        # Check for Bluffs Park Shade Structure specifically
        if 'Bluffs Park Shade Structure' in text and 'November 2022' in text:
            completed_2022.append('Bluffs Park Shade Structure')

print('Park projects completed in 2022:', completed_2022)

# Get funding for these park projects from funding database
park_names = [rec['Project_Name'].lower() for rec in funding_records]
print(f'Funding records count: {len(funding_records)}')

# Look for funding related to park projects
funding_for_parks_2022 = []
for rec in funding_records:
    name = rec['Project_Name'].lower()
    if ('park' in name and 
        ('shade' in name or 'bluff' in name or 'south walkway' in name)):
        funding_for_parks_2022.append({
            'project': rec['Project_Name'],
            'amount': int(rec['Amount'])
        })

print('Funding found:', funding_for_parks_2022)

total_funding = sum(f['amount'] for f in funding_for_parks_2022)

result = {
    'park_projects_2022': ['Bluffs Park Shade Structure'],
    'funding_records': funding_for_parks_2022,
    'total_funding': total_funding
}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'file_path': 'file_storage/functions.query_db:6.json', 'doc_count': 5}, 'var_functions.execute_python:22': {'text_length': 63698, 'doc_count': 5}}

exec(code, env_args)
