code = """import json, os, re

# Load the funding data
funding_file = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents with 2022 files  
mongo_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_52.json'
with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

print('Found', len(civic_docs), 'documents from 2022')

# From manual review of the 2022 document, these projects started in Spring 2022:
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
    '2021 Annual Street Maintenance',
    'Malibu Road Slope Repairs (CalOES Project)'
]

# Find which ones have funding data
funded_projects = []
total_funding = 0

for project_name in spring_2022_projects:
    for funding in funding_data:
        if funding['Project_Name'] == project_name:
            amount = int(funding['Amount'])
            total_funding += amount
            funded_projects.append((project_name, amount))
            break

# Check for similar names
all_project_names = [f['Project_Name'] for f in funding_data]

# Create final answer
answer = f"Projects that started in Spring 2022: {len(spring_2022_projects)}\n"
answer += f"Total funding: ${total_funding:,}\n\n"
answer += "Projects:\n"
for proj in spring_2022_projects:
    answer += f"  - {proj}\n"

answer += f"\nProjects with funding data: {len(funded_projects)}\n"
for proj, amt in funded_projects:
    answer += f"  - {proj}: ${amt:,}\n"

print(answer)

result = {
    'project_count': len(spring_2022_projects),
    'total_funding': total_funding,
    'funded_count': len(funded_projects),
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
