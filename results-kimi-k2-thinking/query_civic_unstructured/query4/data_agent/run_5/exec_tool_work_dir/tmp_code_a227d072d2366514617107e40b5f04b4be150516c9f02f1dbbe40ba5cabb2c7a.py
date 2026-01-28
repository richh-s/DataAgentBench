code = """import json

# Get the stored data from previous query results
civic_result = locals()['var_functions.query_db:82']
funding_result = locals()['var_functions.query_db:83']

# Load the data (they're stored as file paths)
if isinstance(civic_result, str):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

if isinstance(funding_result, str):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Build funding lookup (project name -> total amount)
funding_lookup = {}
for rec in funding_data:
    project_name = rec['Project_Name']
    amount = int(rec['Amount'])
    if project_name in funding_lookup:
        funding_lookup[project_name] += amount
    else:
        funding_lookup[project_name] = amount

# From the data previews and analysis:
# These are the projects that started in Spring 2022
spring_2022_project_names = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    '2022 Annual Street Maintenance'
]

# Count projects and calculate total funding
count = 0
total_funding = 0
matched_projects = []

for project_name in spring_2022_project_names:
    if project_name in funding_lookup:
        count += 1
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({
            'project': project_name,
            'funding': amount
        })

# Create final result
result = {
    'count': count,
    'total_funding': total_funding,
    'projects': matched_projects
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
