code = """import json
import re

# Load funding data for 2022 projects
funding_file = open('var_functions.query_db:38', 'r')
funding_2022 = json.load(funding_file)
funding_file.close()

# Load civic documents
civic_file = open('var_functions.query_db:14', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

print('Funding records for 2022:', len(funding_2022))
print('Civic documents loaded:', len(civic_docs))

# Create set of 2022 project names from funding
funding_project_names = set()
for f in funding_2022:
    funding_project_names.add(f.get('Project_Name', ''))

print('2022 project names from funding:', list(funding_project_names))

# Now search civic docs for these projects and verify Spring 2022 start
spring_2022_confirmed = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check each 2022 project name
    for project_name in funding_project_names:
        if project_name.lower() in text.lower():
            # Look for Spring 2022 dates near this project name
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if project_name.lower() in line.lower():
                    # Look ahead for schedule info
                    for j in range(i, min(i+10, len(lines))):
                        next_line = lines[j].strip()
                        # Check if this line has Spring 2022 or March/April/May 2022
                        if ('2022' in next_line and 
                            ('Spring' in next_line or 'March' in next_line or 'April' in next_line or 'May' in next_line)):
                            spring_2022_confirmed.append(project_name)
                            break

# Remove duplicates
spring_2022_confirmed = list(set(spring_2022_confirmed))

# Calculate total funding for confirmed Spring 2022 projects
total_funding = 0
for project in spring_2022_confirmed:
    for fund in funding_2022:
        if fund.get('Project_Name') == project:
            total_funding += int(fund.get('Amount', 0))

result = {
    'project_count': len(spring_2022_confirmed),
    'total_funding': total_funding,
    'projects': spring_2022_confirmed
}

print('Confirmed Spring 2022 projects:', spring_2022_confirmed)
print('Total funding:', total_funding)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': []}

exec(code, env_args)
