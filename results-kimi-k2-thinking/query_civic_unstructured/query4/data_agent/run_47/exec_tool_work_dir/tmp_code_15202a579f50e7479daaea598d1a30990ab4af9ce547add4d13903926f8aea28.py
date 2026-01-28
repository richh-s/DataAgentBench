code = """import json
import os

# Load funding data
funding_file = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load MongoDB data  
mongo_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_32.json'
with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic docs: {len(civic_docs)}")

# Find Spring 2022 projects
spring_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for project name patterns
        if line.isupper() and len(line) > 15 and 'PAGE' not in line:
            skip = False
            for term in ['AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:']:
                if term in line:
                    skip = True
                    break
            if not skip:
                following = '\n'.join(lines[i:i+10])
                if '2022' in following and 'pring' in following.lower():
                    spring_2022_projects.add(line)
        elif '2022' in line and len(line) > 10 and 'Page' not in line and 'AGENDA' not in line:
            spring_2022_projects.add(line)

project_list = sorted(list(spring_2022_projects))
print(f"Spring 2022 projects: {len(project_list)}")
for proj in project_list:
    print(f"  - {proj}")

# Calculate funding
total_funding = 0
for project_name in project_list:
    for funding in funding_data:
        if funding['Project_Name'] == project_name:
            total_funding += int(funding['Amount'])

print(f"Total funding: ${total_funding:,}")
result = {'project_count': len(project_list), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
