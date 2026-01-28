code = """import json, os

# Find the data files
files = os.listdir('.')
funding_file = [f for f in files if 'query_db' in f and 'Project_Name' in str(open(f, 'r').read(200))][0]
civic_file = [f for f in files if 'query_db' in f and 'text' in str(open(f, 'r').read(200))][0]

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Build funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Projects with 2022 in their name are likely Spring 2022 projects
spring_2022_projects = []
for project_name in funding_dict.keys():
    if '2022' in project_name and 'Annual' not in project_name:
        spring_2022_projects.append(project_name)

# Also search civic documents for Spring 2022 mentions and extract project names
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', 'Spring 2022', 'March 2022', 'April 2022', 'May 2022']
for doc in civic_data:
    text = doc.get('text', '')
    text_lower = text.lower()
    for pattern in spring_patterns:
        if pattern.lower() in text_lower:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 15 and (line.istitle() or (line[0].isupper() and len(line.split()) > 2)):
                    if line not in spring_2022_projects and line in funding_dict:
                        spring_2022_projects.append(line)

# Calculate total funding
total_funding = 0
for project in spring_2022_projects:
    total_funding += funding_dict[project]

# Format result
project_count = len(spring_2022_projects)
funding_formatted = '{:,}'.format(total_funding)
result = 'Projects started in Spring 2022: {}. Total funding: ${}'.format(project_count, funding_formatted)

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.list_db:89': ['civic_docs'], 'var_functions.list_db:90': ['Funding'], 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:93': 'file_storage/functions.query_db:93.json', 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:105': 'file_storage/functions.query_db:105.json'}

exec(code, env_args)
