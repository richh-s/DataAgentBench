code = """import json

civic_docs = json.load(open(locals()['var_functions.query_db:0']))
funding_data = json.load(open(locals()['var_functions.query_db:1']))

for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc['text']
    if 'park' in text.lower() and 'completed' in text.lower() and '2022' in text:
        # Extract relevant project names
        if 'Bluffs Park Shade Structure' in text and 'Bluffs Park Shade Structure' not in park_projects:
            park_projects.append('Bluffs Park Shade Structure')
        if 'Point Dume Walkway Repairs' in text and 'Point Dume Walkway Repairs' not in park_projects:
            park_projects.append('Point Dume Walkway Repairs')

# Calculate funding
total = 0
matches = []
for project in park_projects:
    p_lower = project.lower()
    for fund in funding_data:
        f_lower = fund['Project_Name'].lower()
        if p_lower == f_lower or f_lower in p_lower or p_lower in f_lower:
            total += fund['Amount']
            matches.append({'project': project, 'funding': fund['Project_Name'], 'amount': fund['Amount']})

result = {'total_funding': total, 'projects': park_projects, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:24': {'civic_docs': 5, 'funding': 500}, 'var_functions.execute_python:26': {'specific_park_projects': ['Bluffs Park Shade Structure', 'Point Dume Walkway Repairs'], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'funding_record': 'Bluffs Park Shade Structure', 'amount': 21000, 'source': 'Government Grant'}, {'project': 'Point Dume Walkway Repairs', 'funding_record': 'Point Dume Walkway Repairs', 'amount': 59000, 'source': 'International Aid'}], 'total_funding': 80000, 'record_count': 2}}

exec(code, env_args)
