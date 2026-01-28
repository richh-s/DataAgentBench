code = """import json

# Load data from the stored files
civic_file = open('/tmp/results/20250219_143343_mongodb_civic_docs_database_query_42.json', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

funding_file = open('/tmp/results/20250219_143343_sqlite_funding_database_query_12.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Count records
print('Civic docs with 2022:', len(civic_docs))
print('Funding records:', len(funding_data))

# Find Spring 2022 projects
spring_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Check for project names with year
            if '2022' in line and len(line) > 10:
                if 'Page' not in line and 'AGENDA' not in line and 'SUBJECT' not in line:
                    spring_2022.append(line)
            # Check for uppercase project names
            elif line.isupper() and len(line) > 15 and 'PAGE' not in line and 'AGENDA' not in line:
                # Look ahead for Spring 2022 schedule
                ahead = '\n'.join(lines[i:i+10])
                if '2022' in ahead and 'pring' in ahead.lower():
                    spring_2022.append(line)

# Remove duplicates
unique_projects = []
seen = set()
for proj in spring_2022:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

unique_projects.sort()
project_count = len(unique_projects)

# Calculate funding
total_funding = 0
for proj in unique_projects:
    for fund in funding_data:
        if fund['Project_Name'] == proj:
            total_funding += int(fund['Amount'])

print('Spring 2022 projects:', project_count)
print('Total funding:', total_funding)

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
