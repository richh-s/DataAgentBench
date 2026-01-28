code = """import json
import re

civic_docs = json.load(open(locals()['var_functions.query_db:0']))
funding_data = json.load(open(locals()['var_functions.query_db:1']))

# Convert amounts
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Find projects
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'park' in text and 'completed' in text and '2022' in text:
        lines = doc.get('text', '').split('\n')
        for line in lines:
            stripped = line.strip()
            if len(stripped) > 10 and stripped[0].isupper():
                if 'park' in stripped.lower() and stripped not in found_projects:
                    found_projects.append(stripped)

# Match with funding
total = 0
matches = []

for project in found_projects:
    proj_key = project.lower()
    for fund in funding_data:
        fund_key = fund['Project_Name'].lower()
        if proj_key == fund_key or fund_key in proj_key or proj_key in fund_key:
            total += fund['Amount']
            matches.append({'project': project, 'matched_funding': fund['Project_Name'], 'amount': fund['Amount']})

result = {'projects': found_projects, 'matching_funds': matches, 'total': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
