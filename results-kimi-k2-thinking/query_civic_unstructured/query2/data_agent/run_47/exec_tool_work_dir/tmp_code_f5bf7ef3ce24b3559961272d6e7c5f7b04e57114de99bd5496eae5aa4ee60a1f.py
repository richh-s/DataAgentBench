code = """import json

funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# From the civic documents analysis, we found:
# "Bluffs Park Shade Structure" was completed in November 2022
# This is park-related and completed in 2022

# Filter funding for this specific project
park_project_2022 = []
for rec in funding_records:
    if rec['Project_Name'] == 'Bluffs Park Shade Structure':
        park_project_2022.append({
            'project': rec['Project_Name'],
            'amount': int(rec['Amount'])
        })

total_funding = sum(p['amount'] for p in park_project_2022)

print('Park-related project completed in 2022:')
print(f"  - {park_project_2022[0]['project']}: ${park_project_2022[0]['amount']:,}")
print(f"Total funding: ${total_funding:,}")

result = {
    'project': 'Bluffs Park Shade Structure',
    'funding': total_funding
}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'file_path': 'file_storage/functions.query_db:6.json', 'doc_count': 5}, 'var_functions.execute_python:22': {'text_length': 63698, 'doc_count': 5}, 'var_functions.execute_python:26': {'park_projects_2022': ['Bluffs Park Shade Structure'], 'funding_records': [{'project': 'Bluffs Park Shade Structure', 'amount': 21000}, {'project': 'Bluffs Park Workout Station', 'amount': 39000}, {'project': 'Malibu Bluffs Park Roof Replacement Project', 'amount': 44000}, {'project': 'Malibu Bluffs Park South Walkway', 'amount': 91000}, {'project': 'Malibu Bluffs Park South Walkway Repairs', 'amount': 81000}], 'total_funding': 276000}}

exec(code, env_args)
