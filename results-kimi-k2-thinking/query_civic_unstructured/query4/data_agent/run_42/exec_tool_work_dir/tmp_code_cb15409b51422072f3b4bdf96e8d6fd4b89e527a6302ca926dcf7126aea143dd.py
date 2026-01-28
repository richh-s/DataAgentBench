code = """import json
import re

# Load MongoDB data
mongo_file_location = locals()['var_functions.query_db:42']
funding_file_location = locals()['var_functions.query_db:4']

with open(mongo_file_location, 'r') as file1:
    mongo_docs = json.load(file1)

with open(funding_file_location, 'r') as file2:
    funding_recs = json.load(file2)

# Create funding lookup map
funding_map = {}
for record in funding_recs:
    funding_map[record['Project_Name']] = int(record['Amount'])

# Find projects starting in Spring 2022
spring_projects = set()

for document in mongo_docs:
    text_content = document.get('text', '')
    lines = text_content.split('\n')
    
    for index in range(len(lines)):
        line = lines[index]
        if 'Begin Construction' in line and '2022' in line and 'Spring' in line:
            for backtrack in range(index-1, max(index-10, -1), -1):
                project_line = lines[backtrack].strip()
                if project_line and project_line[0] != '(' and 'Schedule' not in project_line:
                    if len(project_line) > 5:
                        spring_projects.add(project_line)
                        break

# Match with funding and calculate totals
matched_list = []
for project_name in spring_projects:
    if project_name in funding_map:
        amount = funding_map[project_name]
        matched_list.append({'name': project_name, 'funding': amount})

project_count = len(matched_list)
total_funding_amount = sum(item['funding'] for item in matched_list)

result_data = {'count': project_count, 'total_funding': total_funding_amount}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
