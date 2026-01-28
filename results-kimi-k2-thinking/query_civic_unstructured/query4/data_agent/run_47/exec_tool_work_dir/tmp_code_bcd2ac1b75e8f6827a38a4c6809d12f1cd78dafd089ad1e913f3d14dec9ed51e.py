code = """import json
import os

# Load funding data
funding_file = open('/tmp/results/20250219_143343_sqlite_funding_database_query_12.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load civic documents
mongo_file = open('/tmp/results/20250219_143343_mongodb_civic_docs_database_query_42.json', 'r')
civic_docs = json.load(mongo_file)
mongo_file.close()

# Find projects that started in Spring 2022
spring_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Identify projects with year 2022 in the name
        if ('2022' in line and len(line) > 10 and 
            'Page' not in line and 'AGENDA' not in line and 'SUBJECT' not in line):
            spring_2022_projects.add(line)
        
        # Identify projects in uppercase with following spring schedule
        elif (line.isupper() and len(line) > 15 and 'PAGE' not in line and 
              'AGENDA' not in line and 'COMMISSION' not in line and 'MEETING' not in line and
              'SUBJECT' not in line and 'RECOMMENDED ACTION' not in line):
            # Look ahead for Spring 2022 scheduling
            following = '\n'.join(lines[i:i+15])
            if '2022' in following and 'pring' in following.lower() and 'Advertise' in following:
                spring_2022_projects.add(line)

# Clean up - remove any header lines that got through
final_projects = []
for proj in spring_2022_projects:
    if (len(proj) > 15 and not proj.startswith('PAGE') and 'AGENDA' not in proj and 
        'PUBLIC WORKS COMMISSION' not in proj and 'MEETING' not in proj and
        'SUBJECT:' not in proj and 'RECOMMENDED ACTION:' not in proj):
        final_projects.append(proj)

final_projects.sort()
project_count = len(final_projects)

# Calculate total funding for these projects
total_funding = 0
for project_name in final_projects:
    for funding in funding_data:
        if funding.get('Project_Name') == project_name:
            total_funding += int(funding.get('Amount', 0))

# Create result
result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
