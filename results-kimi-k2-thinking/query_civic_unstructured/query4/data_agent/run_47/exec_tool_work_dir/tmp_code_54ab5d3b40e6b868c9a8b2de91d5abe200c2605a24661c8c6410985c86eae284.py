code = """import json, os, re, sys

# Load funding data
funding_file = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Funding records: {len(funding_data)}")

# Load MongoDB data
mongo_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_32.json'
with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Civic docs: {len(civic_docs)}")

# Find all projects that mention Spring 2022
spring_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('spring' in text.lower() or 'Spring' in text):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for uppercase project names
            if line.isupper() and len(line) > 15 and not line.startswith('PAGE'):
                skip_words = ['AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:']
                found_skip = False
                for word in skip_words:
                    if word in line:
                        found_skip = True
                        break
                if not found_skip:
                    # Check if following lines mention Spring 2022
                    following = '\n'.join(lines[i:i+10])
                    if '2022' in following and 'pring' in following.lower():
                        spring_2022_projects.add(line)
            # Look for projects with year in name
            elif '2022' in line and len(line) > 10 and not any(x in line for x in ['Page', 'AGENDA ITEM', 'SUBJECT:']):
                spring_2022_projects.add(line)

project_list = sorted(list(spring_2022_projects))
print(f"Found {len(project_list)} Spring 2022 projects")
print("Projects:")
for proj in project_list:
    print(f"  - {proj}")

# Get funding for these projects
total_funding = 0
project_funding = {}
for project_name in project_list:
    # Find matching funding records
    for funding in funding_data:
        if funding['Project_Name'] == project_name:
            amount = int(funding['Amount'])
            total_funding += amount
            project_funding[project_name] = amount

print(f"Total funding for Spring 2022 projects: ${total_funding:,}")
print("Project funding details:")
for proj, amt in project_funding.items():
    print(f"  - {proj}: ${amt:,}")

result = {
    'project_count': len(project_list),
    'total_funding': total_funding,
    'projects': project_list,
    'funding_details': project_funding
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
