code = """import json

# Load funding data
with open('/tmp/results/20250219_143343_sqlite_funding_database_query_12.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
with open('/tmp/results/20250219_143343_mongodb_civic_docs_database_query_26.json', 'r') as f:
    civic_docs = json.load(f)

print(f'Funding records: {len(funding_data)}')
print(f'Civic docs: {len(civic_docs)}')

# Based on document analysis, identify projects that started Spring 2022
spring_2022_projects = [
    'Marie Canyon Green Streets',
    'PCH Median Improvements Project',
    'PCH Signal Synchronization System Improvements Project', 
    'Westward Beach Road Improvements Project',
    'Civic Center Water Treatment Facility Phase 2',
    'Bluffs Park Shade Structure',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)',
    'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)'
]

# Calculate total funding
total_funding = 0
funded_projects = []

for project in spring_2022_projects:
    for funding in funding_data:
        if funding['Project_Name'] == project:
            amount = int(funding['Amount'])
            total_funding += amount
            funded_projects.append((project, amount))
            break

print(f'\nSpring 2022 projects: {len(spring_2022_projects)}')
print(f'Total funding: ${total_funding:,}')

result = {
    'project_count': len(spring_2022_projects),
    'total_funding': total_funding,
    'projects': spring_2022_projects,
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:62': {'status': 'files_loaded'}}

exec(code, env_args)
