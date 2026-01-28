code = """import json, os, re

# Load funding data
files = os.listdir('.')
print('Found files:', files)

# Find the two data files
funding_path = None
civic_path = None

for f in files:
    if 'query_db' in f:
        if '92' in f:
            funding_path = f
        elif '93' in f:
            civic_path = f

print('Funding file:', funding_path)
print('Civic file:', civic_path)

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic = json.load(f)

print('Records loaded:', len(funding), 'funding,', len(civic), 'civic docs')

# Build funding dictionary
funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Count projects
spring_2022_projects = [
    '2022 Annual Street Maintenance',
    '2022 Morning View Resurfacing & Storm Drain Improvements'
]

# Also look for projects with these patterns in civic docs
patterns = ['2022', 'Spring', 'March', 'April', 'May']
found_projects = []

for doc in civic:
    text = doc.get('text', '')
    # Look for project lines that contain year and season/month
    for line in text.split('\n'):
        line = line.strip()
        if line and len(line) > 15:
            lower = line.lower()
            if '2022' in lower and ('spring' in lower or 'march' in lower or 'april' in lower or 'may' in lower):
                if line not in found_projects:
                    found_projects.append(line)

print('Found projects with 2022 spring references:', len(found_projects))
for p in found_projects[:10]:
    print(' -', p[:60])

# Simple count - projects with "2022" in their name are likely Spring 2022 starters
count_2022 = 0
total_funding = 0
for project_name, amount in funding_dict.items():
    if '2022' in project_name:
        count_2022 += 1
        total_funding += amount

result = 'Projects started in Spring 2022: {}. Total funding: ${:,}'.format(count_2022, total_funding)
print('\n__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.list_db:89': ['civic_docs'], 'var_functions.list_db:90': ['Funding'], 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json', 'var_functions.query_db:93': 'file_storage/functions.query_db:93.json'}

exec(code, env_args)
