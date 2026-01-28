code = """import json

# Load the civic documents and funding data
with open('/tmp/results/20250219_143343_mongodb_civic_docs_database_query_42.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/results/20250219_143343_sqlite_funding_database_query_12.json', 'r') as f:
    funding_data = json.load(f)

# Extract projects that mention Spring 2022 in their schedule
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('spring' in text.lower() or 'Spring' in text):
        # Look for project names (uppercase lines)
        for line in text.split('\n'):
            line = line.strip()
            if line.isupper() and len(line) > 15 and 'PAGE' not in line and 'AGENDA' not in line and 'COMMISSION' not in line and 'MEETING' not in line:
                spring_projects.add(line)
        # Also catch projects with year in name
        for line in text.split('\n'):
            line = line.strip()
            if '2022' in line and len(line) > 10 and 'Page' not in line and 'AGENDA' not in line:
                spring_projects.add(line)

final_projects = sorted(list(spring_projects))
print(f"Spring 2022 projects: {len(final_projects)}")

# Calculate total funding
total_funding = 0
for project in final_projects:
    for funding in funding_data:
        if funding['Project_Name'] == project:
            total_funding += int(funding['Amount'])

print(f"Total funding: ${total_funding:,}")

result = {
    'project_count': len(final_projects),
    'total_funding': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
