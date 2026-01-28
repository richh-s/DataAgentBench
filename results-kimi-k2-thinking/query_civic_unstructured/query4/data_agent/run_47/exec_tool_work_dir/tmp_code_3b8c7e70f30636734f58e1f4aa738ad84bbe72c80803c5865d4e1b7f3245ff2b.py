code = """import json

# Load data
civic_path = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_68.json'
funding_path = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'

civic_file = open(civic_path, 'r')
civic_docs = json.load(civic_file)
civic_file.close()

funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')

# Manually reviewed 2022 projects that started in Spring:
spring_projects = [
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

# Get funding for these projects
total = 0
funded = []
for proj in spring_projects:
    for fund in funding_data:
        if fund['Project_Name'] == proj:
            total += int(fund['Amount'])
            funded.append((proj, int(fund['Amount'])))
            break

result = {
    'project_count': len(spring_projects),
    'total_funding': total,
    'projects': spring_projects,
    'funded': funded
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:62': {'status': 'files_loaded'}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
